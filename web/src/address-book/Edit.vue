<template>
<section class="section">
  <div class="field">
    <label class="label">Name</label>
    <div class="control has-icons-left has-icons-right">
      <input type="text"
             class="input"
             placeholder="Enter Name"
             :class="className"
             v-model.lazy="name">
      <span class="icon is-small is-left">
        <i class="fas fa-user" />
      </span>
      <span v-if="!validNameRequired || !validNameUnique" class="icon is-small is-right">
        <i class="fas fa-exclamation-triangle" />
      </span>
    </div>
    <p v-if="!validNameUnique" class="help is-warning">
      This name already exists
    </p>
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
             v-model.lazy="company">
    </div>
  </div>

  <div class="field">
    <label class="label">Address</label>
    <div class="control has-icons-right">
      <input type="text"
             class="input"
             placeholder="Full Address including unit number"
             :class="classAddress"
             v-model.lazy="address">
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
             v-model.lazy="city">
      <span v-if="!validCityRequired" class="icon is-small is-right">
        <i class="fas fa-exclamation-triangle" />
      </span>
    </div>
    <div class="control">
      <div class="select">
        <select v-model="state">
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
             v-model.lazy="zip">
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
</section>
</template>
<script>
import usStates from "@/service/usStates.js";

export default {
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
        {"is-success": this.nameDirty && this.validNameRequired && this.validNameUnique},
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
    validAddressRequired() {
      if (!this.addressDirty) return true;
      return !!this.address;
    },
    validCityRequired() {
      if (!this.cityDirty) return true;
      return !!this.city;
    },
    validNameRequired() {
      if (!this.nameDirty) return true;
      return !!this.name;
    },
    validNameUnique() {
      if (!this.nameDirty) return true;
      // TODO - do we really want to do this?
      return true;
    },
    validZip() {
      if (!this.zipDirty) return true;
      // TODO - validate with endpoint to confirm zip vs city and state
      return true;
    }
  },
  data() {
    return {
      address: "",
      addressDirty: false,
      city: "",
      cityDirty: false,
      company: "",
      name: "",
      nameDirty: false,
      state: "CO",
      zip: "",
      zipDirty: false
    };
  },
  watch: {
    address() {
      this.addressDirty = true;
    },
    city() {
      this.cityDirty = true;
    },
    name() {
      this.nameDirty = true;
    },
    zip() {
      this.zipDirty = true;
    }
  }
};
</script>
<style lang="scss" scoped>

</style>
