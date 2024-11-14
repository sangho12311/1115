<template>
<div>
  <!-- 할 일 추가할 때마다, 새로고침 막기 -->
   <!-- submit 이벤트 발생할 때마다 createTodo 함수 호출 -->
  <form @submit.prevent="createTodo(todoText)" ref="formElem">
    <!-- v-model 양방향 바인딩 -->
    <input type="text" v-model="todoText">
    <input type="submit">

  </form>
</div>
</template>

<script setup>
  import { ref } from 'vue'
  // 저장소 가져오기
  import { useCounterStore } from '@/stores/counter';

  // 인스턴스 생성. store의 state와 action 사용가능
  const store = useCounterStore()

  const todoText = ref('')
  const formElem = ref(null)

  // 할 일 추가 함수 
  const createTodo = function(todoText){

    // addTodo action을 호출
    store.addTodo(todoText)
    console.log(todoText)

    // 할 일 추가 할 때마다. 폼 초기화 
    formElem.value.reset()

  }

</script>

<style  scoped>

</style>