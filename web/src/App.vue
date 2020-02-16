<template>
<body>
  <header>
    <h1>LTGC USPS Address Book Demo</h1>
    <router-link tag="button" class="icon fas fa-address-card" :to="{name: 'new'}" />
  </header>
  <main>
    <transition>
      <router-view class="router-view" :key="componentKey" />
    </transition>
  </main>
  <footer class="footer">
    <div class="content has-text-centered">
      <strong>USPS</strong> by Joe Rouse. There is no license, use it for anything you want,
      but hold me harmless.
    </div>
  </footer>
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

<style lang="scss" scoped>
body {
  display: flex;
  flex-direction: column;

  > header {
    flex-shrink: 0;
    padding: 1.5rem;
    display: flex;
    justify-content: space-between;

    h1 {
      font-weight: bold;
      font-size: 1.5rem;
    }

    button {
      font-size: 2rem;
      border: 0;
      color: #094e87;
      cursor: pointer;
    }
  }
}
main {
  flex: 1 1 auto;
  position: relative;

  > .router-view {
    position: absolute;
    width: 100%;
  }

  .v-enter, .v-leave-to {
    opacity: 0;
  }

  .v-enter-active {
    transition-property: opacity;
    transition-duration: 200ms;
    transition-timing-function: linear;
  }

  .v-leave-active {
    transition-property: opacity;
    transition-duration: 200ms;
    transition-timing-function: linear;
    transition-delay: 100ms;
  }
}
footer {
  flex-shrink: 0;
  padding: 1.5rem;
}
</style>
