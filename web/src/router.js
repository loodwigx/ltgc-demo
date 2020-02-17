import Vue from "vue";
import Router from "vue-router";

import Legal from "@/Legal.vue";

import View from "@/address-book/View.vue";
import Edit from "@/address-book/Edit.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {path: "/", name: "view", component: View},
    {path: "/legal", name: "legal", component: Legal},
    {path: "/new", name: "new", component: Edit},
    {path: "/:addressId", name: "edit", component: Edit}
  ]
});
