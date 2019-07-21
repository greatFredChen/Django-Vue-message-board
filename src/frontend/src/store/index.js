import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)
const store = new Vuex.Store({
    state: {
        account: '',
        is_login: '',
        user_name: '',
        user_id: ''
    },
    mutations: {
        login(state, LoginUser) {
            state.account = LoginUser.account
            state.is_login = LoginUser.is_login
            state.user_name = LoginUser.username
            state.user_id = LoginUser.user_id
        },
        logout(state) {
            state.account = ''
            state.is_login = ''
            state.user_name = ''
            state.user_id = ''
        }
    },
    actions: {
        actionLogin(context, LoginUser) {
            context.commit('login', LoginUser)
        },
        actionLogout(context) {
            context.commit('logout')
        }
    }
})

export default store