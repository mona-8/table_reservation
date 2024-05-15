<template>
    <div class="container">
        <div class="row">
            <div class="col-xl-4 col-md-6" v-for="restaurant of restaurants" :key=restaurant.id>
                <PreviewComp :restaurant="restaurant" />
            </div>
        </div>
    </div>
</template>

<script>

import PreviewComp from '../components/PreviewComp.vue'
import {getAPI} from '../axios-api'

export default {
  data() {
    return {
      restaurants:[]
    }
  },
  components: {
    PreviewComp
  },
  props: ["restaurant"],
  created(){
    getAPI.get('/data/')
    .then(response=>{
      console.log(response.data)
      this.restaurants = response.data
    })
    .catch(error => {
      console.log(error);
    })
  }
}
</script>

<style scoped>
.container {
    margin-top: 72px;
}
</style>
