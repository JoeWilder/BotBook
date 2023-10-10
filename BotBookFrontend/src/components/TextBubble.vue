<!-- TextBubble.vue -->
<template>
  <div class="text-bubble">
    <div class="user-info">
      <div class="username">{{ username }}</div>
      <div class="posted-time">{{ postedTime }}</div>
    </div>
    <hr class="separator" />
    <div class="message-container">
      <div class="message">{{ message }}</div>
      <!-- Move the posted-time element here -->
    </div>
  </div>
</template>

<script>
export default {
  props: {
    username: String,
    message: String,
    postedTime: String,
  },
};
</script>

<style scoped>
.text-bubble {
  background-color: #007bff;
  color: #fff;
  padding: 10px;
  border-radius: 10px;
  margin-bottom: 10px;
  max-width: 70%;
  word-wrap: break-word;
  display: flex;
  flex-direction: column;
  /* Remove align-items: flex-start; to prevent blocking */
}

.user-info {
  display: flex;
  justify-content: space-between;
  width: 100%;
}

.username {
  font-weight: bold;
}

.separator {
  border: none;
  height: 1px;
  background-color: #ffffff;
  margin: 5px 0;
}

.message-container {
  /* Add styles for the message container here */
}

.message {
  margin-top: 5px;
}

.posted-time {
  color: #ccc;
  margin-top: 5px; /* Adjust the margin as needed */
}
</style>
