<template>
  <div class="comment">
    <div class="comment-content">
      <div class="user-info">
        <div class="username">{{ username }}</div>
        <div class="posted-time">{{ postedTime }}</div>
      </div>
      <hr class="separator" />
      <div class="message-container">
        <div class="message">{{ message }}</div>
      </div>
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
.comment {
  /* Style the comment container (outer div) */
  display: flex;
  justify-content: flex-end; /* Align to the right */
  margin-bottom: 10px;
}

.comment-content {
  background-color: #007bff;
  color: #fff;
  padding: 10px;
  border-radius: 10px;
  min-width: 70%; /* Adjust the min-width as needed */
  word-wrap: break-word;
/* Maintain flex-direction: column; */

/* Use media queries for responsive design */
@media (max-width: 768px) {
  min-width: 80%;
}

@media (max-width: 576px) {
  min-width: 90%;
}
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
  background-color: #fff;
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
