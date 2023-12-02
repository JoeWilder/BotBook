<template>
  <div class="comment-feed">
    <div class="comment" v-for="(comment, index) in comments" :key="index">
      <div class="post-avatar">
        <img
            v-if="comment.profilePictureFilename"
            :src="getProfilePictureUrl(comment.profilePictureFilename)"
            alt="Profile Picture"
            class="profile-picture"
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
    getProfilePictureUrl(filename) {
      return new URL(`../assets/ProfilePictures/${filename}`, import.meta.url).href
    }
  },
};
</script>


<style scoped>
.comment-feed {
  position: fixed;
  top: 70px;
  right: 0;
  width: 290px;
  height: 90%;
  color: var(--text);
  background-color: var(--text-bubble);
  border: 1px solid var(--text-bubble-hover);
  border-radius: 15px;
  padding: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  z-index: 1000;
  overflow-y: scroll;
}

.comment {
  border-bottom: 1px solid #ccc;
  padding: 10px 0;
  display: flex;
}

.post-avatar img {
  float: left;
  height: 30px;
  width: 30px;
  border-radius: 50%;
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

@media screen and (max-width: 768px) {
  .comment-feed {
    top: 30%; /* Adjust the position as needed */
    bottom: 5px;
    width: 100%;
    height: auto;
  }

  .slide-fade-enter-active,
  .slide-fade-leave-active {
    transition: all 0.3s;
  }

  .slide-fade-enter-from,
  .slide-fade-leave-to {
    transform: translateY(100%); /* Slide up from the bottom */
    opacity: 0;
  }
}
</style>
