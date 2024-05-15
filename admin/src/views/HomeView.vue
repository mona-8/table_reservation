<template>
    <div>
        <div class="background"></div>
        <div class="container center">
            <div class="row">
                <div class="content col-7">
                    <div class="fw-bolder text-light shad">Explore the best restaurants around you.
                        Hassle Free!</div>
                </div>
                <div class="content col-4">
                    <!-- <b-card overlay title="Book Now" text-variant="white" :img-src="image" style="min-width: 20rem; min-height: 10rem;">
                            <br> <br>
                            <div class="text-center">
                            <router-link to="/browse">
                                <b-button block class="mx-5" size="lg" variant="primary">Book a Table</b-button>
                            </router-link>
                            </div>
                        </b-card> -->
                    <router-link to="/browse">
                        <b-button block class="mx-5" size="lg" variant="primary">Book a Table</b-button>
                    </router-link>
                    <br> <br>
                    <router-link to="/admin">
                        <b-button block class="mx-5" size="lg" variant="primary">Admin</b-button>
                    </router-link>
    
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import image from "../assets/book.png";
export default {
  methods: {
    browse() {
      this.$router.push('/browse')
    }
  },
  data() {
    return {
      image,
    };
  }
}
</script>

<style scoped>
.bi {
    background-image: url('../assets/new.jpg');
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center center;
}

.background {
    position: absolute;
    height: 100%;
    width: 100%;
    background-image: url('../assets/new.jpg'), linear-gradient(rgba(0,0,0,0.4),rgba(0,0,0,0.4));
    background-blend-mode: overlay;
    background-size: cover;
    background-position: center;
    z-index: -1;
    overflow: hidden;
    
    opacity: 1;
}

.shad {
    text-shadow: 4px 2px 1px rgba(0, 0, 0, 0.75);
    font-size: 40px;
}

.center {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
}

.content {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
}
</style>
