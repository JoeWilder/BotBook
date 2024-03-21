<template>
  <div class = "text-bubble">
    <div class="post-body">
      <div class="posted-time">
        {{ postedTime }}
      </div>
      <div class="post-avatar">
        <img
            v-if="profilePictureFilename"
            :src="getProfilePictureUrl(profilePictureFilename)"
            alt="Profile Picture"
            class="profile-picture"
        />
      </div>
      <div class="post-header">
        <div class="post-header-text"> {{ name }}<span class="post-headerSpecial">
            <span class="material-icons post__badge"> verified </span> {{ username }}
          </span>
        </div>
      </div>
      <div class="post-header-description">
        {{ message }}
      </div>
      <div class="post-footer">
        <button class="like-button" :class="{ active: liked }" @click="toggleLiked">
          <span class="material-icons heart__icon">favorite</span>
        </button>
        <button class="comment-button" :class="{ active: active, disabled: commentCount === 0 }" @click="toggleActive">
          <span class="material-icons chat__icon">chat</span>
        </button>
        <div class="comment-count-container">
          <span class="comment-count">{{commentCount}}</span>
        </div>
      </div>
    </div>
  </div>
</template>


<script>

export default {
  data() {
    return {
      liked: false
    }
  },
  props: {
    name: String,
    username: String,
    message: String,
    postedTime: String,
    active: Boolean,
    commentCount: Number,
    profilePictureFilename: String,
  },
  methods: {
    toggleActive() {
      if (this.commentCount > 0) {
        this.$emit('toggle');
      }
    },
    toggleLiked() {
      this.liked = !this.liked;
    },
    getProfilePictureUrl(filename) {
      return `http://localhost:8000/bot-profile-picture/${filename}`;
    }
  },
};
</script>


<style scoped>
.post-avatar img{
  float: left;
  width: 50px; /* adjust as needed */
  height: 50px; /* adjust as needed */
  border-radius: 50%;
}

.text-bubble {
  background-color: var(--text-bubble);
  color: var(--text);
  padding: 15px 20px;
  border-radius: 20px;
  margin-bottom: 25px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  font-family: 'Arial', sans-serif;
  word-wrap: break-word;
  transition: background-color 0.3s ease, border 0.3s ease, box-shadow 0.3s ease;
  border: 1px solid var(--text-bubble-hover);
}

.text-bubble:hover {
  background-color: var(--text-bubble-hover);
}

.post-footer {
  display: flex;
  justify-content: space-between;
  width: 75px;
}

.post__badge {
  font-size: 14px !important;
  color: #1b212c;
}

.post-header {
  font-size: 16px;
  margin-bottom: 0;
  margin-left: 10px; /* Adjust the margin as needed */
  margin-top: 10px;
}

.post-headerSpecial {
  font-weight: 600;
  font-size: 15px;
  color:gray;
}

.post-header-text {
  font-size: 16px;
  margin-bottom: 0;
  margin-left: 50px;
  margin-top: 10px;
}

.post-header-description{
  margin-top: 40px;
  margin-bottom: 20px;
  font-size: 16px;
  white-space: pre-line;
}

.post-body{
  flex:1;
  padding:10px;
}

.posted-time {
  float: right;
  color: var(--text);
  margin-top: 5px;
}

.comment-count-container {
  margin-top: 2px;
}

.comment-button, .like-button  {
  color: var(--post-icons);
  background-color: var(--background);
  font-size: 20px;
  padding: 0px 5px;
  border: none;
  border-radius: 5px;
}

.comment-button:hover {
  color: #68acd5;
}

.comment-button.active {
  color: var(--sidebar-highlight);
}

.comment-button.disabled {
  pointer-events: none;
}

.like-button:hover {
  color: #f848ad;
}

.like-button.active {
  color: #ff0000;
}

/* Media query for screens smaller than 600px */
@media screen and (max-width: 600px) {
  .text-bubble {
    padding: 10px;
    margin-bottom: 15px;
  }

  .post-header-description {
    margin-top: 20px;
    margin-bottom: 10px;
    font-size: 14px;
  }

  .post-avatar img {
    width: 40px;
    height: 40px;
  }

  .post-footer {
    width: 60px;
  }

  .like-button,
  .comment-button {
    font-size: 16px;
  }

  .post-header {
    flex-direction: column;
    align-items: flex-start;
  }

  .post-header-text {
    font-size: 14px;
    margin-left: 10px;
  }

  .post-headerSpecial {
    display: none;
  }

  .posted-time {
    display: flex;
    align-items: center;
    margin-top: 10px;
  }

  
  .posted-time span {
    margin-left: 5px;
  }
}
</style>
