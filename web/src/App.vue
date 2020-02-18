<template>
<body>
  <header class="has-text-white-bis">
    <h1>LTGC USPS Address Book Demo</h1>
    <router-link tag="button" class="button is-link is-light is-medium" :to="{name: 'new'}">
      <span class="icon">
        <i class="fas fa-address-card" />
      </span>
      <span>Create New Address</span>
    </router-link>
  </header>
  <main>
    <transition>
      <router-view class="router-view" :key="componentKey" />
    </transition>
  </main>
  <footer class="footer has-background-dark has-text-light">
    <div class="content has-text-centered">
      <strong class="has-text-white-bis">USPS</strong> by Joe Rouse.
      <router-link :to="{name: 'legal'}">
        Legal Info
      </router-link>
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
    background-color: var(--ltgc-blue);

    h1 {
      font-weight: bold;
      font-size: 1.5rem;
    }

    button {
      font-size: 2rem;
      border: 0;
      margin-left: 1rem;
      color: var(--ltgc-blue);
      cursor: pointer;
    }
  }
}
main {
  flex: 1 1 auto;
  position: relative;
  background-color: var(--main-background-color);

  > .router-view {
    position: absolute;
    width: 100%;
    height: 100%;
    overflow-y: auto;
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

  a:hover {
    color: var(--footer-link-hover-color);
  }
}
</style>
