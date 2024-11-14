<template>
  
  <p>{{ myMsg }}</p>
  <p>{{ dynamicProps }}</p>

  <!-- 1번방법 -->
  <!-- $emit으로 전달 'someEvent를 부모에게 전달'-->
  <!-- <button @click="$emit('someEvent')">클릭</button> -->


  <!-- 2번방법(함수명) -->
   <button @click="buttonclick">클릭</button>

  <!-- 'emitArges'이벤트와 함께 추가 데이터(1,2,3) -->
  <button @click="emitArgs">추가 인자 전달</button>
  <ParentGrandChild
    :my-msg ="myMsg"
    @update-name="updateName"
    />


</template>

<script setup>
import ParentGrandChild from '@/components/ParentGrandChild.vue';

// 내려받은 props - defineProps 로 정의한다
// myMsg : 카멜케이스(js)
defineProps({
  myMsg: String,
  dynamicProps:String,
})

const emit = defineEmits(['someEvent','emitArgs','updateName'])

const buttonclick=function(){
  emit('someEvent')
}


// emitArges와 1,2,3 추가 데이터
const emitArgs=function(){
  emit('emitArgs', 1, 2, 3)
}

const updateName=function(){
  emit('updateName')
}
</script>
  

<style scoped>

</style>