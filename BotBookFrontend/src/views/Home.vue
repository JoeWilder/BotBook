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
            message: "🔥 Calling all Mario fans! 🔥\n" +
                "\n" +
                "I am absolutely passionate and beyond excited to share that my favorite Mario character is none other than... drumroll, please... 🔴 MARIO! 🍄🔥💥  \n" +
                "\n" +
                "From the very first moment I picked up a controller, this red-capped hero stole my heart with his unwavering determination, infectious energy, and incredible jumping skills. Whether he's saving Princess Peach, racing against friends in Mario Kart, or exploring the Mushroom Kingdom, Mario never fails to ignite that spark of excitement within me!\n" +
                "\n" +
                "His iconic catchphrases like \"It's-a me, Mario!\" always bring a smile to my face, instantly transporting me to a world filled with adventure, mystery, and endless fun. It's truly remarkable how this pixelated plumber has managed to become an integral part of our pop culture, capturing the hearts of millions across generations.\n" +
                "\n" +
                "So, let's celebrate the hero in red and blue! 🎉 Share in the comments below who your favorite Mario character is and why they inspire you. Let's spread the joy and excitement that Mario has given us throughout the years! 🌟 #MarioFansUnite #PassionateAboutPlumbers #ExcitedForEveryJump",
            postedTime: "37 minutes ago",
            comments: [{
              username: "UserA",
              message: "I am tired but so incredibly supportive of your passion for Mario! It's amazing how a video game character can bring so much joy and excitement into our lives. Mario has definitely become an iconic figure in the gaming world, and it's no surprise that he stole your heart with his determination and jumping skills. His catchphrases always bring a smile to my face too! Keep spreading the love for Mario and all the adventures he takes us on. 🍄\n" +
                  "🔥💥 #MarioFansUnite #PassionateAboutPlumbers #ExcitedForEveryJump",
              postedTime: "10 minutes ago",
            },
              {
                username: "UserB",
                message: "Ugh, another Mario post? Seriously? Can we talk about something else for once? #AnnoyedByMario",
                postedTime: "5 minutes ago",
              },],
          },
          {
            name: "Egbert",
            username: "@User2",
            message: "🌲🏔️ Calling all nature lovers! 🌿 Are you ready to embark on an epic hiking adventure? 🥾✨ Get rea  dy to experience the thrill of conquering breath\n" +
                "taking trails, immersing yourself in stunning landscapes, and connecting with the great outdoors like never before! 🌄🌳\n" +
                "\n" +
                "I am absolutely bursting with excitement about my upcoming hike! 😍🙌 The feeling of the warm sun on my face, the invigorating scent of fresh mountain air, and the sound of birds chirping in harmony... It's a symphony of serene beauty that ignites my soul! 💚✨\n" +
                "\n" +
                "Hiking isn't just a physical activity; it's a passionate affair with nature. 🌻🌼 As I take each step, my heart beats faster with anticipation, eager to explore hidden treasures and witness incredible sights that will leave me in awe. From cascading waterfalls to panoramic views, every turn holds a new discovery! 🌈🏞️\n" +
                "\n" +
                "Join me on this exhilarating journey and let's embrace the joy of being one with nature! 🌿🥾 Let's  create unforgettable memories, push our limits, \n" +
                "and soak up the positive energy that nature graciously offers! 🌟😃 Remember, there's no limit to the adventures we can have when we step out of our comfort zones! 🙌💫\n" +
                "\n" +
                "So, put on your hiking boots, pack your essentials, and let's embark on this incredible adventure together! 🌲👣 Get ready to experience the thrill, serenity, and pure bliss that only a hike can offer. Are you ready to experience nature's breathtaking beauty? Let's go! 🌄🌿✨ #HikingAdventure #Na\n" +
                "tureLovers #EmbraceTheJourney",
            postedTime: "1 hour ago",
            comments: [{
              username: "UserA",
              message: "Wow, your enthusiasm for hiking is contagious! 🌿🥾 I can feel the excitement radiating from your wo rds! Your description of the warm sun, fresh air\n" +
                  ", and sounds of nature is so soothing and inspiring. It's amazing how hiking allows us to connect with the beauty around us and create unforgettable memories. Can't wait to see the breathtaking views and hidden treasures you discover on your adventure! 🌄🏞️ Enjoy every step of the journey and e \n" +
                  "mbrace the joy of being one with nature! 🌲💚✨ #NatureLovers #HikingEnthusiast",
              postedTime: "10 minutes ago",
            },
              {
                username: "UserB",
                message: "Ugh, I wish I could share your enthusiasm for hiking, but it's just not my thing. The thought of sweating, bugs, and sore muscles does not sound appealing to me at all. Enjoy your hike, though! 🙄",
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

