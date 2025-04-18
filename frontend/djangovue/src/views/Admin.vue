<template>
    <div class="flex justify-center w-full lg:min-h-screen md:h-10 ">
        <div class="flex w-4/5 h-[90%] border-slate-300 border-[2px] rounded-lg ">
            <div class="text-[rgb(150,150,150)] w-[15%] h-full flex flex-col justify-start items-center rounded-l-lg relative">
                <div class="flex justify-start ps-[14%] item3-center w-full h-[5%] after:content-[''] after:absolute after:ml-auto after:mt-auto after:right-0 after:top-[1%] after:w-[2px] after:h-[98%] after:bg-slate-300" >
                </div>
                <div @click="goToAdminPage('Dashboard')" class="flex justify-start ps-[14%] gap-3 items-center w-full h-[8%]" >
                    <i class="fa-solid fa-house text-xl text-black"></i>
                    <h1 class="text-md">Dashboard</h1>
                </div>
                <div @click="goToAdminPage('Products')" class="flex justify-start ps-[14%] gap-3 items-center w-full h-[8%]" >
                    <i class="fa-solid fa-shop text-xl text-black"></i>
                    <h1 class="text-md">Products</h1>
                </div>
                <div @click="goToAdminPage('Sales')" class="flex justify-start ps-[14%] gap-3 items-center w-full h-[8%]" >
                    <i class="fa-solid fa-money-check-dollar text-xl text-black"></i>
                    <h1 class="text-md">Sales</h1>
                </div>
                <div @click="goToAdminPage('Customers')" class="flex justify-start ps-[14%] gap-3 items-center w-full h-[8%]" >
                    <i class="fa-solid fa-user text-xl text-black"></i>
                    <h1 class="text-md">Customers</h1>
                </div>
                <div @click="goToAdminPage('Analytics')" class="flex justify-start ps-[14%] gap-3 items-center w-full h-[8%]" >
                    <i class="fa-solid fa-chart-line text-xl text-black"></i>
                    <h1 class="text-md">Analytics</h1>
                </div>
                <div @click="goToAdminPage('Notifications')" class="flex justify-start ps-[14%] gap-3 items-center w-full h-[8%]" >
                    <i class="fa-solid fa-bell text-xl text-black"></i>
                    <h1 class="text-md">Notifications</h1>
                </div>
                <div @click="goToAdminPage('Settings')" class="flex justify-start ps-[14%] gap-3 items-center w-full h-[8%]" >
                    <i class="fa-solid fa-gear text-xl text-black"></i>
                    <h1 class="text-md">Settings</h1>
                </div>
            </div>
            <div class="flex w-[85%] h-full justify-center items center rounded-r-lg">
                <router-view/>
            
            </div>
        </div>
    </div>
</template>


<script setup>
import { v4 as uuidv4 } from 'uuid'

import { useRouter,useRoute } from 'vue-router'


const router = useRouter()
const route = useRoute()




const goToAdminPage = (name) => {

    if(name === 'Products'){
        router.push({
        name: 'adminProducts',
        params: {
            category: 'devices'
        }
    })  
    } else{


    router.push({
        name: 'admin' + name
    })  
    }
    
    
}
</script>

