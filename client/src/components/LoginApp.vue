<template>
<div>
  <button type="button" class="btn btn-success btn-sm" v-b-modal.login-modal>Login</button>
  <div>
    <b-modal id="login-modal" ref="loginForm" hide-footer>
      <b-form @submit="onSubmit" class="w-100">
      <b-form-group id="form-email-group"
                    label="Email:"
                    label-for="form-email-input">
          <b-form-input id="form-email-input"
                        type="text"
                        v-model="loginForm.email"
                        required
                        placeholder="Enter email">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-password-group"
                      label="Password:"
                      label-for="form-password-input">
            <b-form-input id="form-password-input"
                          type="text"
                          v-model="loginForm.password"
                          required
                          placeholder="Enter password">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-read-group">
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</div>
</template>

<script>
  import axios from 'axios';
    export default {
      name: "LoginApp",
      data() {
        return {
          loginForm: {
            email: '',
            password: '',
          },
        };
      },
      methods: {
        login(payload) {
          const path = 'http://0.0.0.0:8000/api/v1/login/';
          axios.post(path, payload)
        },
        onSubmit(evt) {
          evt.preventDefault();
          this.$refs.loginForm.hide();
          const payload = {
            email: this.loginForm.email,
            password: this.loginForm.password,
          };
          this.login(payload)
        },
      },
    };
</script>

<style scoped>

</style>
