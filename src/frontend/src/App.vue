<template>
  <div id="app">
    <LoginPage v-if="this.$store.state.is_login!='1'"></LoginPage>
    <messageIndexPage v-else></messageIndexPage>
  </div>
</template>

<script>
    import LoginPage from './components/login.vue'
    import messageIndexPage from './components/messageIndex.vue'
    export default {
        name: 'app',
        components: {
            LoginPage,
            messageIndexPage
        },
        created() {
            if (sessionStorage.getItem("username") && sessionStorage.getItem("account")) {
                let temp = {
                    account: sessionStorage.getItem("account"),
                    is_login: sessionStorage.getItem("is_login"),
                    username: sessionStorage.getItem("username"),
                    user_id: sessionStorage.getItem("user_id")
                }
                this.$store.dispatch("actionLogin", temp)
            }
        }
    }
</script>

<style>
    #app {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
    }
</style>