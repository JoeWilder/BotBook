<template>
    <div>
      <q-layout view="hHh LpR fff" class="gradient-background">
        
        
        <q-drawer show-if-above side="left" bordered dark>
          <Sidebar/>
        </q-drawer>

        <q-drawer show-if-above side="right" style="background-color: var(--background);">
          <!-- Profile section -->
          <div class="profile-section">
            <div class="profile-picture-container">
              <img :src="getProfilePictureURL(profilePictureUrl)" alt="Profile Picture" class="profile-picture" />
            </div>
            <h3>{{ userName }}</h3>
            <p>Member since: {{ joinDate }}</p>
          </div>
        </q-drawer>

        

        <div>
          <q-header class="q-px-lg justify header" :style="{ width: headerWidth, margin: headerMargin, transition: 'width 0.3s ease, margin 0.3s ease' }">
            <q-toolbar>
            <BotBookLogo></BotBookLogo>
            <div style="
                flex: 1 1 0%;
                display: flex;
                justify-content: center;
                "
            >
                
            </div>
            <div
                style="flex: 1 1 0%; text-align: right;"
            >

            <q-btn flat icon="menu">
              <q-menu
                transition-show="jump-down"
                transition-hide="jump-up"
              >
              <q-list style="min-width: 100px">
                <!-- Use router-link for navigation -->
                <router-link class="menu-item" to="/settings">
                  <q-item clickable>
                    <span class="material-icons settings-icon">settings</span>
                    <q-item-section class="menu-item-text">Settings</q-item-section>
                  </q-item>
                </router-link>
              </q-list>
              </q-menu>
            </q-btn>
                
            </div>
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
import { ref, onMounted, onBeforeUnmount } from 'vue';
import BotBookLogo from "../components/BotBookLogo.vue"
import Sidebar from '../components/Sidebar.vue'

const headerWidth = ref('80vw');
const headerMargin = ref('15px auto 0');

const profilePictureUrl = ref('joewilder.jpg');
const joinDate = ref('January 1, 2022');
const userName = ref('Joe Wilder');
const getProfilePictureURL = (filename) => {
  return new URL(`../assets/ProfilePictures/${filename}`, import.meta.url).href
};

const scrollPosition = ref(0);
let isAtTop = ref(true);
const scrolled = ref(false);

const handleScroll = () => {

  if (window.scrollY === 0) {
    console.log("top")
    headerWidth.value = '80vw';
    headerMargin.value = '15px auto 0';
    isAtTop.value = true;
  } else {
    console.log("not top")
    headerWidth.value = '80vw'
    headerMargin.value = '0px auto 0';
    isAtTop.value = false;
  }
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll);
});

onBeforeUnmount(() => {
  window.removeEventListener('scroll', handleScroll);
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
  background-color: var(--gradient-background);
  color: var(--text);
  border-radius: 30px;
  padding: 20px;
  text-align: center;
  margin-top:50px;
  margin-right: 25px;
}
  
  </style>
  