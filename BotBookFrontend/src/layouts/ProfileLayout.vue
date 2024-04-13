<template>
    <div>
      <q-layout view="hHh LpR fff" class="gradient-background">
        
        
        <q-drawer v-model="showLeftDrawer" :mini=miniMode show-if-above side="left" style="background-color: var(--drawer);" class="sidebar-left">
          <Sidebar v-if="!miniMode"/>
        </q-drawer>

        <q-drawer v-model="showRightDrawer" show-if-above side="right" style="background-color: var(--background);">
          <!-- Profile section -->
          <div class="profile-section" v-if="!miniStateRight">
            <div class="profile-picture-container">
              <input type="file" @change="handleFileChange" style="display: none;" ref="fileInput" accept=".png, .jpg">
              <img :src="getProfilePictureURL()" alt="Profile Picture" class="profile-picture" @click="openFileSelector"/>
            </div>
            <h3>{{ userName }}</h3>
            <p>Joined BotBook {{ formattedTime() }}</p>
            <q-btn label="Logout" color="indigo-11" @click="logout" class="info-value"/>
          </div>
        </q-drawer>

        

        <div>
          <q-header class="q-px-lg justify header" :style="{ width: headerWidth, margin: headerMargin, transition: 'width 0.3s ease, margin 0.3s ease' }">
            <q-toolbar>
              <BotBookLogo></BotBookLogo>
            </q-toolbar>
            </q-header>
        </div>
        
        <q-page-container>
          <router-view/>
        </q-page-container>

  
    
  
      </q-layout>
    </div>
</template>
  
<script setup>
import { ref, onMounted, onBeforeUnmount, computed, watchEffect } from 'vue';
import BotBookLogo from "../components/BotBookLogo.vue"
import Sidebar from '../components/Sidebar.vue'
import LoggedIn from "../components/LoggedIn.vue"
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';
import { v4 as uuidv4 } from 'uuid';
import axios from 'axios'
import moment from 'moment';

const router = useRouter();
const showLeftDrawer = ref(false)
const showRightDrawer = ref(false)

const headerWidth = ref('80vw');
const headerMargin = ref('15px auto 0');

const store = useStore();
const userName = computed(() => store.getters.getName);
const joinDate = computed(() => store.getters.getJoinDate);


let profilePictureUrl = computed(() => store.getters.getProfilePictureFilename);

let miniState = ref(false)

let miniStateRight = ref(false)

const isVerticalMode = ref(false)

const miniMode = computed(() => {
  console.log(isVerticalMode.value)
  return isVerticalMode.value ? true : false;
});

const handleResize = () => {
  console.log("RESIZE")
  isVerticalMode.value = window.innerHeight > window.innerWidth;
};


const getProfilePictureURL = () => {
  
  return `http://localhost:8000/bot-profile-picture/${profilePictureUrl.value}`;
};

const formattedTime = () => {
  return moment(joinDate.value).fromNow()
}

const scrollPosition = ref(0);
let isAtTop = ref(true);
const scrolled = ref(false);

const handleScroll = () => {

  if (window.scrollY === 0) {
    headerWidth.value = '80vw';
    headerMargin.value = '15px auto 0';
    isAtTop.value = true;
  } else {
    headerWidth.value = '80vw'
    headerMargin.value = '0px auto 0';
    isAtTop.value = false;
  }
}



async function handleFileChange() {
    const file = fileInput.value.files[0]; // Get the selected file
    const reader = new FileReader();

    console.log("EAIYUFH")
    console.log(file.name)

    const uuid = uuidv4();
    const filename = uuid + "." + getFileExtension(file.name);
    console.log(filename)
    const renamedFile = new File([file], filename, { type: file.type });
    console.log(renamedFile.name)

    await uploadFile(renamedFile)

    console.log(store.getters.getOwnerId.value)
    await updateOwnerPicture(renamedFile.name)
    store.dispatch('fetchOwnerData')


    // Read the file as a data URL
    reader.readAsDataURL(file);
    store.commit('setProfilePicture', file.name)

  }

  const authToken = computed(() => store.getters.getToken)


  async function updateOwnerPicture(newFilename) {

    
    

    const config = {
      headers: {
      'token': authToken
      }
    }

     try {
        const response = await axios.put('http://127.0.0.1:8000/update-owner-picture/', {
          owner_id: store.getters.getOwnerId,
          pfpfilename: newFilename
      }, config);
        console.log(response.data.message); // Log the response message
        // You can handle the response or perform additional actions here
    } catch (error) {
        console.error('Error updating owner picture:', error);
        // Handle the error or show an error message to the user
    }
  }


  function getFileExtension(filenameEx) {
    return filenameEx.split('.').pop();
}

  const fileInput = ref(null);
  function openFileSelector() {
    fileInput.value.click();
  }


  async function uploadFile(file) {
    try {
        const formData = new FormData();
        formData.append('file', file);

        console.log(`hello token: ${authToken.value}`)
        

        const response = await axios.post('http://127.0.0.1:8000/upload', formData, {
            headers: {
                'Content-Type': 'multipart/form-data',
                'token': authToken
            }
        });

        console.log('File uploaded successfully:', response.data.message);
        return response.data;
    } catch (error) {
        console.error('Error uploading file:', error);
        throw error;
    }
}


function logout() {
  store.commit('logout')
  router.push('/feed');
}






onMounted(() => {
  window.addEventListener('scroll', handleScroll);
  window.addEventListener('resize', handleResize);
});

onBeforeUnmount(() => {
  window.removeEventListener('scroll', handleScroll);
  window.removeEventListener('resize', handleResize);
});
   
  </script>
  
  <style scoped>
  .header {
    background-color: var(--titlebar-background);
    border-radius: 50px;
    width: 80vw;
    margin: 0 auto;
    transition: width 0.3s ease, margin 0.3s ease;
  }
  
  .login-button {
    outline: none;
  }
  
  .login-button, .signup-button {
    color: var(--text-color);
    font-weight: bold;
  }
  
  .signup-button {
    background-color: var(--sidebar-highlight);
  }
  
  .header-content {
    display: flex;
    gap: 10px;
  }
  
  .gradient-background {
    background: var(--background);
  }
  
  .toolbar-title {
    display: flex;
    align-items: center;
  }
  
  .title {
    font-size: 1.5rem;
    font-weight: bold;
    color: var(--text-color);
    margin-left: 10px;
  }
  
  .footer-content {
    display: flex;
    align-items: center;
    margin: 0 auto;
    justify-content: space-evenly;
    width: 100%;
  }

  .menu-item {
  text-decoration: none; /* Remove underline */
  color: black; /* Set color to black */
}

.menu-item:hover {
  background-color: #f0f0f0; /* Change background color on hover */
}

.menu-item-text {
  margin-left: 10px; /* Add margin for text */
}

.profile-picture-container {
  text-align: center;
  margin-bottom: 10px; /* Adjust spacing */
}

.profile-picture {
  width: 150px; /* Adjust size as needed */
  height: 150px; /* Adjust size as needed */
  border-radius: 50%;
}

.profile-section {
  flex: 1; /* Adjust flex value to take up less space */
  background-color: var(--drawer);
  color: var(--text);
  border-radius: 30px;
  padding: 20px;
  text-align: center;
  margin-top:50px;
  margin-right: 25px;
}
  
  </style>
  