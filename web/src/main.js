import Vue from "vue";
import "bulma/css/bulma.css";
import App from "@/App.vue";
import router from "@/router.js";

import addressSvc from "@/service/addressSvc.js";
import uspsSvc from "@/service/uspsSvc.js";

const services = {
  addressSvc,
  uspsSvc
};

/* eslint-disable no-new */
new Vue({
  router,
  provide: services,
  render: (h) => h(App)
}).$mount("body");
