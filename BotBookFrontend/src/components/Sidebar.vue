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


<style lang="scss" scoped>
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
  z-index: 100;
  transition: 0.2s ease-in-out;
  margin-left: 50px;
  width: 200px;

  .flex {
    flex: 1 1 0;
  }

  .logo {
    margin-bottom: 2rem;

    img {
      width: 2rem;
    }
  }

  .menu {
    margin: 0 -1rem;

    .button {
      display: flex;
      align-items: center;
      text-decoration: none;
      transition: 0.2s ease-in-out;
      padding: .6rem 1rem;

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

      &:hover {
        background-color: var(--sidebar-hover);
        border-radius: 8px;
      }

      &.router-link-exact-active {
        background-color: var(--sidebar-highlight);
        border-right: 5px solid var(--sidebar-accent);
        border-radius: 8px;

        .material-icons, .text {
          color: #212121;
        }
      }
    }
  }

  @media (max-width: 896px) {
    z-index: 200;
    display: none;
  }
}
</style>