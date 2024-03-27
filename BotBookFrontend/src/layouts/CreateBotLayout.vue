<template>
    <div>
      <q-layout view="hHh LpR fff" class="gradient-background">
        
        <q-drawer show-if-above style="background-color: var(--drawer);">
          <Sidebar/>
        </q-drawer>

      <q-drawer show-if-above side="right" bordered style="background-color: var(--drawer);"/>


        <div class="q-pa-md">
            <q-header class="q-px-lg justify header" :style="{ width: headerWidth, margin: headerMargin, transition: 'width 0.3s ease, margin 0.3s ease' }">
            <q-toolbar>
            <BotBookLogo></BotBookLogo>
            <div style="
                flex: 1 1 0%;
                display: flex;
                justify-content: center;
                "
            >
            </div>
            <div
                style="
                flex: 1 1 0%;
                text-align: right;
                overflow: auto;
                "
            >

            <q-btn flat icon="menu">
              <q-menu
                transition-show="jump-down"
                transition-hide="jump-up"
              >
              <q-list style="min-width: 100px">
                <!-- Use router-link for navigation -->
                <router-link class="menu-item" to="/settings">
                  <q-item clickable>
                    <span class="material-icons settings-icon">settings</span>
                    <q-item-section class="menu-item-text">Settings</q-item-section>
                  </q-item>
                </router-link>
              </q-list>
              </q-menu>
            </q-btn>
                
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
  import { ref, onMounted, onBeforeUnmount } from 'vue';
  import { useRouter } from 'vue-router'
  import { useStore } from 'vuex';

  import BotBookLogo from "../components/BotBookLogo.vue"
  import LoginButtons from "../components/LoginButtons.vue"
  import Sidebar from '../components/Sidebar.vue'
  
  const headerWidth = ref('80vw');
  const headerMargin = ref('15px auto 0');
  
  let loginDialog = ref(false);
  let signUpDialog = ref(false);
  
  let username = ref('');
  let password = ref('');
  
  let newUsername = ref('');
  let newPassword = ref('');

  const store = useStore();
  
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

  .menu-item {
  text-decoration: none; /* Remove underline */
  color: black; /* Set color to black */
}

.menu-item:hover {
  background-color: #f0f0f0; /* Change background color on hover */
}

.menu-item-text {
  margin-left: 10px; /* Add margin for text */
}
  
  </style>
  