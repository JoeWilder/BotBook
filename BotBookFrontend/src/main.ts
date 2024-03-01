import { createApp } from 'vue'
import { Quasar } from 'quasar'

// Import icon libraries
import '@quasar/extras/material-icons/material-icons.css'

// Import Quasar css
import 'quasar/src/css/index.sass'


import './style.css'
import App from './App.vue'

import router from './router/index.js'
import store from './store/store.js'

createApp(App)
    .use(router)
    .use(Quasar, {
        plugins: {}
    })
    .use(store)
    .mount('#app')
