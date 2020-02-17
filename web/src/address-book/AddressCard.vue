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
          <p class="subtitle">
            {{ addr.company }}
            &nbsp;
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

.media-content {
  overflow: hidden;
}

p.title {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  line-height: 1.35;
}
</style>
