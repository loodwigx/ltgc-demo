<template>
<article>
  <div class="card">
    <div class="card-content">
      <div class="media">
        <div class="media-left">
          <figure class="image is-64x64">
            <img src="static/home64.png" alt="">
          </figure>
        </div>
        <div class="media-content">
          <p class="title">
            <router-link :to="{name: 'edit', params: { addressId: addr.address_id }}">
              {{ addr.name }}
            </router-link>
          </p>
          <p v-if="addr.company" class="subtitle">
            {{ addr.company }}
          </p>
        </div>
      </div>
      <div class="content">
        {{ addr.address }}
        <br>
        {{ addr.city }}, {{ addr.state }} {{ addr.zip }}
      </div>
    </div>
  </div>
</article>
</template>
<script>
export default {
  props: {
    addr: {type: Object, required: true}
  }
};
</script>

<style lang="scss" scoped>

.card {
  border-radius: 0.5rem;
}

p.title {
  overflow: hidden;
}
</style>
