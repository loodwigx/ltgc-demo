<template>
<section class="section">
  <div class="container has-background-white">
    <p>
      This is free and unencumbered software released into the public domain.
    </p>
    <p>
      Anyone is free to copy, modify, publish, use, compile, sell, or
      distribute this software, either in source code form or as a compiled
      binary, for any purpose, commercial or non-commercial, and by any
      means.
    </p>

    <p>
      In jurisdictions that recognize copyright laws, the author or authors
      of this software dedicate any and all copyright interest in the
      software to the public domain. We make this dedication for the benefit
      of the public at large and to the detriment of our heirs and
      successors. We intend this dedication to be an overt act of
      relinquishment in perpetuity of all present and future rights to this
      software under copyright law.
    </p>
    <p>
      THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
      EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
      MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
      IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
      OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
      ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
      OTHER DEALINGS IN THE SOFTWARE.
    </p>

    <p>
      For more information, please refer to
      <a href="http://unlicense.org/">&lt;http://unlicense.org/&gt;</a>
    </p>
  </div>

  <router-link tag="button" class="button is-link" :to="{name: 'view'}">
    <span class="icon">
      <i class="fas fa-address-book" />
    </span>
    <span>Neato. Now let's go back to the address book</span>
  </router-link>
</section>
</template>

<style lang="scss" scoped>
p {
  margin: 0.5rem;
}
button {
  float: right;
}

.container {
  padding: 0.5rem;
  border-radius: 0.5rem;
  margin-bottom: 2rem;
}

</style>
