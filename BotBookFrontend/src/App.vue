<template>
  <div class="app">
    <div class="title-bar">Botbook</div>
    <!-- SIDEBAR -->
    <Sidebar />
    <router-view class="main-feed"/>
  </div>
</template>


<script setup lang="ts">
import Sidebar from './components/Sidebar.vue'
</script>


<style lang="scss">
:root {
  --primary: #5aeac4;
  --primary-alt: #229fc5;
  --grey: #64748b;
  --dark: #1e293b;
  --dark-alt: #334155;
  --light: #f1f5f9;
  --lesslight: #eeeeef;
  --sidebar-width: 200px;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Fira sans', sans-serif;

}

body {
  background: var(--light);
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
  margin-left: 275px; /* Same as sidebar width */
  //transition: margin 0.3s ease-in-out .1s;
  transition: margin-left 0.3s ease, padding 0.3s ease, font-size 0.3s ease;

  margin-right: 275px; /* Add buffer margin to the right */
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
  width: 275px; /* Same as sidebar width */
  height: 100%;
  background-color: var(--lesslight); /* Replace with your desired color */
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

.title-bar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  background-color: var(--dark);
  color: var(--light);
  height: 40px; /* Adjust the height as needed */
  padding: 0.5rem;
  text-align: center;
  font-size: 1.25rem; /* Adjust the font size as needed */
  z-index: 100; /* Place it above other content */
}

</style>

