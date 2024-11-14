<template>
  <!-- "message"를 자식에게 전달하는 정적 props -->
   <!-- name 변수를 자식에게 전달하는 동적 props -->
    <!-- my-msg : 케밥 케이스(HTML 속성) -->
  <ParentChild 
  @some-event="someCallback"
  @emit-arges="getNumbers"
  @update-name="updateName"
  my-msg="message"
  :dynamic-props="name"
  />

  <ParentItem
  v-for="item in items"
  :key="item.id"
  :my-prop="item"
  
  />

  
</template>

<script setup>
import {ref} from 'vue'
import ParentChild from '@/components/ParentChild.vue';
import ParentItem from '@/components/ParentItem.vue';

const name = ref('Bob')

const items = ref([
  {id:1, name:'사과'},
  {id:2, name:'바나나'},
  {id:3, name:'딸기'},
])
const getNumbers=function(...args){
  alert(`ParentChildrk 발신한 추가인자${args}수신했다.`)
}

const someCallback=function(){
  alert('ParentChild가 발신한 이벤트를 수신')
}

const updateName=function(){
  name.value='Bella'
}

</script>

<style scoped>

</style>