<template>
    <div class="container">
        <div class="row pt-4">
            <div class="col-7 border border-light-subtle ">
                <div class="image row">
                    <img src='../assets/bg2.jpeg' alt="">
                </div>
                <div class="row">
                    <p id="title">{{this.restaurants[this.id].name}}</p>
                </div>
                <div class="row ">
                    <b-icon class="col-1 " icon="map"></b-icon>{{this.restaurants[this.id].location}}
                    <!-- <div class="col-8"></div> -->
                    <section class="col-2 ms-auto fw-bold">Rating: {{this.restaurants[this.id].rating}} </section>
                </div>
                <div class="row px-4 py-2 text-muted">
                    {{this.restaurants[this.id].cuisine}} <br>
                    {{this.restaurants[this.id].type}}
                </div>
    
    
                <!-- {{this.restaurants[this.id].img_url}} -->
            </div>
            <div class="col-5 px-5">
                <b-card title="Book Slots" style="max-width: 25rem; " class="shadow p-2 mt-5">
    
                    <div class="pt-3 fw-medium text-muted">
                        <label for="example-datepicker">Select Date</label>
                        <b-form-datepicker required :min="min" :max="max" id="example-datepicker" v-model="slot_date"
                            class="mb-2"></b-form-datepicker>
                    </div>
    
                    <div class="pt-3 fw-medium text-muted">
                        <label for="example-time">Select Dining Time</label>
                        <b-form-timepicker required hide-header id="example-time" v-model="slot_time"
                            locale="en"></b-form-timepicker>
                    </div>
    
                    <div class="pt-3 fw-medium text-muted">
                        <label for="example-count">Select No. of Diners</label>
                        <b-form-spinbutton required id="example-count" size="lg" v-model="value" min="1"
                            max="20"></b-form-spinbutton>
                    </div>
    
                    <div class="pt-4 col-8 ms-auto">
                        <b-button v-b-modal.modal-1>Book Now</b-button>
    
                        <b-modal id="modal-1" title="Table Reserved">
                            <p class="my-4">Reservation successful! 
                                Your table is awaiting you :)</p>
                        </b-modal>
                    </div>
    
                </b-card>
            </div>
        </div>
    
    </div>
</template>

<script>

import { getAPI } from '../axios-api'

export default {
  data() {
    const now = new Date()
    const today = new Date(now.getFullYear(), now.getMonth(), now.getDate())
    const maxDate = new Date(now.getFullYear(), now.getMonth() + 1, now.getDate())
    return {
      id: 0,
      restaurants: [],
      slot_date: '',
      slot_time: '',
      slot_ppl: '',
      min: today,
      max: maxDate,
      im: '../assets/bg2.jpeg',
    }
  },
  created() {
    getAPI.get('/data/')
      .then(response => {
        this.restaurants = response.data
      })
      .catch(error => {
        console.log(error);
      })

  },
  mounted() {
    this.id = (this.$route.params.id) - 1;
  }
}

</script>

<style scoped>
.container {
    margin-top: 72px;
}

img {
    height: 300px;
    padding-top: 10px;
}

#title {
    font-size: 30px;
    padding: 10px 0 0 20px;
    font-weight: bolder;
}
</style>