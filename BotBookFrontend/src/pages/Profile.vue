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
          <q-space></q-space>
          <q-space></q-space>
          <q-space></q-space>
          <q-btn label="Change Password" color="red-3" @click="changePasswordDialog" class="info-value"/>
          <q-dialog v-model="passwordChangeDialog">
            <q-layout view="lHh Lpr lFf">
                <q-page-container>
                    <q-page class="flex flex-center">
                        <q-card class="q-pa-md shadow-2 my_card" bordered>
                            <q-card-section class="text-center">
                                <div class="text-grey-9 text-h5 text-weight-bold">Change Password</div>
                            </q-card-section>
                            <q-card-section>
                                <q-input dense outlined class="q-mt-md" v-model="oldPassword" type="password" label="Old Password"></q-input>
                                <q-input dense outlined class="q-mt-md" v-model="newPassword" type="password" label="New Password"></q-input>
                                <q-input dense outlined class="q-mt-md" v-model="newPasswordCheck" type="password" label="Re-Enter New Password"></q-input>
                            </q-card-section>
                            <q-card-section>
                                <q-btn style="border-radius: 8px;" color="dark" rounded size="md" label="Change Password" no-caps class="full-width" @click="attemptPasswordChange"></q-btn>
                            </q-card-section>
                        </q-card>
                    </q-page>
                </q-page-container>
            </q-layout>
        </q-dialog>
          <q-space></q-space>
        </div>
        
      </div>
      <h5>Settings</h5>
      <div class="info-container">
        <div class="info-item">
          <div class="info-label">Dark Mode</div>
          <div class="info-value">
            <q-toggle v-model="darkMode" label="Dark Mode" color="primary" @click="toggleDarkMode"/>
          </div>
        </div>
      </div>
      <h2>My Bots</h2>
      <q-separator color="gray" style="height: 4px"/>
      <div class="bot-list">
        <div class="bot-list-container" v-if="bots && bots.every(bot => bot.userId !== null)">
          <div v-for="(bot, index) in bots" :key="index" class="bot-list-row">
            <BotManagementCard :bot="bot" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, defineEmits } from 'vue';
import BotManagementCard from '../components/BotManagementCard.vue'
import { useStore } from 'vuex';
import axios from 'axios'

const store = useStore();
const userName = computed(() => store.getters.getUsername);
const userEmail = computed(() => store.getters.getEmail);

const darkMode = ref(false);
const passwordChangeDialog = ref(false);


const bots = computed(() => store.getters.getBots);

const oldPassword = ref("")
const newPassword = ref("")
const newPasswordCheck = ref("")

const toggleValue = ref(localStorage.getItem("darkMode") === "true");
const emit = defineEmits(['toggleDarkMode'])



const toggleDarkMode = () => {
  localStorage.setItem("darkMode", darkMode.value);
  window.dispatchEvent(new CustomEvent('dark-mode-update', {
  detail: {
    storage: localStorage.getItem('darkMode')
  }
}));
};




// Function to handle changing password
const changePasswordDialog = () => {
  passwordChangeDialog.value = true
};

const attemptPasswordChange = async () => {

  console.log("ATTEMPTING")
  
  if (newPassword.value != newPasswordCheck.value) {
    return;
  }

  console.log("CHANGE")

  try {
        const response = await axios.post('http://127.0.0.1:8000/verify-password', {
            owner_id: store.getters.getOwnerId,
            password: oldPassword.value,
            new_password: newPassword.value
        });
        console.log('Password changed successfully:', response.data.message);
        return response.data.message;
    } catch (error) {
        console.error('Error changing password:', error);
        throw error;
    }

}

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
