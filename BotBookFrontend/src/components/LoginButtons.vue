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
                        <q-input dense outlined v-model="username" label="Username"></q-input>
                        <q-input dense outlined class="q-mt-md" v-model="password" type="password" label="Password"></q-input>
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
                            <q-input dense outlined v-model="newEmail" label="Email"></q-input>
                            <q-input dense outlined class="q-mt-md" v-model="newUsername" label="Username"></q-input>
                            <q-input dense outlined class="q-mt-md" v-model="newPassword" type="password" label="Password"></q-input>
                            <q-input dense outlined class="q-mt-md" v-model="newPasswordCheck" type="password" label="Re-Enter Password"></q-input>
                        </q-card-section>
                        <q-card-section>
                            <q-btn style="border-radius: 8px;" color="dark" rounded size="md" label="Sign Up" no-caps class="full-width"></q-btn>
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




</template>


<script setup>

import { ref, onMounted, onBeforeUnmount } from 'vue';
import { useRouter } from 'vue-router'
import axios from 'axios'

let loginDialog = ref(false);
let signUpDialog = ref(false);

let username = ref('');
let password = ref('');

let newUsername = ref('');
let newPassword = ref('');

const showLoginDialog = () => {
  loginDialog.value = true;
  signUpDialog.value = false;
};

const showSignUpDialog = () => {
  signUpDialog.value = true;
  loginDialog.value = false;
};

const attemptLogin = () => {
    console.log('Attempting login with username:', username.value, 'and password:', password.value);
    fetchToken(username.value, password.value);
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
 
    const token = response.data.access_token;
   
    console.log('Token:', token);
  } catch (error) {
    console.error('Error fetching token:', error);
    throw error;
  }
};

</script>


<style>

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

</style>