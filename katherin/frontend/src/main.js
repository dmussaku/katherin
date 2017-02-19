import Vue from 'vue'
import App from './App.vue'
import Blog from './apps/blog/Blog.vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  base: __dirname,
  routes: [
    { path: '/', component: Blog }
  ]
})

// Start the app on the #app div

new Vue({
	router,
  el: '#app',
  template: '<App/>',
  render: h => h(App),
})