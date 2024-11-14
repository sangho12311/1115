import { ref, computed, queuePostFlushCb } from 'vue'
import { defineStore } from 'pinia'
// defineStore:pinia의 저장소를 정의 'counter' : 저장소 명 
export const useCounterStore = defineStore('counter', () => {

//=======  state  영역=========== 반응형 상태(데이터)
//할 일 게시글의 id
let id = 0
// 할 일 목록 todo
const todos =ref([])

// ======= action 영역 ======== (메서트)
// todoText : 사용자가 입력한 게시글
// create 함수 
const addTodo = function(todoText){
  todos.value.push({
    id:id++,
    text: todoText,
    isDone: false //할 일의 완료 여부 
  })
}
const deleteTodo = function(todoId){
  // findIndex() : 조건에 맞는 첫 번째 요소의 인덱스 반환
  // splice(index, 1): index번째 1개의 항목 제거
  const index = todos.value.findIndex((todo)=>todo.id === todoId)
  todos.value.splice(index,1)
}

const updateTodo = function(todoId){
  // map():배열의 각 요소 순회하면서 새로운 배열을 만드는 메서드
  todos.value = todos.value.map((todo)=>{
    if(todo.id === todoId){
      // false -> ture, true -> false 
      todo.isDone = !todo.isDone
    }
    return todo // 변경된 todo객체 반환
  })



}
 //=======getter 영역 =====(계산된 값)
 // computed 완료된 할 일의 개수를 계산 
 const doneTodoCount = computed(()=>{
  // isdone이 true인것만 새 배열을 만들어서, 배열의 길이를 return한다. 
  const doneTodos = todos.value.filter((todo) => todo.isDone)
  return doneTodoCount.length
 })
  return { todos, addTodo , deleteTodo, updateTodo, doneTodoCount}
},{persist: true})//새로고침해도 데이터가 유지된다.
