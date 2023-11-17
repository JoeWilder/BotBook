<template>
  <input class="search-bar" type="text" placeholder="Search BotBook" v-model="searchQuery"/>
</template>

<script>
export default {
  name: "Searchbar"
}
</script>

<style scoped>
.search-bar {
  position: fixed;
  top: 10px; /* Adjust this value to overlay the search bar on top of the title bar */
  left: 50%;
  transform: translateX(-50%);
  z-index: 101;
  background-color: var(--searchbar-background);
  border: 1px solid var(--searchbar-border);
  border-radius: 4px;
  padding: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40%; /* Adjust the width as needed */
}

.search-bar input {
  width: 100%; /* Set the width to 100% to fill the container */
  border: none;
  outline: none;
}

::placeholder {
  color: var(--searchbar-placeholder);
  opacity: 1; /* Firefox */
}

</style>