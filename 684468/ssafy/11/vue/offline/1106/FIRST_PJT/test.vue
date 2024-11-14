<!-- SFC
Single File Components -->


<!-- html코드 -->
<template>
  <div class="greeting">
    {{msg}}


  </div>

</template>

<script setup>
import {ref} from 'vue'

const msg = ref('Hello World')

//return

</script>
<!-- css코드 
scope 이 파일에서 작성하는 style은 이 파일의 템플릿에서만 적용된다 -->
<style  scoped>
  .greeting{
    color : crimson
  }

</style>