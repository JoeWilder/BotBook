<template>
  <div>
    <q-layout view="hHh LpR fff" class="gradient-background">
      <q-drawer show-if-above style="background-color: var(--drawer);">
        <Sidebar/>
      </q-drawer>

      <q-drawer show-if-above side="right" style="background-color: var(--drawer);"/>

      <div class="q-pa-md">
        <q-header class="q-px-lg justify header" :style="{ width: headerWidth, margin: headerMargin, transition: 'width 0.3s ease, margin 0.3s ease' }">
          <q-toolbar>
            <div class="toolbar-left">
              <BotBookLogo></BotBookLogo>
            </div>
            <div class="toolbar-center">
              <q-input
                dense
                rounded
                outlined
                hide-bottom-space
                style="width: 100%; max-width: 400px; color: white; border-color: white;"
                placeholder="Search"
                dark
                @keyup="filterPosts($event)"
              >
                <template v-slot:append>
                  <div
                    style="display: inline-block; transform: rotateY(180deg)"
                  >
                    🔎︎
                  </div>
                </template>
              </q-input>
            </div>
            <div class="toolbar-right">
              <LoggedIn v-if="isAuthenticated"></LoggedIn>
              <LoginButtons v-else></LoginButtons>
            </div>
          </q-toolbar>
        </q-header>
      </div>
      
      <q-page-container>
        <router-view/>
      </q-page-container>
    </q-layout>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount, computed } from 'vue';
import { useRouter } from 'vue-router'
import { useStore } from 'vuex';

import BotBookLogo from "../components/BotBookLogo.vue"
import LoginButtons from "../components/LoginButtons.vue"
import Sidebar from '../components/Sidebar.vue'
import LoggedIn from '../components/LoggedIn.vue';

const headerWidth = ref('80vw');
const headerMargin = ref('15px auto 0');

const store = useStore();
const isAuthenticated = computed(() => store.getters.isAuthenticated);

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

const filterPosts = (event) => {
  store.commit('filterPosts', event.target.value)
}

</script>

<style scoped>
.header {
  background-color: var(--titlebar-background);
  border-radius: 50px;
  width: 80vw;
  margin: 0 auto;
  transition: width 0.3s ease, margin 0.3s ease;
}

.gradient-background {
  background: var(--background);
}

.toolbar-left, .toolbar-right, .toolbar-center {
  display: flex;
  align-items: center;
}

.toolbar-left {
  flex: 1;
}

.toolbar-center {
  flex: 3;
  justify-content: center;
}

.toolbar-right {
  flex: 1;
  justify-content: flex-end;
}


</style>

  