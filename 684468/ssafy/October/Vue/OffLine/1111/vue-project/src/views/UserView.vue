<template>
  <div>
    <RouterLink :to="{name: 'user-profile'}">Profile</RouterLink>
    <RouterLink :to="{name: 'user-posts'}">Posts</RouterLink>

    <h1>UserView</h1>
    <h2>{{ userId }}번 페이지 </h2>
    <button @click="goHome">Home</button>
    <button @click="routeUpdate">100번 유저의 페이지 </button>

    <!-- 중첩 라우트의 컴포넌트가 렌더링 -->
    <RouterView/>

  </div>
</template>

<script setup>
import {ref} from 'vue'
import { RouterLink, RouterView } from 'vue-router';
import { useRoute, useRouter } from 'vue-router';
//leave: 페이지 떠날 때 실행되는 가드 
//update: 페이지 url 변경될 때 실행되는 가드 
import { onBeforeRouteUpdate,onBeforeRouteLeave } from 'vue-router';


const route= useRoute()

const router = useRouter()

const userId = ref(route.params.id)

const goHome = function(){
  //router.push() : 이전페이지로 돌아갈 수 있다. 만약 A->B->C라고 하면 C에서 push하면 B로 감 . 이건 히스토리에 추가되기 때문
  //router.replace() : 이전페이지로 돌아갈 수 없다 C에서 replace하면 A로 감 . 이건 히스토리에 추가되지 않기 때문 
  router.replace({name: 'home'})
}

const routeUpdate=function(){
  router.push({name:'user',params:{id:100}})
}

onBeforeRouteLeave((to,from)=>{
  const answer = window.confirm('정말 떠날실 건가요?')
  if (answer === false){
    return false // 만약 '아니오' 할거면 페이지 이동 취소 
  }
})
//from : 1번 , to:100번
onBeforeRouteUpdate((to,from)=>{
  userId.value = to.params.id
})


</script>

<style  scoped>

</style>