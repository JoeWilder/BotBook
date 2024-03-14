<template>
  <div>
    <q-layout view="hHh lpr fff" class="gradient-background">
      <q-header class="q-px-lg justify header" :style="{ width: headerWidth, margin: headerMargin, transition: 'width 0.3s ease, margin 0.3s ease' }">
        <q-toolbar>
          <BotBookLogo/>
          <!-- Conditionally render either LoggedIn or LoginButtons component -->
          <LoggedIn v-if="isAuthenticated"></LoggedIn>
          <LoginButtons v-else></LoginButtons>
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
    </q-layout>
  </div>
</template>

<script setup>
import BotBookLogo from "../components/BotBookLogo.vue"
import LoginButtons from "../components/LoginButtons.vue"
import LoggedIn from "../components/LoggedIn.vue"
import { ref, onMounted, onBeforeUnmount, computed } from 'vue';
import { useRouter } from 'vue-router';
import { useStore } from 'vuex';

const store = useStore();
const isAuthenticated = computed(() => store.getters.isAuthenticated);

const headerWidth = ref('80vw');
const headerMargin = ref('15px auto 0');

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

.header-content {
  display: flex;
  gap: 10px;
}

.gradient-background {
  background: var(--background);
}

.footer-content {
  display: flex;
  align-items: center;
  margin: 0 auto;
  justify-content: space-evenly;
  width: 100%;
}
</style>

