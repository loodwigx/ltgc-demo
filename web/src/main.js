import Vue from "vue";
import App from "@/App.vue";
import router from "@/router.js";

const services = {};

/* eslint-disable no-new */
new Vue({
  router,
  provide: services,
  render: (h) => h(App)
}).$mount("body");
