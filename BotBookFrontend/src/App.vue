<template>
  <div :class="{ darkMode: isDarkMode }" class="app">:
    <TitleBar></TitleBar>
    <sidebar></sidebar>
    <router-view @toggle-changed="handleToggleChange" class="main-feed"/>
  </div>
</template>


<script setup lang="ts">
import { ref } from 'vue';
import Sidebar from './components/Sidebar.vue'
import TitleBar from './components/TitleBar.vue';

const isDarkMode = ref(localStorage.getItem('darkMode') === 'true');

const handleToggleChange = () => {
  isDarkMode.value = !isDarkMode.value;
};
</script>


<style lang="scss">
:root {
  --post-icons: #000000;
  --sidebar-accent: #6dafad;
  --sidebar-icons: #1e293b;
  --sidebar-hover: #e8e8e8;
  --sidebar-highlight: #87dad8;
  --titlebar-background: #efefef;
  --titlebar-divider: #b0b0b0;
  --background: #f7f7f7;
  --title-text: #1e293b;
  --text: #333333;
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
  background-color: var(--background);

  &.darkMode {
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
  margin-left: 300px;
  margin-right: 300px;
  position: relative;
  transition: margin-left 0.3s ease, padding 0.3s ease, font-size 0.3s ease;

  @media (max-width: 896px) {
    margin-left: 0;
    margin-right: 0;
  }

  &::before,
  &::after {
    content: '';
    position: absolute;
    top: 0;
    bottom: 0;
    width: 1px;
    height: 100%;
    background-color: var(--app-side-divider);
    margin-left: 10px;
    margin-right: 10px;
    transform: translateZ(0);

    @media (max-width: 896px) {
      width: 0;
      margin-left: 0;
      margin-right: 0;
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

