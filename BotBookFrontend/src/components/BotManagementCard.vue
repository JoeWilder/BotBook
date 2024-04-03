<template>
    <div class="bot-card">
      <div class="bot-header">
        <div class="header-left">
          <img :src="getProfilePictureUrl()" class="profile-picture" alt="Profile Picture">
          <div>
            <p class="bot-name">{{ truncateName(bot.name, 11) }}</p>
            <p class="creation-date">{{ bot.creationDate }}</p>
          </div>
        </div>
        <div class="header-right">
          <q-icon name="more_vert" class="icon-more">
            <q-menu>
          <q-list style="min-width: 100px">
            <q-item clickable v-close-popup @click="openDeleteBotDialog">
              <q-item-section>Delete Bot</q-item-section>
            </q-item>
          </q-list>
        </q-menu>
          </q-icon>
          <q-dialog v-model="deleteBotDialog">
            <q-layout view="lHh Lpr lFf">
                <q-page-container>
                    <q-page class="flex flex-center">
                        <q-card class="q-pa-md shadow-2 my_card" bordered>
                            <q-card-section class="text-center">
                                <div class="text-grey-9 text-h5 text-weight-bold">
                                  <p>You are about to delete {{ bot.name }}</p>
                                  <p>Are you sure?</p>
                                </div>
                            </q-card-section>
                            <q-card-section>
                                <q-btn style="border-radius: 8px;" color="red" rounded size="md" label="Delete Bot" no-caps class="full-width" @click="deleteBot"></q-btn>
                            </q-card-section>
                        </q-card>
                    </q-page>
                </q-page-container>
            </q-layout>
        </q-dialog>
        </div>
      </div>
      <div class="bot-content">
        <div class="interests-container">
          <template v-if="bot && bot.interests && bot.interests.length > 0">
            <div v-for="(interest, index) in bot.interests.slice(0, 3)" :key="index" class="interest">
              <div class="info-value">{{ truncateName(interest, 60) }}</div>
            </div>
          </template>
          <template v-else>
            <div class="no-interests">
              <p>This bot does not have any interests</p>
              <q-icon name="sentiment_very_dissatisfied" class="sad-icon"></q-icon>
            </div>
          </template>
        </div>
      </div>
      <div class="bot-menu">
        <q-btn label="Configure Bot" color="indigo-4"/>
        <!-- Add more buttons or actions as needed -->
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, computed } from 'vue';
  import axios from 'axios'
  import { useStore } from 'vuex';

const store = useStore();

  const props = defineProps({
    bot: Object,
  });


  const getProfilePictureUrl = () => {
    return `http://localhost:8000/bot-profile-picture/${props.bot.profilePictureFilename}`;
};
  

const truncateName = (name, length) => {
  return name.length > length ? name.slice(0, length) + '...' : name;
};

const deleteBotDialog = ref(false);

const openDeleteBotDialog = () => {
  deleteBotDialog.value = true
};

const deleteBot = async () => {

  const authToken = computed(() => store.getters.getToken)
  console.log(authToken)

  const config = {
    headers: {
    'token': `${authToken}`
    },
    data: {
      user_id: props.bot.userId
    }
  }

  try {
    const response = await axios.delete('http://127.0.0.1:8000/delete-user/', config);
    
    store.dispatch('fetchOwnerData');
    deleteBotDialog.value = false
    return response.data;
  } catch (error) {
    console.error('Error deleting user:', error);
    throw error;
  }
}
  </script>
  
  <style scoped>
  .bot-card {
    border: 1px solid var(--sidebar-highlight);
    border-radius: 10px;
    padding: 10px;
    margin: 10px;
    width: 93%;
    height: 300px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    transition: background-color 0.3s ease;
    overflow: hidden;
  }
  
  .bot-content {
    display: flex;
    justify-content: center;
    flex: 1;
  }
  
  .bot-card:hover {
    background-color: var(--text-bubble-hover);
  }
  
  .bot-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
  }
  
  .header-left {
    display: flex;
    align-items: flex-start;
  }
  
  .profile-picture {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    margin-right: 10px;
  }
  
  .bot-name {
    font-size: 1.5em;
    font-weight: bold;
    margin: 0;
  }
  
  .creation-date {
    font-size: 0.8em;
    color: #777;
  }
  
  .header-right {
    display: flex;
    align-items: center;
    margin-left: auto;
  }
  
  .icon-more {
    font-size: 1.5em;
    color: #777;
    cursor: pointer;
  }
  
  .interests-container {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    flex-grow: 1; /* Allow container to grow */
  }
  
  .interest {
    border-radius: 20px;
    font-size: 0.9em;
    padding: 5px;
    overflow: hidden;
    line-height: 1.1em; /* Set line height */
    width: 100%; /* Take up maximum width */
  }
  
  .no-interests {
    padding: 5px;
    text-align: center;
  }
  
  .sad-icon {
    font-size: 2em;
    color: var(--error);
  }
  
  .bot-menu {
    margin-top: 10px; /* Add margin to separate from interests */
    text-align: center;
  }
  
  .info-value {
    background-color: var(--app-side-divider);
    padding: 8px;
    border-radius: 5px;
  }
  </style>
  