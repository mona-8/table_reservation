<template>
    <div>
        <b-navbar type="dark" variant="dark" class="px-3 fixed-top navv">
            <b-navbar-brand href="#" class="fw-bolder " style="font-size:30px;">
                <!-- <router-link to="/">DineIn </router-link> -->
                <section style="font-family:'cursive;">Diner's Inn</section>
            </b-navbar-brand>
            <b-navbar-nav class="ms-auto">
                <!-- <b-nav-form>
                        <b-form-input size="sm" class="me-2" placeholder="Search"></b-form-input>
                        <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
                    </b-nav-form> -->
                <!-- <b-input-group class="mt-3" size="sm">
                    <b-form-input></b-form-input>
                    <b-input-group-append>
                        <b-button variant="info">Search</b-button>
                    </b-input-group-append>
                </b-input-group> -->
                 <router-link to="/login">
                <b-button class="mx-2" variant="primary">Log In</b-button>
                    </router-link>
                    <router-link to="/signup">
                <b-button class="mx-2">Sign Up</b-button>
                    </router-link>
            </b-navbar-nav>
        </b-navbar>
    
    </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.navv {
    background-color: transparent;
}
</style>