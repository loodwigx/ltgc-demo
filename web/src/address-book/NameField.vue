<template>
<div class="field">
  <label class="label">Name</label>
  <div class="control has-icons-left has-icons-right">
    <input type="text"
           class="input"
           placeholder="Enter Name"
           :class="inputClass"
           :value="name"
           @blur="dirty = true"
           @change="$emit('update:name', $event.target.value)">
    <span class="icon is-small is-left">
      <i class="fas fa-user" />
    </span>
    <span v-if="!valid" class="icon is-small is-right">
      <i class="fas fa-exclamation-triangle" />
    </span>
  </div>
  <p v-if="!valid" class="help is-danger">
    Name is required
  </p>
</div>
</template>

<script>

export default {
  props: {
    name: {type: String, required: true}
  },
  computed: {
    inputClass() {
      return [
        {"is-success": this.dirty && this.valid},
        {"is-danger": !this.valid}
      ];
    },
    valid() {
      if (!this.dirty) return true;
      return !!this.name;
    }
  },
  data() {
    return {
      dirty: false
    };
  }
};
</script>
