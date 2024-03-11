<template>
    <q-page>
      <q-container>
        <q-card>
          <q-card-section>
            <div class="text-h6">Create a Bot</div>
          </q-card-section>
  
          <q-card-section>
            <q-form @submit.prevent="createBot">
              <q-input
                v-model="formData.username"
                label="Bot Username"
                dense
                outlined
              />
  
              <div class="q-uploader-container">
                <input
                  type="file"
                  @change="handleFileUpload"
                  accept=".png"
                  style="display: none"
                  ref="fileInput"
                />
                <div class="q-uploader-circle" @click="openFileInput">
                  <q-icon v-if="formData.botPicture" :name="null" size="2em" color="white">
                    <img :src="formData.botPicture" alt="Bot Preview" class="q-uploader-preview" />
                  </q-icon>
                  <q-icon v-else name="add" size="2em" color="white" />
                </div>
                <div class="q-uploader-file-name">{{ formData.botPictureName }}</div>
              </div>
  
              <q-input
                v-model="formData.interestInput"
                label="Interests"
                dense
                outlined
                @keyup.enter="addInterest"
              />
              <q-btn icon="add" @click="addInterest" />
  
              <div v-for="(interest, index) in formData.interests" :key="index" class="q-mt-md">
                <q-input
                  v-model="interest.value"
                  label="Interest"
                  dense
                  outlined
                  class="q-mr-md"
                />
                <q-btn icon="remove_circle" @click="removeInterest(index)" />
              </div>
  
              <q-btn icon="add" @click="addEmotion" />
  
              <div v-for="(emotion, index) in formData.emotions" :key="index" class="q-mt-md">
                <q-input
                  v-model="emotion.value"
                  label="Emotion"
                  dense
                  outlined
                  class="q-mr-md"
                />
                <q-btn icon="remove_circle" @click="removeEmotion(index)" />
              </div>
  
              <q-btn
                type="submit"
                color="primary"
                label="Create Bot"
                class="q-mt-md"
                :loading="loading"
              />
            </q-form>
          </q-card-section>
        </q-card>
      </q-container>
    </q-page>
  </template>
  
  <style scoped>
  .q-uploader-container {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .q-uploader-circle {
    width: 80px; /* Adjust the size as needed */
    height: 80px; /* Adjust the size as needed */
    background-color: #42b983; /* Quasar primary color, change as needed */
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    margin-bottom: 8px;
  }
  
  .q-uploader-preview {
    width: 80px; /* Adjust the size as needed */
    height: 80px; /* Adjust the size as needed */
    border-radius: 50%;
  }
  
  .q-uploader-file-name {
    text-align: center;
    font-size: 14px;
    color: #42b983;
  }
  </style>
  
  <script>
  export default {
    data() {
      return {
        formData: {
          username: "",
          botPicture: null,
          botPictureName: "",
          interests: [{ value: "" }],
          interestInput: "",
          emotions: [{ value: "" }],
        },
        loading: false,
      };
    },
    methods: {
      createBot() {
        // Handle bot creation logic here
        // You can make an API request to the server or perform any other actions
        // Access the bot picture using this.formData.botPicture
  
        // Show loading indicator while processing
        this.loading = true;
  
        // Simulate bot creation success after 2 seconds (replace with actual logic)
        setTimeout(() => {
          // Reset loading indicator
          this.loading = false;
  
          // Optionally, you can redirect the user to another page
          // this.$router.push('/bots');
        }, 2000);
      },
      addEmotion() {
        // Add another emotion input box
        this.formData.emotions.push({ value: "" });
      },
      removeEmotion(index) {
        // Remove the emotion input box at the specified index
        this.formData.emotions.splice(index, 1);
      },
      openFileInput() {
        // Trigger the hidden file input
        this.$refs.fileInput.click();
      },
      handleFileUpload(event) {
        const file = event.target.files[0];
  
        if (file) {
          const reader = new FileReader();
          reader.onload = () => {
            this.formData.botPicture = reader.result;
          };
          reader.readAsDataURL(file);
  
          this.formData.botPictureName = file.name;
        }
      },
      addInterest() {
        // Add another interest input box
        this.formData.interests.push({ value: "" });
      },
      removeInterest(index) {
        // Remove the interest input box at the specified index
        this.formData.interests.splice(index, 1);
      },
    },
  };
  </script>
  