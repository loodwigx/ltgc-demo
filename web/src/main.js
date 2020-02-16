import Vue from "vue";
import "bulma/css/bulma.css";
import App from "@/App.vue";
import router from "@/router.js";

import addressSvc from "@/service/addressSvc.js";

const services = {
  addressSvc
};

/* eslint-disable no-new */
new Vue({
  router,
  provide: services,
  render: (h) => h(App)
}).$mount("body");
