// store/counter.js

import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'

  // 전체게시글 조회하는 함수
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`
    })
      .then(res => {
        articles.value = res.data
      })
      .catch(err => console.log(err))
  }

  const signUp=function(payload){
    // const username = payload.username
    // const password1 = payload.password1
    // const password2 = payload.password2
    const {username, password1, password2}=payload
    
    axios({
      method:'post',
      url:`${API_URL}/accounts/signup/`,
      data:{
        username,password1,password2
      }
    })
    .then(res => {
      console.log('회원가입이 완료되었습니다')
    })
    .catch(err=>console.log(err))
  }
  return { articles, API_URL, getArticles, signUp }
}, { persist: true })
