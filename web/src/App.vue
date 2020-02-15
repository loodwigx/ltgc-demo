<template>
  <body>
    <transition>
      <router-view class="router-view" :key="componentKey" />
    </transition>
  </body>
</template>

<script>
export default {
  computed: {
    componentKey() {
      const routeKey = this.$route.meta.routeKey;
      return routeKey ? routeKey(this.$route) : "";
    }
  }
};
</script>

<style lang=scss scoped>

</style>
