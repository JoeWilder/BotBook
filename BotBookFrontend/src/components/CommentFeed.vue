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
          <div class="comment-time">{{ formatPostedTime(comment.postedTime) }}</div>
        </div>
        <div class="comment-message">{{ comment.message }}</div>
      </div>
    </div>
  </div>
</template>


<script>
import moment from "moment/moment.js";

export default {
  props: {
    comments: Array
  },methods: {
    formatPostedTime(createdAt) {
      const postedTime = moment(createdAt);
      return postedTime.fromNow();
    },
  },
};
</script>


<style scoped>
.comment-feed {
  position: fixed;
  top: 70px;
  right: 0;
  width: 290px;
  color: var(--text);
  background-color: var(--text-bubble);
  border: 1px solid var(--text-bubble-hover);
  border-radius: 15px;
  padding: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  z-index: 100;
}

.comment {
  border-bottom: 1px solid #ccc;
  padding: 10px 0;
  display: flex;
}

.post-avatar img {
  float: left;
  height: 30px;
}

.comment-content {
  flex: 1;
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
  color: var(--text);
}

.comment-message {
  font-size: 14px;
  line-height: 1.4;
}
</style>
