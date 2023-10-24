<template>
  <main class="home-page">
    <div class="post-container">
      <div class="post-list">
        <div class="post" v-for="(post, index) in posts" :key="index">
          <div
              :class="{
              'post-content': true,
              'inactive-text-bubble': clickedPostIndex !== -1 && clickedPostIndex !== index,
            }"
          >
            <TextBubble
                :name="post.name"
                :username="post.username"
                :message="post.message"
                :postedTime="post.postedTime"
                :active="activeTextBubbleIndex === index"
                :comment-count="post.comments.length"
                @toggle="toggleTextBubble(index)"
            />
          </div>
            <transition name="slide-fade">
              <CommentFeed
                  v-if="activeTextBubbleIndex === index"
                  :comments="post.comments"
              />
            </transition>

        </div>
      </div>
    </div>
  </main>
</template>




<script>
  import TextBubble from "../components/TextBubble.vue"
  import CommentFeed from "../components/CommentFeed.vue"

  export default {
    components: {
      TextBubble,
      CommentFeed
    },
    data() {
      return {
        posts: [
          {
            name: "Bot Guy",
            username: "@User1",
            message: "Hello, World! How are you doing today? How are you doing today? How are you doing today? How are you doing today? How are you doing today? How are you doing today? How are you doing today? Working on CS stuff. Working on CS stuff. Working on CS stuff. Working on CS stuff. Working on CS stuff. Working on CS stuff. Working on CS stuff.",
            postedTime: "37 minutes ago",
            comments: [{
              username: "UserA",
              message: "Comment 1 for User1",
              postedTime: "10 minutes ago",
            },
              {
                username: "UserB",
                message: "Comment 2 for User1",
                postedTime: "5 minutes ago",
              },],
          },
          {
            name: "Egbert",
            username: "@User2",
            message: "Vue.js is working!",
            postedTime: "1 hour ago",
            comments: [{
              username: "UserA",
              message: "Comment 1 for User1",
              postedTime: "10 minutes ago",
            },
              {
                username: "UserB",
                message: "Comment 2 for User1",
                postedTime: "5 minutes ago",
              },],
          },
          {
            name: "Name3",
            username: "@User3",
            message: "Hello, World! How are you doing today? How are you doing today? How are you doing today? How are you doing today? How are you doing today? How are you doing today? How are you doing today? Working on CS stuff. Working on CS stuff. Working on CS stuff. Working on CS stuff. Working on CS stuff. Working on CS stuff. Working on CS stuff.",
            postedTime: "37 minutes ago",
            comments: [{
              username: "UserA",
              message: "Comment 1 for User1",
              postedTime: "10 minutes ago",
            },
              {
                username: "UserB",
                message: "Comment 2 for User1",
                postedTime: "5 minutes ago",
              },],
          },{
            name: "Name4",
            username: "@User4",
            message: "Hello, World! How are you doing today? How are you doing today? How are you doing today? How are you doing today? How are you doing today? How are you doing today? How are you doing today? Working on CS stuff. Working on CS stuff. Working on CS stuff. Working on CS stuff. Working on CS stuff. Working on CS stuff. Working on CS stuff.",
            postedTime: "37 minutes ago",
            comments: [],
          },{
            name: "Name5",
            username: "@User5",
            message: "Hello, World! How are you doing today? How are you doing today? How are you doing today? How are you doing today? How are you doing today? How are you doing today? How are you doing today? Working on CS stuff. Working on CS stuff. Working on CS stuff. Working on CS stuff. Working on CS stuff. Working on CS stuff. Working on CS stuff.",
            postedTime: "37 minutes ago",
            comments: [],
          },
        ],
        activeTextBubbleIndex: -1,
        clickedPostIndex: -1,
      };
    },
    methods: {
      toggleTextBubble(index) {
        if (this.clickedPostIndex === index) {
          this.clickedPostIndex = -1; // Unset the clicked post
          this.activeTextBubbleIndex = -1;
          return
        } else {
          this.clickedPostIndex = index;
        }
        this.activeTextBubbleIndex = index;
      },
    },
  }
</script>

<style>
  .post-container {
    overflow-y: auto;
  }

  .inactive-text-bubble {
    filter: blur(0px);
    opacity: .6;
  }

  .comment-feed {
    position: fixed;
    top: 0;
    right: 0;
    width: 300px; /* Adjust the width to fit your design. */
    height: 100%; /* Make the comment feed take the full screen height. */
    background-color: #64748b; /* Adjust the background color. */
    overflow-y: auto;
  }

  .slide-fade-enter-active {
    transition: all 0.3s; /* Adjust the transition duration */
  }

  .slide-fade-leave-active {
    transition: all 0.3s; /* Adjust the transition duration */
  }

  .slide-fade-enter-from {
    transform: translateX(100%); /* Slide in from the right */
    opacity: 0;
  }

  .slide-fade-leave-to {
    transform: translateX(100%); /* Slide out to the right */
    opacity: 0;
  }





</style>

