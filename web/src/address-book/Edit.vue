<template>
<section class="section">
  <div class="field">
    <label class="label">Name</label>
    <div class="control has-icons-left has-icons-right">
      <input type="text"
             class="input"
             placeholder="Enter Name"
             :class="className"
             v-model.lazy="addr.name">
      <span class="icon is-small is-left">
        <i class="fas fa-user" />
      </span>
      <span v-if="!validNameRequired" class="icon is-small is-right">
        <i class="fas fa-exclamation-triangle" />
      </span>
    </div>
    <p v-if="!validNameRequired" class="help is-danger">
      Name is required
    </p>
  </div>

  <div class="field">
    <label class="label">Company</label>
    <div class="control">
      <input type="text"
             class="input"
             placeholder="Enter Company, if any"
             v-model.lazy="addr.company">
    </div>
  </div>

  <div class="field">
    <label class="label">Address</label>
    <div class="control has-icons-right">
      <input type="text"
             class="input"
             placeholder="Full Address including unit number"
             :class="classAddress"
             v-model.lazy="addr.address">
      <span v-if="!validAddressRequired" class="icon is-small is-right">
        <i class="fas fa-exclamation-triangle" />
      </span>
    </div>
  </div>

  <div class="field is-grouped">
    <div class="control is-expanded has-icons-right">
      <input type="text"
             class="input"
             :class="classCity"
             placeholder="City"
             v-model.lazy="addr.city">
      <span v-if="!validCityRequired" class="icon is-small is-right">
        <i class="fas fa-exclamation-triangle" />
      </span>
    </div>
    <div class="control">
      <div class="select">
        <select v-model="addr.state">
          <option v-for="st in states" :key="st.abbr" :value="st.abbr">
            {{ st.abbr }}
          </option>
        </select>
      </div>
    </div>
    <div class="control has-icons-right">
      <input type="text"
             class="input"
             placeholder="Zip"
             :class="classZip"
             v-model.lazy="addr.zip">
      <span v-if="!validZip" class="icon is-small is-right">
        <i class="fas fa-exclamation-triangle" />
      </span>
    </div>
  </div>

  <div class="field">
    <p v-if="!validAddressRequired" class="help is-danger">
      Address is required
    </p>
    <p v-if="!validCityRequired" class="help is-danger">
      City is required
    </p>
    <p v-if="!validZip" class="help is-danger">
      Zip is invalid
    </p>
  </div>

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
import usStates from "@/service/usStates.js";

export default {
  inject: ["addressSvc"],
  computed: {
    addressId() {
      return this.$route.params.addressId;
    },
    classAddress() {
      return [
        {"is-success": this.addressDirty && this.validAddressRequired},
        {"is-danger": !this.validAddressRequired}
      ];
    },
    classCity() {
      return [
        {"is-success": this.cityDirty && this.validCityRequired},
        {"is-danger": !this.validCityRequired}
      ];
    },
    className() {
      return [
        {"is-success": this.nameDirty && this.validNameRequired},
        {"is-danger": !this.validNameRequired}
      ];
    },
    classZip() {
      return [
        {"is-success": this.zipDirty && this.validZip},
        {"is-danger": !this.validZip}
      ];
    },
    states() {
      return usStates;
    },
    validated() {
      return !!(
        this.addr.address &&
        this.addr.city &&
        this.addr.name &&
        this.addr.state &&
        this.addr.zip
      );
    },
    validAddressRequired() {
      if (!this.addressDirty) return true;
      return !!this.addr.address;
    },
    validCityRequired() {
      if (!this.cityDirty) return true;
      return !!this.addr.city;
    },
    validNameRequired() {
      if (!this.nameDirty) return true;
      return !!this.addr.name;
    },
    validZip() {
      if (!this.zipDirty) return true;
      // TODO - validate with endpoint to confirm zip vs city and state
      return true;
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
      addressDirty: false,
      cityDirty: false,
      confirmDelete: false,
      error: false,
      nameDirty: false,
      zipDirty: false
    };
  },
  created() {
    this.init();
  },
  watch: {
    addressId() {
      this.init();
    },
    "addr.address"() {
      this.addressDirty = true;
    },
    "addr.city"() {
      this.cityDirty = true;
    },
    "addr.name"() {
      this.nameDirty = true;
    },
    "addr.zip"() {
      this.zipDirty = true;
    }
  },
  methods: {
    async create() {
      this.error = false;
      try {
        await this.addressSvc.postAddress(this.addr);
        this.$router.push({name: "view"});
      } catch (err) {
        this.error = true;
        console.error(err);
      }
    },
    async destroy() {
      if (this.confirmDelete) {
        await this.addressSvc.deleteAddress(this.addressId);
        this.$router.replace({name: "view"});
      } else {
        this.confirmDelete = true;
      }
    },
    async init() {
      if (this.addressId) {
        try {
          const addr = await this.addressSvc.getAddress(this.addressId);
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
      this.addressDirty = false;
      this.cityDirty = false;
      this.error = false;
      this.nameDirty = false;
      this.zipDirty = false;
    },
    async update() {
      this.error = false;
      try {
        await this.addressSvc.putAddress(this.addressId, this.addr);
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
</style>
