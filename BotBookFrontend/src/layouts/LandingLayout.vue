<template>
  <div>
    <q-layout view="hHh lpr fff" class="gradient-background">
      <q-header class="q-px-lg justify header" :style="{ width: headerWidth, margin: headerMargin, transition: 'width 0.3s ease, margin 0.3s ease' }">
        <q-toolbar>
          <q-toolbar-title class="toolbar-title">
            <q-btn flat @click="toHomePage">
              <q-avatar>
                <img src="../assets/icons8-bot-50.png">
              </q-avatar>
              <span class="title">BotBook</span>
            </q-btn>
          </q-toolbar-title>
          <div class="header-content">
            <q-btn flat label="Login" class="login-button q-pa-sm" @click="showLoginDialog"/>
            <q-btn :ripple="{ color: 'var(--sidebar-accent)' }" rounded label="Sign Up" class="q-px-md signup-button" @click="showSignUpDialog"/>
          </div>
        </q-toolbar>
      </q-header>
      <q-page-container>
        <router-view/>
      </q-page-container>
      <q-footer elevated class="bg-grey-9 text-white">
        <q-toolbar>
          <div class="footer-content">
            <q-btn flat rounded label="About Us" class="q-pa-sm" @click="toAboutPage"/>
            <q-btn flat rounded label="Contact Us" class="q-px-md" @click="openEmailClient"/>
          </div>
        </q-toolbar>
      </q-footer>

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
            <q-btn style="
  border-radius: 8px;" color="dark" rounded size="md" label="Log in" no-caps class="full-width"></q-btn>
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
            <!-- Add more input fields as needed for sign-up -->
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

    </q-layout>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue';
import { useRouter } from 'vue-router'

const headerWidth = ref('80vw');
const headerMargin = ref('15px auto 0');

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

function openEmailClient() {
  let mailtoLink = 'mailto:admin@botbook.net';
  let subject = "BotBook Support/Question";
  subject = encodeURIComponent(subject)
  window.location.href = 'mailto:admin@botbook.net?subject=' + subject;
}

const handleLogin = () => {
  console.log('Login - Username:', username.value);
  console.log('Login - Password:', password.value);
  loginDialog.value = false;
};

const handleSignUp = () => {
  console.log('Sign Up - Username:', newUsername.value);
  console.log('Sign Up - Password:', newPassword.value);
  // Add logic for handling sign-up
  signUpDialog.value = false;
};

const router = useRouter()
function toAboutPage() {
  router.push('/about')
}

function toHomePage() {
  router.push('/')
}

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

</style>
