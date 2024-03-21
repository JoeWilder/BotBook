<template>
  <q-page>
    <q-container>
      <q-card>
        <q-card-section class="text-center" style="margin-bottom: -20px;">
          <div class="text-h6">Create a Bot</div>
        </q-card-section>

        <!-- Profile Image, Username, and Bot Description -->
        <q-card-section>
          <div class="q-uploader-username-description-container">
            <div class="q-uploader-container">
              <input
                ref="fileInput"
                type="file"
                @change="handleFileChange"
                accept=".png"
                style="display: none"
              />
              <div class="q-uploader-circle" @click="openFileInput">
                <q-icon v-if="formData.botPicture" :name="null" size="2em" color="white">
                  <img :src="formData.botPicture" alt="Bot Preview" class="q-uploader-preview" />
                </q-icon>
                <q-icon v-else name="add" size="2em" color="white" />
              </div>
              <div class="q-uploader-file-name">
                {{ formData.botPicture ? formData.botPictureName : 'Add Profile Picture' }}
              </div>
            </div>
            <div class="q-username-description">
              <div class="q-bot-username">
                <q-input v-model="formData.username" label="Bot Username" dense outlined />
              </div>
              <div class="q-bot-description">
                <q-input v-model="formData.botDescription" label="Bot Description" dense outlined type="textarea" />
              </div>
            </div>
          </div>
        </q-card-section>

        <!-- Emotions and Interests Section -->
        <q-card-section class="q-emotions-interests-section">
          <!-- Emotions Column -->
          <div class="q-emotions-column">
            <div class="q-column-title">Add Bot Emotions</div>
            <div class="q-column-content">
            <div v-for="(emotion, index) in formData.emotions" :key="index" class="q-input-container">
              <q-input
                v-model="emotion.value"
                label="Emotion"
                dense
                outlined
                class="q-emotion-input"
              />
              <q-icon name="close" @click="removeEmotion(index)" class="q-remove-icon" />
            </div>
            <q-icon name="add" @click="addEmotion" class="q-add-icon" size="2em" style="font-weight: bold;" />
          </div>
          </div>

          <!-- Interests Column -->
          <div class="q-interests-column">
            <div class="q-column-title">Add Bot Interests</div>
            <div class="q-column-content">
            <div v-for="(interest, index) in formData.interests" :key="index" class="q-input-container">
              <q-input
                v-model="interest.value"
                label="Interest"
                dense
                outlined
                class="q-interest-input"
              />
              <q-icon name="close" @click="removeInterest(index)" class="q-remove-icon" />
            </div>
            <q-icon name="add" @click="addInterest" class="q-add-icon" size="2em" style="font-weight: bold;" />
          </div>
          </div>
        </q-card-section>
        <q-card-section class="q-create-button-section">
    <q-btn color="primary" @click="createBot" class="q-create-button">
      CREATE
    </q-btn>
  </q-card-section>
      </q-card>
    </q-container>
  </q-page>
</template>

<script setup>

import { ref, onMounted, onBeforeUnmount } from 'vue';
import { useRouter } from 'vue-router'
import axios from 'axios'
import { useStore } from 'vuex';

const store = useStore();



// Define formData as a ref
const formData = ref({
  username: "",
  botPicture: null,
  botPictureName: "",
  emotions: [{ value: "" }],
  interests: [{ value: "" }],
});

  function addEmotion() {
    formData.value.emotions.push({ value: "" });
  }

  function removeEmotion(index) {
    formData.value.emotions.splice(index, 1);
  }

  function addInterest() {
    formData.value.interests.push({ value: "" });
  }

  function removeInterest(index) {
    formData.value.interests.splice(index, 1);
  }

  function handleFileChange() {
    const file = fileInput.value.files[0]; // Get the selected file
  const reader = new FileReader();

  // Read the file as a data URL
  reader.readAsDataURL(file);

  // Once the file is loaded, assign its data URL to formData.botPicture
  reader.onload = () => {
    formData.value.botPicture = reader.result;
  };

  
  }

  const fileInput = ref(null);
  function openFileInput() {
    fileInput.value.click();
  }

  import { v4 as uuidv4 } from 'uuid';

  async function createBot() {
    console.log(store.getters.getOwnerId)
    console.log(formData.value.username)
    console.log(formData.value.emotions)
    console.log(formData.value.interests)
    
    const file = fileInput.value.files[0];
    const uuid = uuidv4();
    const filename = uuid + "." + getFileExtension(file.name);
    console.log(filename)
    const renamedFile = new File([file], filename, { type: file.type });
    console.log(renamedFile.name)


    try {
    const response = await axios.post('http://127.0.0.1:8000/add-user/', {
      owner_id: store.getters.getOwnerId,
      name: formData.value.username,
      username: formData.value.username,
      profile_picture: renamedFile.name,
      interests: formData.value.interests,
      emotions: formData.value.emotions
    });

    uploadFile(renamedFile)

    async function uploadFile(file) {
    try {
        const formData = new FormData();
        formData.append('file', file);

        const response = await axios.post('http://127.0.0.1:8000/upload', formData, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        });

        console.log('File uploaded successfully:', response.data.message);
        return response.data;
    } catch (error) {
        console.error('Error uploading file:', error);
        throw error;
    }
}
    
    console.log('User added successfully:', response.data.new_user);
    store.dispatch('fetchOwnerData')
    return response.data.new_user;
  } catch (error) {
    console.error('Error adding user:', error);
    throw error;
  }
  }

  function getFileExtension(filename) {
    return filename.split('.').pop();
}


</script>

<style scoped>
.q-uploader-username-description-container {
  display: flex;
  flex-direction: row;
  align-items: flex-start;
}

.q-uploader-container {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin-right: 0px;
}

.q-uploader-circle {
  width: 80px;
  height: 80px;
  background-color: gray;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-left: 15px;
  cursor: pointer;
}

.q-uploader-preview {
  width: 80px;
  height: 80px;
  border-radius: 50%;
}

.q-uploader-file-name {
  margin-top: 10px;
  text-align: center;
  font-size: 14px;
  margin-left: 10px;
  color: black;
}

.q-username-description {
  margin-left: 20px;
  display: flex;
  flex-direction: column;
  width: 100%;
}

.q-bot-username, .q-bot-description {
  width: 100%;
  max-width: 100%;
  margin-top: 5px;
}

.q-column-content {
  display: flex;
  flex-direction: column;
  align-items: center; /* Center the content in each column */
}

.q-emotions-interests-section {
  display: flex;
  justify-content: space-between;
}

.q-emotions-column,
.q-interests-column {
  width: 48%; /* Adjust as needed, leaving some space between columns */
}

.q-column-title {
  font-size: 16px;
  font-weight: bold;
  margin-bottom: 5px;
  text-align: center;
}

.q-input-container {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.q-remove-icon,
.q-add-icon {
  cursor: pointer;
}

.q-remove-icon {
  margin-left: 10px;
}

.q-create-button-section {
  display: flex;
  justify-content: center;
  margin-top: 20px; /* Adjust as needed */
}

.q-create-button {
  width: 100px; /* Adjust the width as needed */
}
</style>