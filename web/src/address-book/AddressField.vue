<template>
<div>
  <div class="field">
    <label class="label">Address</label>
    <div class="control has-icons-right">
      <input type="text"
             class="input"
             placeholder="Full Address including unit number"
             :class="classAddress"
             :value="address"
             @blur="addressDirty = true"
             @change="$emit('update:address', $event.target.value)">
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
             :value="city"
             @blur="cityDirty = true"
             @change="$emit('update:city', $event.target.value)">
      <span v-if="!validCityRequired" class="icon is-small is-right">
        <i class="fas fa-exclamation-triangle" />
      </span>
    </div>
    <div class="control">
      <div class="select">
        <select @change="$emit('update:state', $event.target.value)">
          <option v-for="st in states" :key="st.abbr" :value="st.abbr" :selected="state === st.abbr">
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
             :value="zip"
             @blur="zipDirty = true"
             @change="$emit('update:zip', $event.target.value)">
      <span v-if="!validZip" class="icon is-small is-right">
        <i class="fas fa-exclamation-triangle" />
      </span>
    </div>
  </div>

  <div class="field">
    <p v-if="uspsMessage" class="help has-background-warning">
      {{ uspsMessage }}
    </p>
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
</div>
</template>

<script>
import uspsSvc from "@/service/uspsSvc.js";
import usStates from "@/service/usStates.js";

export default {
  props: {
    address: {type: String, required: true},
    city: {type: String, required: true},
    state: {type: String, required: true},
    zip: {type: String, required: true}
  },
  computed: {
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
    validZip() {
      if (!this.zipDirty) return true;
      return this.zipOk && Number.isInteger(parseInt(this.zip));
    }
  },
  data() {
    return {
      addressDirty: false,
      cityDirty: false,
      uspsMessage: "",
      zipDirty: false,
      zipOk: true
    };
  },
  watch: {
    address() {
      this.addressDirty = true;
      this.fillInZip();
    },
    city() {
      this.cityDirty = true;
      this.fillInZip();
    },
    state() {
      this.fillInZip();
    },
    zip() {
      this.zipDirty = true;
      this.zipOk = true;
      this.fillInCityState();
    }
  },
  methods: {
    async fillInCityState() {
      if (Number.isInteger(parseInt(this.zip)) && !this.city) {
        try {
          this.uspsMessage = "Validating with USPS";
          const data = await uspsSvc.getCityState(this.zip);
          if (data) {
            if (data.error) {
              this.zipOk = false;
              this.uspsMessage = data.error;
            } else {
              this.uspsMessage = "";
              this.city = data.city.toLowerCase()
                  .split(" ")
                  .map((n) => n.charAt(0).toUpperCase() + n.slice(1))
                  .join(" ");
              this.state = data.state.toUpperCase();
              this.uspsMessage = "";
            }
          }
        } catch (err) {
          this.uspsMessage = "";
          this.$emit("setError");
          console.error(err);
        }
      }
    },
    async fillInZip() {
      if (this.address && this.city) {
        try {
          this.uspsMessage = "Validating with USPS";
          const data = await uspsSvc.getZip(this.address, this.city, this.state);
          if (data) {
            if (data.error) {
              this.uspsMessage = data.error;
            } else {
              this.zip = data.zip;
              this.uspsMessage = "";
            }
          }
        } catch (err) {
          this.uspsMessage = "";
          this.$emit("setError");
          console.error(err);
        }
      }
    }
  }
};
</script>
