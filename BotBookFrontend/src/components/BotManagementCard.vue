<template>
    <div class="bot-card">
      <div class="bot-header">
        <div class="header-left">
          <img src="../assets/ProfilePictures/justinperkins.jpg" class="profile-picture" alt="Profile Picture">
          <div>
            <p class="bot-name">{{ truncateName(bot.name, 11) }}</p>
            <p class="creation-date">{{ bot.creationDate }}</p>
          </div>
        </div>
        <div class="header-right">
          <q-icon name="more_vert" class="icon-more"></q-icon>
        </div>
      </div>
      <div class="bot-content">
        <div class="interests-container">
          <template v-if="bot.interests && bot.interests.length > 0">
            <div v-for="(interest, index) in bot.interests" :key="index" class="interest">
              <div class="info-value">{{ truncateName(interest, 60) }}</div>
            </div>
          </template>
          <template v-else>
            <div class="no-interests">
              <p>This bot does not have any interests</p>
              <q-icon name="sentiment_very_dissatisfied" class="sad-icon"></q-icon>
            </div>
          </template>
        </div>
      </div>
      <div class="bot-menu">
        <q-btn label="Configure Bot" color="indigo-4" @click="editbot"/>
        <!-- Add more buttons or actions as needed -->
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      bot: {
        type: Object,
        required: true
      }
    },
    methods: {
      editBot() {
        // Implement edit bot logic
      },
      deleteBot() {
        // Implement delete bot logic
      },
      truncateName(name, length) {
        return name.length > length ? name.slice(0, length) + '...' : name;
      }
    }
  }
  </script>
  
  <style scoped>
  .bot-card {
    border: 1px solid var(--sidebar-highlight);
    border-radius: 10px;
    padding: 10px;
    margin: 10px;
    width: 93%;
    height: 300px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    transition: background-color 0.3s ease;
    overflow: hidden;
  }
  
  .bot-content {
    display: flex;
    justify-content: center;
    flex: 1;
  }
  
  .bot-card:hover {
    background-color: var(--text-bubble-hover);
  }
  
  .bot-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
  }
  
  .header-left {
    display: flex;
    align-items: flex-start;
  }
  
  .profile-picture {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    margin-right: 10px;
  }
  
  .bot-name {
    font-size: 1.5em;
    font-weight: bold;
    margin: 0;
  }
  
  .creation-date {
    font-size: 0.8em;
    color: #777;
  }
  
  .header-right {
    display: flex;
    align-items: center;
    margin-left: auto;
  }
  
  .icon-more {
    font-size: 1.5em;
    color: #777;
    cursor: pointer;
  }
  
  .interests-container {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    flex-grow: 1; /* Allow container to grow */
  }
  
  .interest {
    border-radius: 20px;
    font-size: 0.9em;
    padding: 5px;
    overflow: hidden;
    line-height: 1.1em; /* Set line height */
    width: 100%; /* Take up maximum width */
  }
  
  .no-interests {
    padding: 5px;
    text-align: center;
  }
  
  .sad-icon {
    font-size: 2em;
    color: var(--error);
  }
  
  .bot-menu {
    margin-top: 10px; /* Add margin to separate from interests */
    text-align: center;
  }
  
  .info-value {
    background-color: var(--app-side-divider);
    padding: 8px;
    border-radius: 5px;
  }
  </style>
  