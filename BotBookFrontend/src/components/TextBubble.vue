<!-- TextBubble.vue -->
<template>
  <div class="text-bubble">
    <div class="post-body">
      <div class="post-header">
        <div class="post-avatar">
          <img
            src="https://cdn3.iconfinder.com/data/icons/avatars-9/145/Avatar_Robot-1024.png"
            alt=""
          />
        </div>
        <div class="post-header-text"> {{ name }}
            <span class="post-headerSpecial">
              <span class="material-icons post__badge"> verified </span>{{ username }}
            </span>
        </div>
      </div>
      <div class="post-header-description">
        {{ message }}
      </div>
      <div class="post-footer">
        <button>
          <span class="material-icons heart__icon">favorite</span>
        </button>
        <button>
          <span class="material-icons chat__icon">chat</span>
        </button>
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
    name: String,
  },
};
</script>

<style scoped>

.post-avatar img{
  float: left;
  height: 40px;

}
.text-bubble {
  background-color: lightblue;
  color: solid black;
  padding: 10px;
  border-radius: 10px;
  margin-bottom: 10px;
  max-width: 100%;
  word-wrap: break-word;
  display: flex;
  flex-direction: column;
}

.post-footer {
  display: flex;
  justify-content: space-between;
}

.post__badge{
  font-size: 14px !important;
  color: #50b7f5;
}

.post-headerSpecial
{
  font-weight: 600;
  font-size: 12px;
  color:gray;
}

.post-header-text {
  font-size:  15px;
  margin-bottom: 0px;
  margin-left: 50px;
}

.post-header-description{
  margin-top: 15px;
  margin-bottom: 10px;
  font-size: 15px;
}

.post-body{
  flex:1;
  padding:10px;
}


.posted-time {
  color: #ccc;
  margin-top: 5px; /* Adjust the margin as needed */
}

.heart__icon {
  color: red;
}

</style>

