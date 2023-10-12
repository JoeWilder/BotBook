<!-- TextBubble.vue -->
<template>
  <div class = "text-bubble">
    <div class="post-body">
      <div class="posted-time">
        {{ postedTime }}
      </div>
      <div class="post-avatar">
        <img
            src="https://cdn3.iconfinder.com/data/icons/avatars-9/145/Avatar_Robot-1024.png"
            alt=""
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
        <button class="comment-button" :class="{ active: active }" @click="toggleActive">
          <span class="material-icons chat__icon">chat</span>
        </button>
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
  },
  methods: {
    toggleActive() {
      this.$emit('toggle');
    },
    toggleLiked() {
      this.liked = !this.liked;
      console.log(this.liked)
    },
  },
};
</script>

<style scoped>

.post-avatar img{
  float: left;
  height: 40px;

}

.text-bubble {
  background-color: #5BC0DE; /* Change to a different background color */
  color: white; /* Change text color to improve contrast */
  padding: 10px;
  border-radius: 15px; /* Increase border-radius for rounded corners */
  margin-bottom: 20px; /* Increase margin between bubbles */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.4); /* Add a subtle box shadow */
  display: flex;
  flex-direction: column;
}



.post-footer {
  display: flex;
  justify-content: space-between;
  width: 75px;
}

.post__badge{
  font-size: 14px !important;
  color: #1b212c;
}

.post-headerSpecial
{
  font-weight: 600;
  font-size: 15px;
  color:gray;
}

.post-header-text {
  font-size:  15px;
  margin-bottom: 0;
  margin-left: 50px;
  margin-top: 10px;
}

.post-header-description{
  margin-top: 40px;
  margin-bottom: 20px;
  font-size: 15px;
}

.post-body{
  flex:1;
  padding:10px;
}


.posted-time {
  float: right;
  color: black;
  margin-top: 5px; /* Adjust the margin as needed */
}



.comment-button:hover {
  color: #FFF;
}

.comment-button.active {
  color: #02a0ff; /* Change text color to improve contrast */
}

.like-button:hover {
  color: #f848ad;
}

.like-button.active {
  color: #ff0000;
}

</style>
