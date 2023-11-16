<template>
  <div class="title-bar">
    <img src="../assets/icons8-bot-50.png" alt="BotBook" class="logo" />
    <div class="title">Botbook</div>
    <span class="material-icons menu-icon" @click="toggleMenu">more_horiz</span>
    <div v-if="isMenuOpen" class="square-menu">
      <router-link class="menu-option" to="/settings" style="text-decoration: none; color: inherit;">
        <span class="material-icons settings-icon">settings</span>
        <span class="menu-text">Settings</span>
      </router-link>
      <!-- Add more menu options as needed -->
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

const isMenuOpen = ref(false);

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value;
};

const closeMenuOnClickOutside = (event) => {
  if (isMenuOpen.value && !event.target.closest('.square-menu') && !event.target.closest('.material-icons')) {
    isMenuOpen.value = false;
  }
};

onMounted(() => {
  document.addEventListener('click', closeMenuOnClickOutside);
});

onUnmounted(() => {
  document.removeEventListener('click', closeMenuOnClickOutside);
});
</script>

<style lang="scss">
.title-bar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  background-color: var(--light);
  border-bottom: 1px solid var(--lesslight);
  color: var(--dark);
  display: flex;
  align-items: center;
  height: 40px;
  padding: 0.5rem 2rem;
  z-index: 100;

  .logo {
    margin-right: 0.5rem;
    max-height: 24px;
    z-index: 1;
    position: relative;
    top: -3px;
  }


  .title {
    flex: 1;
    text-align: left;
    font-size: 1.25rem;
    color: var(--dark);
  }

  .menu-icon {
    cursor: pointer;
    padding: 4px; // Adjust padding for space around the icon

    transition: background-color 0.3s ease, border-radius 0.3s ease; // Added transition for smoother effect

    &:hover {
      background-color: #e8e8e8;
      border-radius: 8px;
      border: 1px solid #ccc; // Added consistent border
    }
  }

  .square-menu {
    position: absolute;
    top: 40px;
    right: 30px;
    background-color: var(--light);
    border: 1px solid var(--lesslight);
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    padding: 0.5rem;
    z-index: 101; /* Place it above the title bar */
    width: 120px; /* Adjusted width for a square menu */
    border-radius: 8px; /* Added border-radius for a rounded appearance */
    display: flex;
    flex-direction: column;

    .menu-option {
      display: flex;
      align-items: center;

      .settings-icon {
        margin-right: 8px; // Adjust the margin between the icon and text
        cursor: auto; // Disable hover effect for the settings icon
        &:hover {
          background-color: transparent;
          border-radius: 0;
          border: none;
        }
      }
    }


  }
}
</style>
