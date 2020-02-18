<template>
<section class="section">
  <div :class="sectionColumns">
    <address-card v-for="address in addresses"
                  :key="address.id"
                  :class="addressColumns"
                  :addr="address" />
    <article v-if="addresses.length === 0" class="hero is-medium">
      <div class="hero-body">
        <div class="container">
          <h1 class="title">
            There are no addresses on your system.
          </h1>
          <h2 class="subtitle">
            The Python Backend utilizes SQLite as a file system database. Addresses should be
            persisted there, even if the back end is restarted.
          </h2>
          <router-link :to="{name: 'new'}">
            <strong>
              Click here to add a new address
            </strong>
          </router-link>
        </div>
      </div>
    </article>
  </div>
</section>
</template>

<script>
import AddressCard from "@/address-book/AddressCard.vue";
import addressSvc from "@/service/addressSvc.js";

export default {
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
    this.addresses = await addressSvc.getAddresses();
  }
};
</script>

<style lang="scss" scoped>
.hero {
  background-color: var(--hero-background-color);
  background: url("/static/Land-Title-hero-home-page1.jpg") center no-repeat;
  border-radius: 0.25rem;

  .container {
    background-color: var(--hero-overlay-color);
    backdrop-filter: blur(3px);
    padding: 0.5rem;
    border-radius: 0.5rem;
  }
}

</style>
