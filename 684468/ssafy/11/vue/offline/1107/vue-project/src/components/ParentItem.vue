<template>
  <p>{{ myProp.id }}</p>
  <p>{{ myProp.name }}</p>

</template>

<script setup>
// 내려받은 props를 정의 하는법: defineProps
defineProps({
  myProp:Object
})

</script>

<style scoped>

</style>