<template>
  <div>
    <q-layout view="hHh lpr fff" class="gradient-background">
      <q-header class="q-px-lg justify header" :style="{ width: headerWidth, margin: headerMargin, transition: 'width 0.3s ease, margin 0.3s ease' }">
        <q-toolbar>
          
          <q-toolbar-title class="toolbar-title">
            <q-avatar>
              <img src="../assets/icons8-bot-50.png">
            </q-avatar>
            
            <span class="title">BotBook</span>
          </q-toolbar-title>
          
          <div class="header-content">
            <q-btn flat label="Login" class="login-button q-pa-sm"/>
            <q-btn :ripple="{ color: 'var(--sidebar-accent)' }" rounded label="Sign Up" class="q-px-md signup-button"/>
          </div>
        </q-toolbar>
      </q-header>

      <q-page-container>
        <router-view/>
      </q-page-container>

      <q-footer elevated class="bg-grey-9 text-white">
        <q-toolbar>
          <div class="footer-content">
            <q-btn flat rounded label="About Us" class="q-pa-sm"/>
            <q-btn flat rounded label="Contact Us" class="q-px-md"/>
          </div>
        </q-toolbar>
      </q-footer>
    </q-layout>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue';

const scrollPosition = ref(0);
let isAtTop = ref(true);
const scrolled = ref(false);
const headerWidth = ref('80vw');
const headerMargin = ref('15px auto 0');

const handleScroll = () => {

  if (window.scrollY === 0) {
    headerWidth.value = '80vw';
    headerMargin.value = '15px auto 0';
    isAtTop.value = true;
  } else {
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
  transition: width 0.3s ease, margin 0.3s ease
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
  /*background: linear-gradient(to top, var(--background), var(--gradient-background));  Adjust colors as needed */
  background: var(--background)
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