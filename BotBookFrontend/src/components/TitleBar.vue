<template>
  <div class="title-bar">
    <img src="../assets/icons8-bot-50.png" alt="BotBook" class="logo" />
    <div class="title">BotBook</div>
    <span class="material-icons menu-icon" @click="toggleMenu">more_horiz</span>
    <div v-if="isMenuOpen" class="square-menu">
      <router-link @click.native="isMenuOpen = false" class="menu-option" to="/settings" style="text-decoration: none; color: inherit;">
        <span class="material-icons settings-icon">settings</span>
        <span class="menu-text">Settings</span>
      </router-link>
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
  background-color: var(--titlebar-background);
  border-bottom: 1px solid var(--titlebar-divider);
  color: var(--sidebar-icons);
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 60px;
  padding: 0 2rem; // Instead of padding: 0.5rem 2rem;
  z-index: 5;
}

.logo {
  margin-right: 1rem;
  max-height: 24px;
  z-index: 1;
  position: relative;
  top: -3px;
}

.title {
  font-size: 1.25rem;
  color: var(--title-text);
  margin-right: auto;
}

.menu-icon {
  color: var(--title-text);
  margin-left: 1rem;
  cursor: pointer;
  padding: 4px;
  transition: background-color 0.3s ease, border-radius 0.3s ease;

  &:hover {
    background-color: #e8e8e8;
    border-radius: 8px;
    border: 1px solid #ccc;
  }
}

.square-menu {
  position: absolute;
  top: 60px;
  right: 30px;
  background-color: var(--titlebar-background);
  border: 1px solid var(--titlebar-divider);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 0.5rem;
  z-index: 101;
  width: 120px;
  border-radius: 8px;
  display: flex;
  flex-direction: column;
}

.square-menu {
  flex: 1;
  margin: 10px 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.square-menu .menu-option {
  display: flex;
  align-items: center;
}

.square-menu .settings-icon {
  margin-right: 8px;
  cursor: pointer;

  &:hover {
    background-color: transparent;
    border-radius: 0;
    border: none;
  }
}
</style>
