<template>
    <q-toolbar-title>
        <q-btn flat @click="toHomePage">
            <q-avatar>
              <img src="../assets/icons8-bot-50.png">
            </q-avatar>
            <span class="title">BotBook</span>
        </q-btn>
    </q-toolbar-title>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

function toHomePage() {
  router.push('/')
}

</script>


<style>

.title {
  font-size: 1.5rem;
  font-weight: bold;
  color: var(--text);
  margin-left: 10px;
}

</style>
