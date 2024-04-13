<template>
    <div class="post-container q-px-xl">
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
</template>

<script setup>
import { useStore } from 'vuex';
import { ref, onMounted, computed } from 'vue'
import axios from 'axios'
import moment from 'moment'
import TextBubble from "../components/TextBubble.vue"
import CommentFeed from "../components/CommentFeed.vue"

const store = useStore();
const posts = computed(() => store.state.posts);
let clickedPostIndex = ref(-1)
let activeTextBubbleIndex = ref(-1)


const toggleTextBubble = (index) => {
  if (clickedPostIndex.value === index) {
    clickedPostIndex.value = -1
    activeTextBubbleIndex.value = -1
  } else {
    clickedPostIndex.value = index
    activeTextBubbleIndex.value = index
  }
}

const formatPostedTime = (createdAt) => {
  const postedTime = moment(createdAt)
  return postedTime.fromNow()
}

onMounted(() => {
  store.dispatch('fetchContentData')
})




</script>

<style lang="scss">

.post-container {
  display: flex;
  flex-direction: column;
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

</style>
