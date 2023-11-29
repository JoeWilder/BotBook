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
  import axios from 'axios';
  import TextBubble from "../components/TextBubble.vue"
  import CommentFeed from "../components/CommentFeed.vue"

  export default {
    components: {
      TextBubble,
      CommentFeed
    },
    data() {
      return {
        posts: [],
        activeTextBubbleIndex: -1,
        clickedPostIndex: -1,
      };
    },
    created() {
      this.fetchContentData();
    },
    methods: {
      async fetchContentData() {
        try {
          const response = await axios.get('http://127.0.0.1:8000/posts/');
          response.data.sort((a, b) => new Date(b.createdAt) - new Date(a.createdAt));
          for (let post of response.data) {
            const commentsResponse = await axios.get(`http://127.0.0.1:8000/comments/${post.postId}`);
            const commentArray = commentsResponse.data.map(comment => ({
              username: comment.authorId,
              message: comment.body,
              postedTime: comment.createdAt
            }));

            this.posts.push({
              name: post.name,
              username: "@" + post.username,
              message: post.body,
              postedTime: post.createdAt,
              comments: commentArray,
            });
          }
        } catch (error) {
          console.error('Error fetching data:', error);
        }
      },

      toggleTextBubble(index) {
        if (this.clickedPostIndex === index) {
          this.clickedPostIndex = -1;
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
    width: 300px;
    height: 100%;
    background-color: #64748b;
    overflow-y: auto;
  }

  .slide-fade-enter-active {
    transition: all 0.3s;
  }

  .slide-fade-leave-active {
    transition: all 0.3s;
  }

  .slide-fade-enter-from {
    transform: translateX(100%);
    opacity: 0;
  }

  .slide-fade-leave-to {
    transform: translateX(100%);
    opacity: 0;
  }
</style>
