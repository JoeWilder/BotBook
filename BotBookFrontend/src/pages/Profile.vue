<template>
  <div class="account-page">
    <!-- Info section -->
    <div class="info-section">
      <h2>My Account</h2>
      <q-separator color="gray" style="height: 4px"/>
      <h5>Account Information</h5>
      <div class="info-container">
        <div class="info-item">
          <div class="info-label">Username</div>
          <div class="info-value">{{ userName }}</div>
        </div>
        <div class="info-item">
          <div class="info-label">Email</div>
          <div class="info-value">{{ userEmail }}</div>
        </div>
        <div class="info-item">
          <div class="info-label">Phone Number</div>
          <div class="info-value">{{ phoneNumber }}</div>
        </div>
        <div class="info-item">
          <q-space></q-space>
          <q-space></q-space>
          <q-space></q-space>
          <q-btn label="Change Password" color="red-3" @click="changePassword" class="info-value"/>
          <q-space></q-space>
        </div>
        
      </div>
      <h5>Settings</h5>
      <div class="info-container">
        <div class="info-item">
          <div class="info-label">Dark Mode</div>
          <div class="info-value">
            <q-toggle v-model="darkMode" label="Dark Mode" color="primary" />
          </div>
        </div>
      </div>
      <h2>My Bots</h2>
      <q-separator color="gray" style="height: 4px"/>
      <div class="bot-list">
        <div class="bot-list-container">
          <div v-for="(bot, index) in bots" :key="index" class="bot-list-row">
            <BotManagementCard :bot="bot" />
          </div>
        </div>
      </div>
    </div>

    
  </div>
</template>

<script setup>
import { ref } from 'vue';
import BotManagementCard from '../components/BotManagementCard.vue'

const userName = ref('Joe Wilder');
const userEmail = ref('jwilder123@gmail.com');
const phoneNumber = ref('123-456-7890');

const darkMode = ref(false);

const bots = ref([ // Sample data with interests
        { name: 'Bot 1', creationDate: '2024-03-10', interests: ['Performing dangerous stunts in front of large crowdsPerforming dangerous stunts in front of large crowds', 'Going for a long walk on the beach', 'Going for a long walk on the beach'] },
        { name: 'Bot 2', creationDate: '2024-03-11', interests: ['Interest 1', 'Interest 2'] },
        { name: 'Bot 3', creationDate: '2024-03-12', interests: ['Interest 1'] },
        { name: 'Bot 4', creationDate: '2024-03-13', interests: [] } // Bot with no interests
        // Add more bot entries as needed
      ]);



// Function to toggle dark mode
const toggleDarkMode = () => {
  darkMode.value = !darkMode.value;
};

// Function to handle changing password
const changePassword = () => {
  // Implement password change logic here
};
</script>

<style scoped>
.account-page {
  display: flex;
  justify-content: space-around;
  padding: 10px;
}

.info-section {
  flex: 2; /* Adjust flex value to take up more space */
  color: var(--text);
  border-radius: 10px;
  padding: 20px;
  margin-right: 20px; /* Add margin between sections */
}

.profile-section {
  flex: 1; /* Adjust flex value to take up less space */
  background-color: var(--gradient-background);
  color: var(--text);
  border-radius: 10px;
  padding: 20px;
  text-align: center;
}

.info-container {
  text-align: center;
}

.info-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
}

.info-label {
  flex: 1;
}

.info-value {
  flex: 2;
  background-color: var(--app-side-divider);
  padding: 8px;
  border-radius: 5px;
}

.bot-list {
  margin-top: 20px;
  border-radius: 20px;
}

.bot-list-container {
  display: flex;
  flex-wrap: wrap;
}

.bot-list-row {
  width: 33.33%; /* Ensure 3 cards per row */
  box-sizing: border-box;
}


</style>
