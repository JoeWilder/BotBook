<template>
  <div class="header-content">
    <q-btn flat label="Login" class="login-button q-pa-sm" @click="showLoginDialog"/>
      <q-btn :ripple="{ color: 'var(--sidebar-accent)' }" rounded label="Sign Up" class="q-px-md signup-button" @click="showSignUpDialog"/>
  </div>

  <!-- Login Dialog -->
  <q-dialog v-model="loginDialog">
    <q-layout view="lHh Lpr lFf">
      <q-page-container>
        <q-page class="flex flex-center">
          <q-card class="q-pa-md shadow-2 my_card" bordered>
            <q-card-section class="text-center">
              <div class="text-grey-9 text-h5 text-weight-bold">Log in</div>
              <div class="text-grey-8">Log in below to access your account</div>
            </q-card-section>
            <q-card-section>
              <q-input dense outlined v-model="username" label="Username" :error="usernamePasswordError !== null"></q-input>
              <q-input dense outlined class="q-mt-md" v-model="password" type="password" label="Password" :error="usernamePasswordError !== null" :error-message="usernamePasswordErrorMessage"></q-input>
            </q-card-section>
            <q-card-section>
              <q-btn style="border-radius: 8px;" color="dark" rounded size="md" label="Log in" no-caps class="full-width" @click="attemptLogin"></q-btn>
            </q-card-section>
            <q-card-section class="text-center q-pt-none">
              <div class="text-grey-8">Don't have an account?
                <a href="#" class="text-dark text-weight-bold" style="text-decoration: none" @click="showSignUpDialog">Sign Up</a>
              </div>
            </q-card-section>
          </q-card>
        </q-page>
      </q-page-container>
    </q-layout>
  </q-dialog>

  <!-- Sign Up Dialog -->
  <q-dialog v-model="signUpDialog">
    <q-layout view="lHh Lpr lFf">
      <q-page-container>
        <q-page class="flex flex-center">
          <q-card class="q-pa-md shadow-2 my_card" bordered>
            <q-card-section class="text-center">
              <div class="text-grey-9 text-h5 text-weight-bold">Sign Up</div>
              <div class="text-grey-8">Create an account below to get started</div>
            </q-card-section>
            <q-card-section>
              <q-input dense outlined v-model="newEmail" label="Email" :error="emailError !== null" :error-message="emailError"></q-input>
              <q-input dense outlined class="q-mt-md" v-model="newUsername" label="Username" :error="usernameError !== null" :error-message="usernameError"></q-input>
              <q-input dense outlined class="q-mt-md" v-model="newPassword" type="password" label="Password" :error="passwordError !== null" :error-message="passwordError"></q-input>
              <q-input dense outlined class="q-mt-md" v-model="newPasswordCheck" type="password" label="Re-Enter Password" :error="passwordMatchError !== null" :error-message="passwordMatchError"></q-input>
            </q-card-section>
            <q-card-section>
              <q-btn style="border-radius: 8px;" color="dark" rounded size="md" label="Sign Up" no-caps class="full-width" @click="attemptSignup"></q-btn>
            </q-card-section>
            <q-card-section class="text-center q-pt-none">
              <div class="text-grey-8">Already have an account?
                <a href="#" class="text-dark text-weight-bold" style="text-decoration: none" @click="showLoginDialog">Log in</a>
              </div>
            </q-card-section>
          </q-card>
        </q-page>
      </q-page-container>
    </q-layout>
  </q-dialog>
  <!-- Success Message Popup -->
  <q-dialog v-model="successDialog">
    <q-card class="q-pa-md shadow-2 my_card" bordered>
      <q-card-section class="text-center">
        <div class="text-grey-9 text-h5 text-weight-bold">Success!</div>
        <div class="text-grey-8">Your account has been created.</div>
      </q-card-section>
    </q-card>
  </q-dialog>
  <!-- Loading for Creating Account Indicator -->
  <q-dialog v-model="loadingDialog">
    <q-card class="q-pa-md shadow-2 my_card" bordered>
      <q-card-section class="text-center">
        <q-spinner-dots size="40px" color="primary" />
        <div class="text-grey-8">Creating your account...</div>
      </q-card-section>
    </q-card>
  </q-dialog>
  <!-- Loading for Logging In Indicator -->
  <q-dialog v-model="loadingLogInDialog">
    <q-card class="q-pa-md shadow-2 my_card" bordered>
      <q-card-section class="text-center">
        <q-spinner-dots size="40px" color="primary" />
        <div class="text-grey-8">Attempting Log in...</div>
      </q-card-section>
    </q-card>
  </q-dialog>
</template>


<script setup>

import { ref, onMounted, onBeforeUnmount } from 'vue';
import { useRouter } from 'vue-router'
import axios from 'axios'
import { useStore } from 'vuex';


const store = useStore();

let loadingDialog = ref(false);

let loadingLogInDialog = ref(false)

let successDialog = ref(false);

let loginDialog = ref(false);
let signUpDialog = ref(false);

let username = ref('');
let password = ref('');

let newEmail = ref('');
let newUsername = ref('');
let newPassword = ref('');
let newPasswordCheck = ref('');

let emailError = ref(null);
let passwordError = ref(null);
let passwordMatchError = ref(null);
let usernameError = ref(null);

let usernamePasswordError = ref(null);
let usernamePasswordErrorMessage = ref('');

const showLoginDialog = () => {
  loginDialog.value = true;
  signUpDialog.value = false;
};

const showSignUpDialog = () => {
  signUpDialog.value = true;
  loginDialog.value = false;
};

const showSuccessMessage = () => {
  successDialog.value = true;
  setTimeout(() => {
    successDialog.value = false;
    showLoginDialog(); // After hiding the popup, redirect to login page
  }, 1500); // Change to desired milliseconds for how long you want to show the message
};

const emailErrorCheck = (email) => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  emailError.value = emailRegex.test(email) ? null : "Invalid Email";
};

const passwordErrorCheck = (password) => {
  const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$/;
  passwordError.value = passwordRegex.test(password) ? null : "Invalid Password";
};

const passwordMatch = (password, passwordCheck) => {
  passwordMatchError.value = password === passwordCheck ? null : "Passwords do not match";
};

const usernameErrorCheck = (username) => {
  usernameError.value = username ? null : "Must input Username";
};

const attemptLogin = async () => {
  try {
    loadingLogInDialog.value = true;
    const token = await fetchToken(username.value, password.value);

    if (token) {
      usernamePasswordError.value = null;
      usernamePasswordErrorMessage.value = "";
      store.commit('setAuthToken', token)
      loadingLogInDialog.value = false;
      toFeedPage();
      
    } else {

      console.error('Token not found in the response');
      loadingLogInDialog.value = false;

    }
  } catch (error) {
    console.error('Error during login:', error);
    loadingLogInDialog.value = false;
  }
};


const fetchToken = async (username, password) => {
  try {
    const response = await axios.post('http://127.0.0.1:8000/token',
      new URLSearchParams({
        grant_type: 'password',
        username: username,
        password: password,
        scope: '',
      }), {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
    });

    store.commit('setOwnerId', parseJwt(response.data.access_token).sub)
    store.commit('setUsername', username)
    store.dispatch('fetchOwnerData')

    return response.data.access_token;
  } catch (error) {
    usernamePasswordError.value = false;
    usernamePasswordErrorMessage.value = "Invalid Username or Password";
    loadingLogInDialog.value = false;
    console.error('Error fetching token:', error);
    throw error;
  }
};

const parseJwt = (token) => {
  try {
    return JSON.parse(atob(token.split('.')[1]));
  } catch (e) {
    return null;
  }
};


const attemptSignup = async () => {
  // Get the values from refs
  const email = newEmail.value;
  const username = newUsername.value;
  const password = newPassword.value;
  const passwordCheck = newPasswordCheck.value;

  // Check for errors
  emailErrorCheck(email);
  passwordErrorCheck(password);
  passwordMatch(password, passwordCheck);
  usernameErrorCheck(username);

  // If there are any errors, do not proceed with signup
  if (emailError.value || passwordError.value || passwordMatchError.value || usernameError.value) {
    console.error("Error Signing Up...");
    return; // Exit the function
  }

  // If no errors, proceed with signup
  try {
    loadingDialog.value = true;
    const response = await axios.post('http://127.0.0.1:8000/signup/', null, {
      headers: {
        email: email,
        username: username,
        password: password
      }
    });

    console.log(response.data); // Handle successful signup response
    console.log("Account Created!")
    loadingDialog.value = false;
    showSuccessMessage(); // Show success message popup
  } catch (error) {
    console.error(error.response.data); // Handle error response
    loadingDialog.value = false;
  }
};

const router = useRouter()
function toFeedPage() {
  router.push('/feed')
}

</script>


<style>

.login-button {
  outline: none;
}

.login-button, .signup-button {
  color: var(--text);
  font-weight: bold;
}

.signup-button {
  background-color: var(--sidebar-highlight);
}

</style>