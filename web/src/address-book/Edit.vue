<template>
<section class="section">
  <name-field :name.sync="addr.name" />
  <company-field :company.sync="addr.company" />
  <address-field :address.sync="addr.address"
                 :city.sync="addr.city"
                 :state.sync="addr.state"
                 :zip.sync="addr.zip"
                 @setError="error = true" />

  <div class="field is-grouped">
    <div v-if="addressId" class="control">
      <button class="button is-link" :disabled="!validated" @click="update">
        Save
      </button>
    </div>
    <div v-else class="control">
      <button class="button is-link" :disabled="!validated" @click="create">
        Create
      </button>
    </div>
    <div class="control">
      <router-link tag="button" class="button is-link is-light" :to="{name: 'view'}">
        Cancel
      </router-link>
    </div>
    <div v-if="addressId" class="control go-right">
      <button v-if="confirmDelete" class="button is-danger" @click="destroy">
        Confirm Delete
      </button>
      <button v-else class="button is-danger" @click="destroy">
        Delete
      </button>
    </div>
  </div>

  <div v-if="confirmDelete" class="notification is-warning">
    <button class="delete" @click="confirmDelete = false" />
    Are you sure you want to delete "{{ addr.name }}?" This cannot be undone, and you'll no longer
    be able to send them a post card from your fabulous road trip to Maui or Plano. That is, unless
    you have their address memorized or don't care much for post cards, in which case please, go
    nuts.
  </div>

  <div v-if="error" class="notification is-danger">
    <button class="delete" @click="error = false" />
    An error occurred when attempting to write to the back end. Since this is a demo, it's likely
    a bug in the code, in which case... whoopsie!
  </div>
</section>
</template>
<script>
import addressSvc from "@/service/addressSvc.js";

import AddressField from "@/address-book/AddressField.vue";
import CompanyField from "@/address-book/CompanyField.vue";
import NameField from "@/address-book/NameField.vue";

export default {
  components: {
    AddressField,
    CompanyField,
    NameField
  },
  computed: {
    addressId() {
      return this.$route.params.addressId;
    },
    validated() {
      return !!(
        this.addr.address &&
        this.addr.city &&
        this.addr.name &&
        this.addr.state &&
        this.addr.zip
      );
    }
  },
  data() {
    return {
      addr: {
        address: "",
        city: "",
        company: "",
        name: "",
        state: "CO",
        zip: ""
      },
      confirmDelete: false,
      error: false,
      nameDirty: false
    };
  },
  created() {
    this.init();
  },
  watch: {
    addressId() {
      this.init();
    }
  },
  methods: {
    async create() {
      this.error = false;
      try {
        await addressSvc.postAddress(this.addr);
        this.$router.push({name: "view"});
      } catch (err) {
        this.error = true;
        console.error(err);
      }
    },
    async destroy() {
      if (this.confirmDelete) {
        await addressSvc.deleteAddress(this.addressId);
        this.$router.replace({name: "view"});
      } else {
        this.confirmDelete = true;
      }
    },
    async init() {
      if (this.addressId) {
        try {
          const addr = await addressSvc.getAddress(this.addressId);
          this.addr = addr;
        } catch (err) {
          this.$router.replace({name: "new"});
        }
      } else {
        this.addr = {
          address: "",
          city: "",
          company: "",
          name: "",
          state: "CO",
          zip: ""
        };
      }
      this.error = false;
    },
    async update() {
      this.error = false;
      try {
        await addressSvc.putAddress(this.addressId, this.addr);
        this.$router.push({name: "view"});
      } catch (err) {
        this.error = true;
        console.error(err);
      }
    }
  }
};
</script>
<style lang="scss" scoped>
.go-right {
  margin: 0 0 0 auto;
}
p.help::v-deep {
  padding: 0.25rem 0.25rem 0.25rem 1rem;
  border-radius: 0.25rem;
}
</style>
