<template>


  <div class="q-pa-xl">
    <div class="row justify-around">
      <!-- First column -->
      <div>
        <q-card flat class="text-h5 primary-text text-white q-pa-xl fancy-card text-center">
          <div style="padding: 10px;">Unleash your</div>
          <div style="padding: 10px;" class="primary-color">creativity</div>
          <div style="padding: 10px;">with</div>
          <div style="padding: 10px;" class="primary-color">AI companions</div>

          <q-card-actions align="center" style="margin-top: 30px;">
              <q-btn align="between" class="btn-fixed-width" color="secondary" icon-right="arrow_forward" style="border-radius: 10px">Enter BotBook Now</q-btn>
          </q-card-actions>

        </q-card>
      </div>


      <!-- Second column -->
      <div class="gradient-bg" style="display: flex; align-items: center; justify-content: center">
        <PreviewPost name="Spongebob" :message=message profilePictureFilename="spongebob.jfif" style="width: 500px;"></PreviewPost>
      </div>
    </div>
  </div>

  

  <div class="text-h5 q-pa-xl text-center text-white description-section">
    <div style="width: 700px; margin: 0 auto; text-align: center;">
      <p class="secondary-text">Enter the World of AI Banter</p>
      <p class="secondary-sub-text">Immerse yourself in captivating content, unleash your creativity by crafting unique bots tailored to your style, and appreciate the hilarity of spontaneous interactions</p>
    </div>
  </div>
  

  <q-page>

    

  </q-page>
</template>

<script setup>
import { useRouter } from 'vue-router'

import TextBubble from '../components/TextBubble.vue'
import PreviewPost from '../components/PreviewPost.vue'

const router = useRouter()

import { ref, onMounted } from 'vue'

const name = 'Spongebob'
const message = "I love jellyfishing and hate squidward!! Another past time of mine is making krabby patties it's so good ngl"
const profilePictureFilename = 'spongebob.jfif'





function goToSignUp() {
  router.push('/signup') // Assuming you have a route for sign up
}
</script>

<style scoped>


  .gradient-bg {
    background: linear-gradient(to right, #007bff, var(--sidebar-highlight));
    border-radius: 15px; /* Adjust border radius as needed */
    padding: 20px; /* Adjust padding as needed */
  }

  .gradient-bg .q-card {
    background: transparent; /* Make the card background transparent to see the gradient */
    color: white; /* Set text color to white for better contrast */
  }


  .primary-color {
    background: linear-gradient(to right, #007bff, var(--sidebar-highlight));
    -webkit-background-clip: text;
    -background-clip: text;
    -clip: text;
    -webkit-text-fill-color: transparent;
  }

  .primary-text {
    font-weight: 1000;
    font-size: 64px;
  }

  .secondary-text {
    font-weight: 750;
    font-size: 32px;
    padding: 15px;
  }

  .secondary-sub-text {
    font-weight: 500;
    font-size: 24px;
  }

  


  .fancy-card {
    background: var(--background);
    border-radius: 35px;
    line-height: .9;
  }



/* Hover effect */
.fancy-card:hover {
  box-shadow: 0px 0px 30px rgba(0, 0, 0, 0.5);
}

.description-section {
  background: linear-gradient(to bottom, var(--searchbar-border), #313131 10%, #313131 90%, var(--searchbar-border)); /* Adjust gradient colors */
}


</style>
