<template>
  <div class="app">
    <TitleBar></TitleBar>
    <sidebar></sidebar>
    <router-view class="main-feed"/>
  </div>
</template>


<script setup lang="ts">
import Sidebar from './components/Sidebar.vue'
import TitleBar from './components/TitleBar.vue'
</script>


<style lang="scss">
:root {
  --primary: #5aeac4;
  --primary-alt: #229fc5;
  --grey: #c5c5c5;
  --dark: #1e293b;
  --dark-alt: #334155;
  --light: #ffffff;
  --lesslight: #f5f5f5;
  --sidebar-width: 200px;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Fira sans', sans-serif;

}

body {
  background: #f7f7f7;
}

button {
  cursor: pointer;
  appearance: none;
  border: none;
  outline: none;
  background: none;
}

.app {
  display: flex;

  main {
    flex: 1 1 0;
    padding: 2rem;

    @media (max-width: 896px) {
      padding-left: 6rem;
    }
  }
}

.main-feed {
  margin-top: 40px;
  z-index: 1;
  margin-left: 300px; /* Same as sidebar width */
  //transition: margin 0.3s ease-in-out .1s;
  transition: margin-left 0.3s ease, padding 0.3s ease, font-size 0.3s ease;

  margin-right: 300px; /* Add buffer margin to the right */
  @media (max-width: 896px) {
    margin-left: 0; /* Remove margin on the left when screen is narrow */
  }
}

.main-feed::before,
.main-feed::after {
  transition: margin-left 0.3s ease, padding 0.3s ease, font-size 0.3s ease;
  content: '';
  position: fixed;
  top: 0;
  right: 0;
  width: 300px; /* Same as sidebar width */
  height: 100%;
  background-color: #f7f7f7; /* Replace with your desired color */
  z-index: -1; /* Place it behind the .main-feed content */

  @media (max-width: 896px) {
    width: 0; /* Remove the colored margins when screen is narrow */
  }
}

.main-feed::before {
  left: 0;
}

.main-feed::after {
  right: 0;
}

</style>

