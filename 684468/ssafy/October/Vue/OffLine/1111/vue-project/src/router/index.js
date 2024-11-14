import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import UserView from '@/views/UserView.vue'
import UserProfile from '@/components/UserProfile.vue'
import UserHome from '@/components/UserHome.vue'
import UserPosts from '@/components/UserPosts.vue'
import LoginView from '@/views/LoginView.vue'

const isAuthenicated = false //로그인 상태가 true

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/', // URL
      name: 'home', // 라우트 name
      component: HomeView, 
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),
    },
    {
      path:'/user/:id',
      // views 디렉토리
      component: UserView,

      //beforEach: 전역가드(모든 라우트 이동에서 실행)
      //beforEnter: 특정 라우트 가드(특정 라우트 이동에서 실행)
      beforeEnter:(to,from) =>{
        console.log(to) // 이동 할 라우트
        console.log(from) // 이동 전 라우트 
      },
      // 중첩 라우트
      // components 디렉토리 
      children : [
        {path:'',name:'user',component: UserHome},//localhost/user/:id
        {path:'profile', name:'user-profile', component: UserProfile}, //localhost/user/:id/profile
        {path:'posts', name: 'user-posts', component: UserPosts},//localhost/user/:id/posts
      ]
    },
    {
      path:'/login',
      name:'login',
      component:LoginView,
      beforeEnter:(to,from) =>{
        if(isAuthenicated === true){  //로그인 되었을 경우
          console.log('이미 로그인 상태입니다.')
          return{name:'home'}//이미 로그인 된 상태라면 홈으로 리다이렉트 

        }
      }
    }
  ],
})

export default router
