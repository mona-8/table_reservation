<template>
    <div>
        <div class="container">
            <div class="row">
                <div class="col-xl-4 col-md-6" >
                    <b-card title="FOOD" img-src="" 
                        style="max-width: 20rem;" class="mb-2">
                        <b-card-text>
                            Food for your pets
                        </b-card-text>
                        <router-link to="/food">
                            <b-button variant="primary">View More</b-button>
                        </router-link>
                    </b-card>
                </div>
                <div class="col-xl-4 col-md-6" >
                    <b-card title="CLOTHES" img-src="" 
                        style="max-width: 20rem;" class="mb-2">
                        <b-card-text>
                            Clothes for your pets
                        </b-card-text>
                        <router-link to="/cloths">
                            <b-button variant="primary">View More</b-button>
                        </router-link>
                    </b-card>
                </div>
                <div class="col-xl-4 col-md-6" >
                    <b-card title="SHELTER" img-src="" 
                        style="max-width: 20rem;" class="mb-2">
                        <b-card-text>
                            Shelter for your pets
                        </b-card-text>
                        <router-link to="/shelter">
                            <b-button variant="primary">View More</b-button>
                        </router-link>
                    </b-card>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  data() {
    return {
    }
  },
}
</script>
