<template>
  <div :class="{ darkMode: isDarkMode }" class="app">:
    <TitleBar></TitleBar>
    <SearchBar></SearchBar>
    <sidebar></sidebar>
    <router-view @toggle-changed="handleToggleChange" class="main-feed"/>
  </div>
</template>


<script setup lang="ts">
import { ref } from 'vue';
import Sidebar from './components/Sidebar.vue'
import TitleBar from './components/TitleBar.vue'
import SearchBar from './components/SearchBar.vue';


const isDarkMode = ref(false);
const handleToggleChange = () => {
  isDarkMode.value = !isDarkMode.value;
};

</script>


<style lang="scss">
:root {
  //--primary: #5aeac4;
  //--primary-alt: #229fc5;
  --post-icons: #000000;
  --sidebar-accent: #6dafad;
  --sidebar-icons: #1e293b;
  --sidebar-hover: #e8e8e8;
  --sidebar-highlight: #87dad8;
  //--dark-alt: #334155;
  --titlebar-background: #efefef;
  --titlebar-divider: #b0b0b0;
  --background: #f7f7f7;
  --title-text: #1e293b;
  --text: #333333;
  --sidebar-width: 200px;
  --text-bubble: #e9e9e9;
  --text-bubble-hover: #e0e0e0;
  --app-side-divider: #d7d7d7;
  --searchbar-background: #fff;
  --searchbar-border: #fff
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Fira sans', sans-serif;

}



button {
  cursor: pointer;
  appearance: none;
  border: none;
  outline: none;
  background: none;
}

html, body {
  height: 100%;
}


.app {
  display: flex;

  min-height: 100vh;
  background-color: var(--background); // Move this line here

  &.darkMode {
    //--primary: #1e1e1e;
    //--primary-alt: #1e1e1e;
    //--grey: #1e1e1e;;
    //--dark: #1e1e1e;;
    //--dark-alt: #1e1e1e;;
    --post-icons: #cccccc;
    --text: #eeeeee;
    --text-bubble: #424242;
    --text-bubble-hover: #2b2b2b;
    --sidebar-icons: #f1f1f1;
    --sidebar-hover: #565656;
    --title-text: #f1f1f1;
    --background: #222222;
    --titlebar-background: #313131;
    --titlebar-divider: #313131;
    --app-side-divider: #424242;
    --searchbar-background: #666666;
    --searchbar-placeholder: #bcbcbc;
    --searchbar-border: #222222;
  }

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
  margin-right: 300px; /* Add buffer margin to the right */
  position: relative;
  transition: margin-left 0.3s ease, padding 0.3s ease, font-size 0.3s ease;

  @media (max-width: 896px) {
    margin-left: 0; /* Remove margin on the left when the screen is narrow */
    margin-right: 0; /* Remove buffer margin on the right when the screen is narrow */
  }

  &::before,
  &::after {
    content: '';
    position: absolute;
    top: 0;
    bottom: 0;
    width: 1px; /* Adjust the thickness of the lines */
    height: 100%;
    background-color: var(--app-side-divider); /* Replace with your desired color */
    margin-left: 10px; /* Adjust the padding between the line and main feed */
    margin-right: 10px; /* Adjust the padding between the line and main feed */
    transform: translateZ(0); /* Ensure consistent rendering */

    @media (max-width: 896px) {
      width: 0; /* Remove the colored margins when the screen is narrow */
      margin-left: 0; /* Remove padding on the left when the screen is narrow */
      margin-right: 0; /* Remove padding on the right when the screen is narrow */
    }
  }

  &::before {
    left: 1px;
  }

  &::after {
    right: 1px;
  }
}

</style>

