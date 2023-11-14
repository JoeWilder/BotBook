<template>
  <div class="comment-feed">
    <div class="comment" v-for="(comment, index) in comments" :key="index">
      <div class="post-avatar">
        <img
          src="https://cdn3.iconfinder.com/data/icons/avatars-9/145/Avatar_Robot-1024.png"
          alt=""
        />
      </div>
      <div class="comment-content">
        <div class="comment-header">
          <div class="comment-username">{{ comment.username }}</div>
          <div class="comment-time">{{ comment.postedTime }}</div>
        </div>
        <div class="comment-message">{{ comment.message }}</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    comments: Array, // Pass the comments data as a prop
  },
};
</script>

<style scoped>
.comment-feed {
  position: fixed;
  top: 40px; /* Adjust the top position to align with the margin */
  right: 0; /* Adjust the right position to leave space from the right edge */
  width: 270px; /* Adjust to your desired width */
  background-color: #e1e1e1; /* Set the background color to your preference */
  border: 1px solid #ccc; /* Add a border for separation */
  border-radius: 15px;
  padding: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Add a subtle box shadow */
  z-index: 100; /* Place it above other content */
}

.comment {
  border-bottom: 1px solid #ccc;
  padding: 10px 0;
  display: flex; /* Use flex display for positioning */
}

.post-avatar img {
  float: left;
  height: 30px;
}

.comment-content {
  flex: 1; /* Use flex-grow to allow the content to take the remaining space */
}

.comment-header {
  display: flex;
  justify-content: space-between;
}

.comment-username {
  font-weight: bold;
  margin-bottom: 5px;
  margin-top: 5px;
  margin-left: 5px;
}

.comment-time {
  font-size: 12px;
  color: #888;
}

.comment-message {
  font-size: 14px;
  line-height: 1.4;
}
</style>
