<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Ready to buy?</h1>
        <hr>
        <router-link to="/movies" class="btn btn-primary">
          Back Home
        </router-link>
        <br><br><br>
        <div class="row">
          <div class="col-sm-6">
            <div>
              <h4>You are buying:</h4>
              <ul>
                <li>Book Title: <em>{{ movie.title }}</em></li>
                <li>Genre: <em>{{ movie.genre }}</em></li>
              </ul>
            </div>
            <div>
              <h4>Use this info for testing:</h4>
              <ul>
                <li>Card Number: 4242 4242 4242 4242</li>
                <li>CVC Code: any three digits</li>
                <li>Expiration: any date in the future</li>
              </ul>
            </div>
          </div>
          <div class="col-sm-6">
            <h3>One time payment</h3>
            <br>
            <form>
              <div class="form-group">
                <label>Credit Card Info</label>
                <input type="text"
                       class="form-control"
                       placeholder="XXXXXXXXXXXXXXXX"
                       v-model="card.number"
                       required>
              </div>
              <div class="form-group">
                <input type="text"
                       class="form-control"
                       placeholder="CVC"
                       v-model="card.cvc"
                       required>
              </div>
              <div class="form-group">
                <label>Card Expiration Date</label>
                <input type="text"
                       class="form-control"
                       placeholder="MM/YY"
                       v-model="card.exp"
                       required>
              </div>
              <button class="btn btn-primary btn-block" v-on:click="createToken">Submit</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios';

    export default {
      name: "Order",
      data(){
        return {
          movie:{
            title: '',
            genre: '',
            year:'',
          },
          card:{
            number:'',
            cvc:'',
            exp:''
          },
         STRIPE_PUBLISHABLE_KEY:'pk_test_9q1AuOJreMih2aojbwteRUX800ZVe64g6f'
        }
      },
      methods:{
        getMovie(){
          const path = `http://0.0.0.0:8000/api/v1/movies/${this.$route.params.id}/`;
          axios.get(path)
            .then((res) => {
              this.movie = res.data
            });
          },
        createToken() {
          window.Stripe.setPublishableKey(this.STRIPE_PUBLISHABLE_KEY);
          window.Stripe.createToken(this.card, (status, response)=> {
              const payload = {
              movie: this.movie.title,
              token: response.id,
            };
            const path = 'http://0.0.0.0:8000/api/v1/payment/charge/';
            axios.post(path, payload).then(() => {
              this.$router.push({ path: '/movies' });
        })
          });
      },
      },
      created() {
          this.getMovie();
      },
    };
</script>

<style scoped>

</style>
