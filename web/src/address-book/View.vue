<template>
<section :class="sectionColumns">
  <address-card v-for="address in addresses"
                :key="address.id"
                :class="addressColumns"
                :addr="address" />
  <article v-if="addresses.length === 0" class="hero is-primary is-large is-bold">
    <div class="hero-body">
      <div class="container">
        <h1 class="title">
          There are no addresses on your system.
        </h1>
        <h2 class="subtitle">
          Explanation on how the DB works
        </h2>
        <router-link :to="{name: 'new'}">
          <strong>
            Click here to add a new address
          </strong>
        </router-link>
      </div>
    </div>
  </article>
</section>
</template>

<script>
import AddressCard from "@/address-book/AddressCard.vue";

export default {
  inject: ["addressSvc"],
  components: {
    AddressCard
  },
  computed: {
    addressColumns() {
      return [
        "column",
        "is-full-mobile",
        "is-half-tablet",
        "is-one-third-desktop",
        "is-one-quarter-widescreen",
        "is-one-fifth-fullhd"
      ];
    },
    sectionColumns() {
      return this.addresses.length ?
        ["columns", "is-multiline"] :
        [];
    }
  },
  data() {
    return {
      addresses: []
    };
  },
  async created() {
    this.addresses = await this.addressSvc.getAddresses();
  }
};
</script>

<style lang="scss" scoped>
.columns {
  background-image: url("/static/lines.png");
}

</style>
