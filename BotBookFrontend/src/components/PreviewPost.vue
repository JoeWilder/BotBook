<template>
  <div class = "text-bubble">
    <div class="post-body">
      <div class="post-avatar">
        <img
            v-if="profilePictureFilename"
            :src="getProfilePictureUrl(profilePictureFilename)"
            alt="Profile Picture"
            class="profile-picture"
        />
      </div>
      <div class="post-header">
        <div class="post-header-text"> {{ name }}
        </div>
      </div>
      <div class="post-header-description">
        <p>
            <span id="typewriter">{{ typedText }}</span><span id="cursor">|</span>
        </p>
      </div>
    </div>
  </div>
</template>


<script>

export default {
  data() {
    return {
        typedText: ''
        
    }
  },
  props: {
    name: String,
    message: String,
    profilePictureFilename: String,
  },
  methods: {
    getProfilePictureUrl(filename) {
      return new URL(`../assets/ProfilePictures/${filename}`, import.meta.url).href
    },
    async startTypingAnimation() {
      const text = this.message;
      while (true) {
        for (let i = 0; i < text.length; i++) {
          this.typedText += text.charAt(i);
          await this.typewriterSleep(50); // Adjust typing speed as needed
        }
    
        await this.typewriterSleep(2500); // Pause before starting again
        this.typedText = ''; // Clear typed text
      }
    },
    typewriterSleep(ms) {
      return new Promise((resolve) => setTimeout(resolve, ms));
    },
  },
  mounted() {
    console.log("EEAOEUFH");
    this.startTypingAnimation();
  },
};
</script>


<style scoped>
.post-avatar img{
  float: left;
  width: 50px; /* adjust as needed */
  height: 50px; /* adjust as needed */
  border-radius: 50%;
}

.text-bubble {
    
  background-color: var(--text-bubble);
  color: var(--text);
  padding: 15px 20px;
  border-radius: 20px;
  margin-bottom: 25px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  font-family: 'Arial', sans-serif;
  word-wrap: break-word;
  transition: background-color 0.3s cubic-bezier(0.68, -0.55, 0.27, 1.55);
  border: 1px solid var(--text-bubble-hover);
}

.text-bubble:hover {
  background-color: var(--text-bubble-hover);
}




.post-header {
  font-size: 16px;
  margin-bottom: 0;
  margin-left: 10px; /* Adjust the margin as needed */
  margin-top: 10px;
}


.post-header-text {
  font-size: 16px;
  margin-bottom: 0;
  margin-left: 50px;
  margin-top: 10px;
}

.post-header-description {
  margin-top: 40px;
  margin-bottom: 20px;
  font-size: 16px;
  letter-spacing: 1px;
}



.post-body{
  flex:1;
  padding:10px;
}


#cursor {
    color: var(--sidebar-highlight);
    animation: blink 1s linear infinite;
}

@keyframes blink {
    0% {
        opacity: 100%;
    }

    50% {
        opacity: 0%;
    }
}



/* Media query for screens smaller than 600px */
@media screen and (max-width: 600px) {
  .text-bubble {
    padding: 10px;
    margin-bottom: 15px;
  }

  .post-header-description {
    margin-top: 20px;
    margin-bottom: 10px;
    font-size: 14px;
  }

  .post-avatar img {
    width: 40px;
    height: 40px;
  }

  

  .post-header {
    flex-direction: column;
    align-items: flex-start;
  }

  .post-header-text {
    font-size: 14px;
    margin-left: 10px;
  }

  .post-headerSpecial {
    display: none;
  }

}


</style>
