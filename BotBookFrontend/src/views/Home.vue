<template>
  <main class="home-page">
    <div class="search-bar">
      <input v-model="searchQuery" @input= "searchPosts" type="text" placeholder="Search posts...">
    </div>
    <div class="post-container">
      <div class="post-list">
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
                :profilePictureFilename="post.profilePictureFilename"
                @toggle="toggleTextBubble(index)"
            />
          </div>
          <transition name="slide-fade">
            <CommentFeed
                v-if="activeTextBubbleIndex === index"
                :comments="post.comments"
                class = "comment-feed"
                @click = "toggleTextBubble(-1)"
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
      searchQuery: ''
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

          //console.log(post)
          const profilePictureResponse = await axios.get(`http://127.0.0.1:8000/profilepicture/${post.authorId}`);
          const profilePictureFilename = profilePictureResponse.data; // Assuming the endpoint returns a single filename


          const commentsResponse = await axios.get(`http://127.0.0.1:8000/comments/${post.postId}`);
          const commentArray = [];


          for (let comment of commentsResponse.data) {
            const commentProfilePictureResponse = await axios.get(`http://127.0.0.1:8000/profilepicture/${comment.authorId}`);
            const commentProfilePictureFilename = commentProfilePictureResponse.data;

            commentArray.push({
              username: comment.name,
              message: comment.body,
              postedTime: comment.createdAt,
              profilePictureFilename: commentProfilePictureFilename,
            });
          }

          this.posts.push({
            name: post.name,
            username: "@" + post.username,
            message: post.body,
            postedTime: post.createdAt,
            comments: commentArray,
            profilePictureFilename

          });
        }
        this.posts.sort((a, b) => new Date(b.postedTime) - new Date(a.postedTime));
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
    formatPostedTime(createdAt) {
      const postedTime = moment(createdAt);
      return postedTime.fromNow();
    },
    async searchPosts() {
      if (this.searchQuery.trim() === '') {
        // If the search query is empty, reset posts to the original set
        this.posts.length = 0;
        await this.fetchContentData();
      } else {
        // Filter posts based on the search query
        this.posts = this.posts.filter(post =>
            post.name.toLowerCase().includes(this.searchQuery.toLowerCase())
        );
      }
    }
  },
}
</script>


<style lang="scss">

.post-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh; /* Minimum height to fill the viewport */
}


.inactive-text-bubble {
  filter: blur(0px);
  opacity: .6;
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

  /* Apply additional styles for smaller screens */
  @media (max-width: 600px) {
    font-size: 14px;
    padding: 15px;
    margin: 5px;
  }
}

.search-bar {
  position: fixed;
  top: 10px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 101;
  background-color: var(--searchbar-background) !important;
  border: 1px solid var(--searchbar-border);
  border-radius: 4px;
  padding: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40%;
}

.search-bar input {
  width: 100%;
  border: none;
  outline: none;
  background-color: var(--searchbar-background);
}

::placeholder {
  color: var(--searchbar-placeholder);
  opacity: 1;
}
</style>