<template>
  <main class="settings-page">
    <h1>Settings</h1>
    <p>Theme</p>
    <label class="switch">
      <input type="checkbox" v-model="toggleValue" @change="toggleDarkMode" />
      <span class="slider"></span>
    </label>
  </main>
</template>

<script setup>
import {ref, defineEmits} from "vue";

const toggleValue = ref(localStorage.getItem("darkMode") === "true");
const emit = defineEmits(['toggleDarkMode'])

const toggleDarkMode = () => {
  localStorage.setItem("darkMode", toggleValue.value);
  emit('toggle-changed', toggleValue.value);
};


</script>

<style lang="scss" scoped>
.settings-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  text-align: center;
  padding: 20px;

  h1 {
    font-size: 2rem;
    margin-bottom: 10px;
    color: var(--title-text);
  }

  .switch {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
  }

  .switch input {
    opacity: 0;
    width: 0;
    height: 0;
  }

  .slider {
    position: relative;
    cursor: pointer;
    width: 60px;
    height: 34px;
    background-color: #ccc;
    transition: 0.4s;
    border-radius: 34px;
  }

  .slider:before {
    content: '';
    position: absolute;
    height: 26px;
    width: 26px;
    left: 4px;
    top: 4px;
    background-color: white;
    transition: 0.4s;
    border-radius: 50%;
  }

  input:checked + .slider {
    background-color: var(--sidebar-highlight);
  }

  input:checked + .slider:before {
    transform: translateX(26px);
  }

  p {
    font-size: 1rem;
    color: var(--text);
  }
}
</style>
