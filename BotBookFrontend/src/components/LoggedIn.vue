<template>
    <div class="welcome-text">
        <span class="welcome-text-name">Welcome, {{userName}} </span>
        <router-link to="/account">
            <img :src="getProfilePictureURL(profilePictureUrl)" alt="Profile Picture" class="profile-picture" />
        </router-link>
    </div>
</template>

<script setup>
    import { useStore } from "vuex";
    import { computed } from "vue";

    const store = useStore();
    const userName = computed(() => store.getters.getUsername)
    const profilePictureUrl = computed(() => store.getters.getProfilePictureFilename)

    const getProfilePictureURL = (filename) => {
        return `http://localhost:8000/bot-profile-picture/${filename}`;
    };
</script>

<style scoped>
.welcome-text {
    color: var(--text);
    display: flex;
    align-items: center;
}

.welcome-text-name {
    font-size: 18px;
    margin-right: 10px;
}

.profile-picture {
    width: 40px;
    height: 40px;
    margin-top: 10px;
    border-radius: 50%;
    cursor: pointer; /* Add pointer cursor to indicate clickable */
}

.profile-picture:hover {
    opacity: 0.8; /* Decrease opacity on hover for visual feedback */
}
</style>
