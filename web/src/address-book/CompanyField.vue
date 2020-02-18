<template>
<div class="field">
  <label class="label">Company</label>
  <div class="control">
    <input type="text"
           class="input"
           placeholder="Enter Company, if any"
           :value="company"
           @change="$emit('update:company', $event.target.value)">
  </div>
</div>
</template>

<script>

export default {
  props: {
    company: {type: String, required: true}
  }
};
</script>
