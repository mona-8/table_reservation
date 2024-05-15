<template>
  <div id="app">
    <NavbarComp/>
    <router-view />
  </div>
</template>

<script>
import NavbarComp from './components/NavbarComp.vue'
export default {
  data() {
    return {
    }
  },
  components: {
    NavbarComp
  },
}
</script>

<style>

</style>
