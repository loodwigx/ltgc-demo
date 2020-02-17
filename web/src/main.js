import Vue from "vue";
import "bulma/css/bulma.css";
import App from "@/App.vue";
import router from "@/router.js";

import axios from "axios";
axios.default.baseURL = "/app";

/* eslint-disable no-new */
new Vue({
  router,
  render: (h) => h(App)
}).$mount("body");
