<template>
    <div class="start">
    <v-app-bar app dark style="background-color: #640726;">
    <v-spacer></v-spacer>
      <v-toolbar-title style="font-family: 'YourFont', sans-serif;">WELCOME TO MESS MANAGEMENT SYSTEM</v-toolbar-title>
    <v-spacer></v-spacer>
    </v-app-bar>
        <div id="container">
            <div id="box">
                <div class="pt-3 fw-medium text-muted">
                        <label for="example-datepicker">Name</label>
                        <b-form-input v-model="text" placeholder="Your Name"></b-form-input>
                </div>
                <br>
                <div class="pt-3 fw-medium text-muted">
                        <label for="example-datepicker">Email</label>
                        <b-form-input v-model="text" placeholder="Your Email"></b-form-input>
                </div>
                <br>
                <div class="pt-3 fw-medium text-muted">
                        <label for="example-datepicker">Password</label>
                        <b-form-input v-model="text" > <b>........</b></b-form-input>
                </div>
                <br><br><br>
                                    <div class="pt-4 col-8 ms-auto">
                        <b-button v-b-modal.modal-1>Sign up Now</b-button>
    
                        <b-modal id="modal-1" title="Registration successfull!">
                            <p class="my-4">Your account was created successfully</p>
                        </b-modal>
                    </div>
                <br>
            </div>
        </div>
    </div>
</template>

<!-- <script>
import axios from 'axios'
export default {
  name: "Login",
  data() {
    return {
      rollno: '',
      password:'',
      wrong: false,
    }
  },
  methods: {
    updateRollno() {
      this.$store.dispatch('updateRollno', this.rollno);
      console.log(this.rollno)
    },
    goToRegistration(){
        this.$router.push('/reg');
    },
    checkCred(){
    const path = 'http://127.0.0.1:5000/login'
    axios.post(path,{rollnumber:this.rollno,password:this.password},{
        headers: {
          'Content-Type': 'application/json'
        }
      }).then(response => {
        console.log(response)
        if(response.data){
            this.$router.push('/home');
        }else{
            this.wrong = true
        }
      }).catch(err => {
        console.log(err);
      });

    }
  }
}
</script> -->

<style scoped>
#container {
    background-color: rgb(255, 255, 255);
    display: flex;
    justify-content: center;
    align-items: center;
    height: 90vh;
    width: 100vw;
}

#box {
    background-color: rgb(241, 241, 241);
    height: 500px;
    width: 500px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

}

#textbox {
    border: solid rgb(95, 92, 92) 1px;
    width: 300px;
    height: 30px;
    padding-left: 5px;
}

#btn {
    border: solid rgb(14, 52, 14);
    color: rgb(44, 8, 8);
    background-color: bisque;
    padding: 3px;
}
</style>