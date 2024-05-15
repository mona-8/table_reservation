<template>
    <div class="my-4 mx-2">
        <b-card :title="restaurant.name" :img-src="image" img-alt="Image" img-top tag="article"
            style="max-width: 20rem;" class="mb-2">
            <b-card-text>
                <section class="text-muted">{{restaurant.description}}</section>
            </b-card-text>
            <router-link :to="{ name:'restaurant', params:{ id: restaurant.id }}">
                <b-button variant="primary">View More</b-button>
            </router-link>
        </b-card>
    </div>
</template>

<script>
import image from "@/assets/img1.png";
export default {
    data() {
    return {
      image
    }
  },
    props:{
        restaurant: String
    }
}
</script>