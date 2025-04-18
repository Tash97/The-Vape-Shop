<script>

import gql from "graphql-tag";


export default {
  data() {
    return {
      Banner_List : null,  
    };
  },

  async created() {
     try {
       const Banner_Products = await this.$apollo.query({
         query: gql`
           query{
              bannerListByName(bannerListName: "first banner list") {
    	            banner1{
                    id,
                    bannerImage,
                    productName
                  },
    	            banner2{
                    id,
                    bannerImage,
                    productName
                  },
    	            banner3{
                    id,
                    bannerImage,
                    productName
                  },
    	            banner4{
                    id,
                    bannerImage,
                    productName
                  },
              }
            }
         `,
        
       });

       this.Banner_List = [
        {
          'image': Banner_Products.data.bannerListByName[0].banner1.bannerImage,
          'id': Banner_Products.data.bannerListByName[0].banner1.id,
          'name': Banner_Products.data.bannerListByName[0].banner1.productName,
        },
        {
          'image': Banner_Products.data.bannerListByName[0].banner2.bannerImage,
          'id': Banner_Products.data.bannerListByName[0].banner2.id,
          'name': Banner_Products.data.bannerListByName[0].banner2.productName,
        },
        {
          'image': Banner_Products.data.bannerListByName[0].banner3.bannerImage,
          'id': Banner_Products.data.bannerListByName[0].banner3.id,
          'name': Banner_Products.data.bannerListByName[0].banner3.productName,
        },
        {
          'image': Banner_Products.data.bannerListByName[0].banner4.bannerImage,
          'id': Banner_Products.data.bannerListByName[0].banner4.id,
          'name': Banner_Products.data.bannerListByName[0].banner4.productName,
        },
      ]


     } catch (error) {
       console.error("Error fetching site data:", error);
       // Handle the error, e.g., display an error message to the user
     }

   }
   
};
</script>

<template>
  <div>
  <div class=" flex relative w-[100%] ">
    <div @mouseover="scrollerReveal()" @mouseout="scrollerHide()" @click="scrollBackward()" id="chevronLeft" class="hidden opacity-70 bg-opacity-50 text-5xl text-black z-20 absolute left-[5%] justify-center items-center w-[5%] h-[100%] bg-slate-400">
      <i id="scrollLeft" class="fa-solid  fa-chevron-left"></i>
    </div>
    <div @mouseover="scrollerReveal()" @mouseout="scrollerHide()" @click="scrollForward()" id="chevronRight" class="hidden text-black text-5xl opacity-70 bg-opacity-50 z-20 absolute left-[90%] justify-center items-center w-[5%] h-[100%] bg-slate-400">
      <i class="fa-solid fa-chevron-right"></i>
    </div>
    <div @mouseover="scrollerReveal()" @mouseout="scrollerHide()" class="w-[90%] overflow-hidden mx-auto">
      <div id="scroller" class="w-[100%]  flex min-w-[100%] aspect-[12/5]">
        <div @click="goToProductPage(banner.id, banner.name)" class="w-[100%] min-w-[100%] h-full " v-for="banner in Banner_List" >
          <img class="w-full" :src="'http://127.0.0.1:8000/media/' + banner.image" :alt="'http://127.0.0.1:8000/media/' + banner.image">
        </div>
      </div>
    </div>
  </div>
 <SlotCarousel List_Name="New Arrivals"  />
 <SlotCarousel class="bg-gray-200" List_Name="Best Sellers"  />
 <SlotCarousel List_Name="Featured"  />
 </div>


</template>

<script setup>
import { useRouter } from 'vue-router'
import SlotCarousel from '../components/6SlotCarousel.vue'

const router = useRouter()

const goToProductPage = (id, name) => {
      const fixedName = name.split(" ").join("-").toLowerCase()

      router.push({
          name: 'productPage',
          params: {
            name: name
          },
      })    
  }



  const scrollerReveal = () => {
  document.getElementById("chevronLeft").style.display = "flex"
  document.getElementById("chevronRight").style.display = "flex"

}

const scrollerHide = () => {
  document.getElementById("chevronLeft").style.display = "none"
  document.getElementById("chevronRight").style.display = "none"

}

  const scrollForward = () => {


  


    const currentScroll =  document.getElementById("scroller")
    if(!currentScroll.style.animation || currentScroll.style.animation === '0.5s ease-in-out 0s 1 normal forwards running flashPanel1R'){
      currentScroll.style.animation = 'flashPanel1 0.5s forwards ease-in-out'
    } else if(currentScroll.style.animation === '0.5s ease-in-out 0s 1 normal forwards running flashPanel1'   ){
        currentScroll.style.animation = 'flashPanel2 0.5s forwards ease-in-out'
    } else if(currentScroll.style.animation === '0.5s ease-in-out 0s 1 normal forwards running flashPanel2' ){
      currentScroll.style.animation = 'flashPanel3 0.5s forwards ease-in-out'
    }

  }

  const scrollBackward = () => {
    const currentScroll =  document.getElementById("scroller")
    if(currentScroll.style.animation === '0.5s ease-in-out 0s 1 normal forwards running flashPanel1' || currentScroll.style.animation === '0.5s ease-in-out 0s 1 normal forwards running flashPanel2R'){
      currentScroll.style.animation = 'flashPanel1R 0.5s forwards ease-in-out'
    } else if(currentScroll.style.animation === '0.5s ease-in-out 0s 1 normal forwards running flashPanel2' || currentScroll.style.animation === '0.5s ease-in-out 0s 1 normal forwards running flashPanel3R'){
      currentScroll.style.animation = 'flashPanel2R 0.5s forwards ease-in-out'
    } else if(currentScroll.style.animation === '0.5s ease-in-out 0s 1 normal forwards running flashPanel3'){
      currentScroll.style.animation = 'flashPanel3R 0.5s forwards ease-in-out'
    }

  }

</script>
