<template>
    <div class="container">
    
        <div class="row">
            <div class="col-2"></div>
            <div class="adm col-8">
    
                <div class=" px-5">
                    <b-card title="REGISTER YOUR RESTAURANT" style="max-width: 50rem; " class="shadow p-2 mt-5">
                        <br>
                        <div class="pt-3 fw-medium text-muted">
                            <label for="example-datepicker">Restaurant Name</label>
                            <b-form-input v-model="rname" placeholder="Restaurant"></b-form-input>
                        </div>
    
                        <div class="pt-3 fw-medium text-muted">
                            <label for="example-datepicker">Address</label>
                            <b-form-input v-model="rlocation" placeholder="Chennai"></b-form-input>
                        </div>
    
                        <div class="pt-3 fw-medium text-muted">
                            <label for="example-datepicker">Cuisine</label>
                            <b-form-input v-model="rcuisine" placeholder="Indian"></b-form-input>
                        </div>
    
                        <div class="pt-3 fw-medium text-muted">
                            <label for="example-datepicker">Description</label>
                            <b-form-input v-model="rdescription" placeholder="How's your place?"></b-form-input>
                        </div>
    
                        <div class="pt-3 fw-medium text-muted">
                            <label for="example-datepicker">Type</label>
                            <b-form-input v-model="rtype" placeholder="Veg/Non-Veg"></b-form-input>
                        </div>
    
                        <div class="pt-3 fw-medium text-muted">
                            <label for="example-datepicker">Rating</label>
                            <b-form-input v-model="rrating" placeholder="4"></b-form-input>
                        </div>
    
                        <div class="pt-4 col-8 ms-auto">
                            <b-button @click="addRes" v-b-modal.modal-1>SUBMIT</b-button>
    
                            <b-modal id="modal-1" title="Registration successfull!">
                                <p class="my-4">Restaurant Registered Successfully</p>
                            </b-modal>
                        </div>
    
                    </b-card>
                </div>
    
            </div>
            <div class="col-2"></div>
        </div>
    </div>
</template>

<script>
import { getAPI } from '../axios-api'
export default {
  data() {
    return {
      rname: '',
      rlocation: '',
      rcuisine: '',
      rtype: '',
      rdescription: '',
      rrating: '',
    }
  },
  methods: {
    addRes() {
      getAPI.post('/addInfo/', {
        name: this.rname,
        location: this.rlocation,
        cuisine: this.rcuisine,
        type: this.rtype,
        rating: this.rrating,
        description: this.rdescription
      })
        .then(function (response) {
          console.log(response);
        })
        .catch(function (error) {
          console.log(error);
        });
    }
  }
}
</script>

<style scoped>
.container {
    margin-top: 72px;
}
</style>