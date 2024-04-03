import { createStore } from 'vuex';
import axios from 'axios'
 
const store = createStore({
  state() {
    return {
      posts: [],
      authToken: null,
      ownerId: null,
      username: null,
      email: null,
      name: null,
      profilePictureFilename: null,
      joinDate: null,
      bots: [],

    };
  },
  mutations: {
    setPosts(state, posts) {
      state.posts = posts;
    },
    setAuthToken(state, token) {
      state.authToken = token;
    },
    clearAuthToken(state) {
      state.authToken = null;
    },
    setOwnerId(state, ownerId) {
      state.ownerId = ownerId
    },
    setUsername(state, username) {
      state.username = username;
    },
    setProfilePicture(state, pfp) {
      state.profilePictureFilename = pfp;
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
    },
    async fetchOwnerData({ state }) {
      try {

        const config = {
          headers: {
            'token': `${state.authToken}`,
          }
        };

        const response = await axios.get(`http://127.0.0.1:8000/owner/${state.ownerId}`, config);
        console.log(response.data.profilePictureFilename)
        state.name = response.data.name
        state.email = response.data.email
        state.profilePictureFilename = response.data.profilePictureFilename
        state.joinDate = response.data.createdAt
        state.bots = response.data.bots
      } catch (error) {
        console.error('Error fetching owner data:', error);
      }
    }
  },
  getters: {
    getPosts(state) {
      return state.posts;
    },
    isAuthenticated(state) {
      return !!state.authToken;
    },
    getUsername(state) {
      return state.username;
    },
    getEmail(state) {
      return state.email
    },
    getName(state) {
      return state.name
    },
    getProfilePictureFilename(state) {
      return state.profilePictureFilename
    },
    getJoinDate(state) {
      return state.joinDate
    },
    getBots(state) {
      return state.bots
    },
    getOwnerId(state) {
      return state.ownerId
    },
    getToken(state) {
      return state.getToken
    }
  },
});
 
export default store;