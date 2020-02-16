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
            John Smith
          </p>
        </div>
      </div>
      <div class="content">
        123 Fake St. Apt Y
        <br>
        Denver, CO 80000
      </div>
    </div>
  </div>
</article>
</template>
<script>
export default {
  props: {
    address: {type: Object, required: true}
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
