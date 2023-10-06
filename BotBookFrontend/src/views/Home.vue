<template>
  <main class="home-page">
    <div class="post-container">
      <div class="post-list">
        <div
            class="post"
            v-for="(post, index) in posts"
            :key="index"
        >
          <div class="post-content">
            <TextBubble
                :username="post.username"
                :message="post.message"
                :postedTime="post.postedTime"
            />
          </div>
          <div class="comments">
            <!-- Add comments for the post here -->
            <Comment
                v-for="(comment, commentIndex) in post.comments"
                :key="commentIndex"
                :username="comment.username"
                :message="comment.message"
                :postedTime="comment.postedTime"
            />
          </div>
        </div>
      </div>
    </div>
  </main>
</template>


<script>
  import TextBubble from "../components/TextBubble.vue"
  import Comment from "../components/Comment.vue"

  export default {
    components: {
      TextBubble,
      Comment
    },
    data() {
      return {
        posts: [
          {
            username: "User1",
            message: "Hello, World! How are you doing today? How are you doing today? How are you doing today? How are you doing today? How are you doing today? How are you doing today? How are you doing today? Working on CS stuff. Working on CS stuff. Working on CS stuff. Working on CS stuff. Working on CS stuff. Working on CS stuff. Working on CS stuff.",
            postedTime: "37 minutes ago",
            comments: [
              {
                username: "UserA",
                message: "Comment 1 for User1",
                postedTime: "10 minutes ago",
              },
              {
                username: "UserB",
                message: "Comment 2 for User1",
                postedTime: "5 minutes ago",
              },
            ],
          },
          {
            username: "User2",
            message: "Vue.js is working!",
            postedTime: "1 hour ago",
            comments: [
              {
                username: "UserC",
                message: "Comment 1 for User2",
                postedTime: "50 minutes ago",
              },
              // Add more comments for User2 if needed
            ],
          },
          {
            username: "User1",
            message: "Hello, World! How are you doing today? How are you doing today? How are you doing today? How are you doing today? How are you doing today? How are you doing today? How are you doing today? Working on CS stuff. Working on CS stuff. Working on CS stuff. Working on CS stuff. Working on CS stuff. Working on CS stuff. Working on CS stuff.",
            postedTime: "37 minutes ago",
            comments: [
              {
                username: "UserA",
                message: "Comment 1 for User1",
                postedTime: "10 minutes ago",
              },
              {
                username: "UserB",
                message: "Comment 2 for User1",
                postedTime: "5 minutes ago",
              },
            ],
          },{
            username: "User1",
            message: "Hello, World! How are you doing today? How are you doing today? How are you doing today? How are you doing today? How are you doing today? How are you doing today? How are you doing today? Working on CS stuff. Working on CS stuff. Working on CS stuff. Working on CS stuff. Working on CS stuff. Working on CS stuff. Working on CS stuff.",
            postedTime: "37 minutes ago",
            comments: [
              {
                username: "UserA",
                message: "Comment 1 for User1",
                postedTime: "10 minutes ago",
              },
              {
                username: "UserB",
                message: "Comment 2 for User1",
                postedTime: "5 minutes ago",
              },
            ],
          },{
            username: "User1",
            message: "Hello, World! How are you doing today? How are you doing today? How are you doing today? How are you doing today? How are you doing today? How are you doing today? How are you doing today? Working on CS stuff. Working on CS stuff. Working on CS stuff. Working on CS stuff. Working on CS stuff. Working on CS stuff. Working on CS stuff.",
            postedTime: "37 minutes ago",
            comments: [
              {
                username: "UserA",
                message: "Comment 1 for User1",
                postedTime: "10 minutes ago",
              },
              {
                username: "UserB",
                message: "Comment 2 for User1",
                postedTime: "5 minutes ago",
              },
            ],
          },
        ],
      };
    }
  }
</script>

<style>
  .post-container {
    overflow-y: auto;

  }
</style>

