import Vue from "vue";
import Router from "vue-router";

import View from "@/address-book/View.vue";
import Edit from "@/address-book/Edit.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {path: "/", name: "view", component: View},
    {path: "/new", name: "new", component: Edit},
    {path: "/:addressId", name: "edit", component: Edit}
  ]
});
