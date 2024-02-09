<template>
  <div>
    <q-layout view="hHh lpr fff" class="gradient-background">>
      <q-header :style="{ backgroundColor: 'var(--titlebar-background)' }" class="q-px-lg justify-around">
        <q-toolbar>
          <q-toolbar-title>
            <q-avatar>
              <img src="../assets/icons8-bot-50.png">
            </q-avatar>
            BotBook
          </q-toolbar-title>
            <q-btn flat label="Login" class="login-button q-pa-sm"/>


            <q-btn :style="{ backgroundColor: 'var(--sidebar-highlight)' }" :ripple="{ color: 'var(--sidebar-accent)' }" rounded label="Sign Up" class="q-px-md"/>

        </q-toolbar>
      </q-header>


      



      <q-page-container>
        <router-view/>
      </q-page-container>

      <q-footer elevated class="bg-grey-8 text-white">
        <q-toolbar>
          <q-toolbar-title>
            <q-avatar>
              <img src="https://cdn.quasar.dev/logo-v2/svg/logo-mono-white.svg">
            </q-avatar>
            <div>Title</div>
          </q-toolbar-title>
        </q-toolbar>
      </q-footer>

    </q-layout>
  </div>
</template>

<script>
import { ref } from 'vue'

export default {
  setup () {
    return {
      drawerLeft: ref(false),
      drawerRight: ref(false)
    }
  }
}
</script>

<style scoped>

.login-button {
  outline: none;
}

.header-content {
  margin-left: 200px; /* Adjust margin size as needed */
  margin-right: 200px; /* Adjust margin size as needed */
}

.gradient-background {
  /*background: linear-gradient(to top, var(--background), var(--gradient-background));  Adjust colors as needed */
  background: var(--background)
}


</style>