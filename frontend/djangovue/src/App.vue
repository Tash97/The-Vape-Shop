
<template>
  <nav class="flex w-full h-[100px] justify-between px-10 items-center bg-gradient-to-b from-[hsla(0,0%,0%,1)] to-[hsla(0,0%,15%,1)] to-[90%] shadow-xl">
    <h1 class="text-white text-2xl" @click="goToHomePage()">Generic Vape Shop Name.</h1>
    <div class=" flex justify-between items-center text-white w-[27.5%] h-[100%]">
      <h1 class="text-xl">Deals</h1>
      <h1 class="text-xl">New Stock</h1>
      <button class="text-3xl"><i class="fa-solid fa-bars"></i></button>
    </div>
  </nav>
  <div class="flex text-md font-semibold w-full mb-10 justify-center items-center">
      <h1 @click="goToCategoryPage('brands')" class="hover:bg-gray-300 py-3 px-5">BRANDS</h1>
      <h1 @click="goToCategoryPage('starter-kits')" class="hover:bg-gray-300 py-3 px-5" >STARTER KITS</h1>
      <h1 @click="goToCategoryPage('devices')" class="hover:bg-gray-300 py-3 px-5" >DEVICES</h1>
      <h1 @click="goToCategoryPage('tanks')" class="hover:bg-gray-300 py-3 px-5" >TANKS</h1>
      <h1 @click="goToCategoryPage('accessories')" class="hover:bg-gray-300 py-3 px-5" >ACCESSORIES</h1>
      <h1 @click="goToCategoryPage('e-liquids')" class="hover:bg-gray-300 py-3 px-5" >E-LIQUIDS</h1>
      <h1 @click="goToCategoryPage('alternatives')" class="hover:bg-gray-300 py-3 px-5" >ALTERNATIVES</h1>
      <h1 @click="goToCategoryPage('disposables')" class="hover:bg-gray-300 py-3 px-5" >DISPOSABLES</h1>
      <h1 @click="goToCategoryPage('clearance')" class="hover:bg-gray-300 py-3 px-5" >CLEARANCE</h1>
  </div>
  <RouterView   v-slot="{ Component }">
      <Transition>
        <component :is="Component" :key="uuidv4()" />
      </Transition>
  </RouterView>
    
 
</template>

<script setup>
import { useRouter } from 'vue-router'
import { v4 as uuidv4 } from 'uuid'
import { RouterLink, RouterView } from 'vue-router'
import{ ref } from 'vue'


const router = useRouter()



const goToCategoryPage = (category) => {
      router.push({
          name: 'categoryPage',
          params: {
              category: category
          },
      })    
  }

  const goToHomePage = () => {
      router.push({
          name: 'home',
      })    
  }


  const scrollForward = () => {
    const img1 = document.getElementById("img1")
    const img2 = document.getElementById("img2")
    const img3 = document.getElementById("img3")
    const img4 = document.getElementById("img4")
    const img5 = document.getElementById("img5")

  


    const currentScroll =  document.getElementById("scroller")
    if(!currentScroll.style.animation || currentScroll.style.animation === '0.5s ease-in-out 0s 1 normal forwards running slidePanel1R'){
      currentScroll.style.animation = 'slidePanel1 0.5s forwards ease-in-out'
    } else if(currentScroll.style.animation === '0.5s ease-in-out 0s 1 normal forwards running slidePanel1' && img3 || currentScroll.style.animation === '0.5s ease-in-out 0s 1 normal forwards running slidePanel2R' && img3){
        currentScroll.style.animation = 'slidePanel2 0.5s forwards ease-in-out'
    } else if(currentScroll.style.animation === '0.5s ease-in-out 0s 1 normal forwards running slidePanel2' && img4 || currentScroll.style.animation === '0.5s ease-in-out 0s 1 normal forwards running slidePanel3R' && img4){
      currentScroll.style.animation = 'slidePanel3 0.5s forwards ease-in-out'
    } else if(currentScroll.style.animation === '0.5s ease-in-out 0s 1 normal forwards running slidePanel3' && img5 || currentScroll.style.animation === '0.5s ease-in-out 0s 1 normal forwards running slidePanel4R' && img5){
      currentScroll.style.animation = 'slidePanel4 0.5s forwards ease-in-out'
    }

  }

  const scrollBackward = () => {
    const currentScroll =  document.getElementById("scroller")
    if(currentScroll.style.animation === '0.5s ease-in-out 0s 1 normal forwards running slidePanel1' || currentScroll.style.animation === '0.5s ease-in-out 0s 1 normal forwards running slidePanel2R'){
      currentScroll.style.animation = 'slidePanel1R 0.5s forwards ease-in-out'
    } else if(currentScroll.style.animation === '0.5s ease-in-out 0s 1 normal forwards running slidePanel2' || currentScroll.style.animation === '0.5s ease-in-out 0s 1 normal forwards running slidePanel3R'){
      currentScroll.style.animation = 'slidePanel2R 0.5s forwards ease-in-out'
    } else if(currentScroll.style.animation === '0.5s ease-in-out 0s 1 normal forwards running slidePanel3' || currentScroll.style.animation === '0.5s ease-in-out 0s 1 normal forwards running slidePanel4R'){
      currentScroll.style.animation = 'slidePanel3R 0.5s forwards ease-in-out'
    } else if(currentScroll.style.animation === '0.5s ease-in-out 0s 1 normal forwards running slidePanel4'){
      currentScroll.style.animation = 'slidePanel4R 0.5s forwards ease-in-out'
    }

  }
</script>
