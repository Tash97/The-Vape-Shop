
import App from './App.vue'
import router from './router'
import "./index.css";


import { ApolloClient, InMemoryCache } from '@apollo/client/core'
import { DefaultApolloClient } from '@vue/apollo-composable'


const cache = new InMemoryCache()

const apolloClient = new ApolloClient({
  cache,
  uri: 'http://127.0.0.1:8000/graphql',
})

import { createApolloProvider } from '@vue/apollo-option'

const apolloProvider = createApolloProvider({
  defaultClient: apolloClient,
})


import { createApp, h, provide } from 'vue'

const app = createApp({
  setup() {
    provide(DefaultApolloClient, apolloClient)
  },
  render: () => h(App),
})

app.use(apolloProvider)

app.use(router)

app.mount('#app')
