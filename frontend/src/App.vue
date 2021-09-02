<template>
  <nav-panel
  v-for="menu in NavMenu"
  :key="menu.hello"
  >
    <h1>{{ menu.hello }}</h1>
  </nav-panel>
</template>

<script>

import NavPanel from './NavPanel'
import './reset.css'
import './style.css'


export default {
  name: 'App',
  data() {
    return {
      NavMenu: {
        hello: "hello"
      }
    }
  },
  components: {
    'nav-panel': NavPanel
  }
}
</script>

<style>
</style>
