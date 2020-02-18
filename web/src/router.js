import Vue from "vue";
import Router from "vue-router";

import Legal from "@/Legal.vue";

import AddressList from "@/address-book/AddressList.vue";
import AddressEditor from "@/address-book/AddressEditor.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {path: "/", name: "view", component: AddressList},
    {path: "/legal", name: "legal", component: Legal},
    {path: "/new", name: "new", component: AddressEditor},
    {path: "/:addressId", name: "edit", component: AddressEditor}
  ]
});
