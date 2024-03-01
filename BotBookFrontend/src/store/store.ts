import { createStore } from 'vuex';
import axios from 'axios'

const store = createStore({
  state() {
    return {
      posts: [],
    };
  },
  mutations: {
    setPosts(state, posts) {
      state.posts = posts;
    },
    filterPosts(state, searchTerm) {
      if (!searchTerm) {
        state.posts = [];
        store.dispatch("fetchContentData")
      } else {
        state.posts = state.posts.filter(post =>
          post.name.toLowerCase().includes(searchTerm.toLowerCase())
        );
      }
    }
  },
  actions: {
    async fetchContentData({}) {
      const posts: any = [];
      try {
        const response: any = await axios.get('http://127.0.0.1:8000/posts/')
        response.data.sort((a, b) => new Date(b.createdAt).valueOf() - new Date(a.createdAt).valueOf())
        
        for (let post of response.data) {
          const profilePictureResponse = await axios.get(`http://127.0.0.1:8000/profilepicture/${post.authorId}`)
          const profilePictureFilename = profilePictureResponse.data
          
          const commentsResponse = await axios.get(`http://127.0.0.1:8000/comments/${post.postId}`)
          const commentArray: any = [];
          
          for (let comment of commentsResponse.data) {
            const commentProfilePictureResponse = await axios.get(`http://127.0.0.1:8000/profilepicture/${comment.authorId}`)
            const commentProfilePictureFilename = commentProfilePictureResponse.data
            
            interface PostComment {
              username: string;
              message: string;
              postedTime: string; // Assuming postedTime is a string; adjust type if necessary
              profilePictureFilename: string;
            }

            commentArray.push({
              username: comment.name,
              message: comment.body,
              postedTime: comment.createdAt,
              profilePictureFilename: commentProfilePictureFilename
            } as PostComment)

            
          }
          
          posts.push({
            postId: post.postId,
            name: post.name,
            username: "@" + post.username,
            message: post.body,
            postedTime: post.createdAt,
            comments: commentArray,
            profilePictureFilename
          })
        }
        
        posts.sort((a, b) => new Date(b.postedTime).valueOf() - new Date(a.postedTime).valueOf())
        store.commit('setPosts', posts)
      } catch (error) {
        console.error('Error fetching data:', error)
      }
    }
  },
  getters: {
    // Optionally, you can define getters to access the posts
    getPosts(state) {
      return state.posts;
    },
  },
});

export default store;