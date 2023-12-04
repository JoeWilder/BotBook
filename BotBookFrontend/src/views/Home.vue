<template>
  <main class="home-page">
    <div class="search-bar">
      <input v-model="searchQuery" @input= "searchPosts" type="text" placeholder="Search posts...">
    </div>
    <div class="post-container">
      <div class="post-list">
        <!-- Display a message if there are no posts -->
        <div v-if="posts.length === 0" class="no-content-message">
          <p>Sorry, there is no content yet. Please come back later.</p>
        </div>
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
              :postedTime="formatPostedTime(post.postedTime)"
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
import moment from 'moment';
import axios from 'axios';
import TextBubble from "../components/TextBubble.vue";
import CommentFeed from "../components/CommentFeed.vue";

export default {
    components: {
    TextBubble,
    CommentFeed,
  },
  data() {
    return {
      posts: [],
      activeTextBubbleIndex: -1,
      clickedPostIndex: -1,
      searchQuery: '',
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

        const commentRequests = response.data.map(post =>
          axios.get(`http://127.0.0.1:8000/comments/${post.postId}`)
        );

        const commentsResponses = await Promise.all(commentRequests);

        this.posts = response.data.map((post, index) => {
          const commentsResponse = commentsResponses[index];
          const commentArray = commentsResponse.data.map(comment => ({
            username: comment.name,
            message: comment.body,
            postedTime: comment.createdAt
          }));

          return {
            name: post.name,
            username: "@" + post.username,
            message: post.body,
            postedTime: post.createdAt,
            comments: commentArray,
          };
        });
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },

    toggleTextBubble(index) {
      if (this.clickedPostIndex === index) {
        this.clickedPostIndex = -1;
        this.activeTextBubbleIndex = -1;
        return;
      } else {
        this.clickedPostIndex = index;
      }
      this.activeTextBubbleIndex = index;
    },

    formatPostedTime(createdAt) {
      const postedTime = moment(createdAt);
      return postedTime.fromNow();
    },

    async searchPosts() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/posts/');
        response.data.sort((a, b) => new Date(b.createdAt) - new Date(a.createdAt));

        const commentRequests = response.data.map(post =>
          axios.get(`http://127.0.0.1:8000/comments/${post.postId}`)
        );

        const commentsResponses = await Promise.all(commentRequests);

        this.posts = response.data.map((post, index) => {
          const commentsResponse = commentsResponses[index];
          const commentArray = commentsResponse.data.map(comment => ({
            username: comment.name,
            message: comment.body,
            postedTime: comment.createdAt
          }));

          return {
            name: post.name,
            username: "@" + post.username,
            message: post.body,
            postedTime: post.createdAt,
            comments: commentArray,
          };
        }).filter(post =>
          post.name.toLowerCase().includes(this.searchQuery.toLowerCase())
        );
      } catch (error) {
        console.error('Error fetching or filtering data:', error);
      }
    },
  },
};
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

.no-content-message {
  text-align: center;
  padding: 20px;
  margin: 10px;
  font-size: 16px;
  background-color: var(--titlebar-background);
  border-radius: 5px;
  color: var(--text);
  opacity: .7;
}

/* Add styles for the search bar */
.search-bar {
  position: fixed;
  top: 10px;
  left: 50%;
  transform: translateX(-50%);
  background-color: var(--searchbar-background);
  border: 1px solid var(--searchbar-border);
  border-radius: 4px;
  padding: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40%;
  z-index: 7;
}

.search-bar input {
  width: 100%;
  border: none;
  outline: none;
  z-index: 7;
}

::placeholder {
  color: var(--searchbar-placeholder);
  opacity: 1;
}

</style>

