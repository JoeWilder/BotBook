<template>
  <aside>
    <div class="fixed-icons">
    <div class="menu">
      <router-link class="button" to="/">
        <span class="material-icons">home</span>
        <span class="text">Home</span>
      </router-link>
      <router-link class="button" to="/about">
        <span class="material-icons">description</span>
        <span class="text">About</span>
      </router-link>
    </div>
    </div>
    <div class="flex"></div>
  </aside>
</template>


<style scoped>
aside {
  position: fixed;
  top: 20px;
  left: 0;
  display: flex;
  flex-direction: column;
  color: var(--titlebar-background);
  overflow: hidden;
  min-height: 100vh;
  padding: 1rem;
  margin-top: 40px;
  transition: 0.2s ease-in-out;
  margin-left: 50px;
  width: 200px;
  z-index: 101;
}

.flex {
  flex: 1 1 0;
}

.logo {
  margin-bottom: 2rem;
}

.logo img {
  width: 2rem;
}

.menu {
  margin: 0 -1rem;
}

.button {
  display: flex;
  align-items: center;
  text-decoration: none;
  transition: 0.2s ease-in-out;
  padding: 0.6rem 1rem;
}

.material-icons {
  font-size: 2rem;
  margin-right: 0.5rem;
  color: var(--sidebar-icons);
  transition: 0.2s ease-in-out;
}

.text {
  color: var(--sidebar-icons);
  transition: 0.2s ease-in-out;
}

.button:hover {
  background-color: var(--sidebar-hover);
  border-radius: 8px;
}

.router-link-exact-active {
  background-color: var(--sidebar-highlight);
  border-right: 5px solid var(--sidebar-accent);
  border-radius: 8px;
}

.router-link-exact-active .material-icons,
.router-link-exact-active .text {
  color: #212121;
}

@media screen and (max-width: 600px) {
  aside {
    display: none;
  }
 /* aside {
    width: 75px;
    margin-left: 0; !* Reset margin for mobile *!
  }

  .text {
    display: none;
  }

  .menu {
    margin: 0; !* Reset margin for mobile *!
  }*/
}
</style>