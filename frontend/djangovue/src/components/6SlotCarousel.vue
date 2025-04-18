<script>
import gql from "graphql-tag";


export default {
  data() {
    return {
      Featured_List1: null,
      Product_List1: null,
     
    };
  },

  async created() {
     try {
       const Featured_Products1 = await this.$apollo.query({
         query: gql`
           query ($featuredListName: String) {
             featuredListByName(featuredListName: $featuredListName) {
               featuredListName,
               featuredProduct1{
                productName,
                productPrice,
                brandName{
                  name
                },
                featuredImage1,
                id,
               },
               featuredProduct2{
                productName,
                productPrice,
                brandName{
                  name
                },
                featuredImage1,
                id,
               },
               featuredProduct3{
                productName,
                productPrice,
                brandName{
                  name
                },
                featuredImage1,
                id,
               },
               featuredProduct4{
                productName,
                productPrice,
                brandName{
                  name
                },
                featuredImage1,
                id,
               },
               featuredProduct5{
                productName,
                productPrice,
                brandName{
                  name
                },
                featuredImage1,
                id,
               },
               featuredProduct6{
                productName,
                productPrice,
                brandName{
                  name
                },
                featuredImage1,
                id,
               },
               featuredProduct7{
                productName,
                productPrice,
                brandName{
                  name
                },
                featuredImage1,
                id,
               },
               featuredProduct8{
                productName,
                productPrice,
                brandName{
                  name
                },
                featuredImage1,
                id,
               },
               featuredProduct9{
                productName,
                productPrice,
                brandName{
                  name
                },
                featuredImage1,
                id,
               },
               featuredProduct10{
                productName,
                productPrice,
                brandName{
                  name
                },
                featuredImage1,
                id,
               },
              }
           }
         `,
         variables: {
            featuredListName: this.$props.List_Name,
        },
       });

       this.Featured_Lists1 = Featured_Products1.data.featuredListByName[0].featuredListName;
       const array = []
        array.push(
          Featured_Products1.data.featuredListByName[0].featuredProduct1,
          Featured_Products1.data.featuredListByName[0].featuredProduct2,
          Featured_Products1.data.featuredListByName[0].featuredProduct3,
          Featured_Products1.data.featuredListByName[0].featuredProduct4,
          Featured_Products1.data.featuredListByName[0].featuredProduct5,
          Featured_Products1.data.featuredListByName[0].featuredProduct6,
          Featured_Products1.data.featuredListByName[0].featuredProduct7,
          Featured_Products1.data.featuredListByName[0].featuredProduct8,
          Featured_Products1.data.featuredListByName[0].featuredProduct9,
          Featured_Products1.data.featuredListByName[0].featuredProduct10,
        )
        this.Product_List1 = array
     } catch (error) {
       console.error("Error fetching site data:", error);
       // Handle the error, e.g., display an error message to the user
     }
   }
   
};
</script>

<template>
    <div  class="flex flex-col w-[100%] ">
      <div class="w-full h-[15vh] flex justify-center  items-center">
        <h1 class="text-3xl font-thin">{{  Featured_List1  }}</h1>
      </div>
      <div>
        <div @click="scrollBackward()" @mouseover="scrollerReveal()" @mouseout="scrollerHide()"  ref="left" class="z-20 hidden absolute w-[5%] opacity-50 text-5xl h-[70vh] text-slate-400  justify-center items-center bg-slate-400 bg-opacity-25">
          <i  class="fa-solid fa-chevron-left"></i>
        </div>
        <div @click="scrollForward()" @mouseover="scrollerReveal()" @mouseout="scrollerHide()"  ref="right" class="z-20 hidden absolute w-[5%] opacity-50 left-[95%] text-5xl h-[70vh] text-slate-400  justify-center items-center bg-slate-400 bg-opacity-25">
          <i  class="fa-solid fa-chevron-right"></i>
        </div>
          <div class="overflow-hidden ">
            <div @mouseover="scrollerReveal()" @mouseout="scrollerHide()" ref="scroller" class="w-full min-w-[100%] hover:cursor-grab  flex justify-start h-[70vh]">
              <div @click="goToProductPage(product.productName)" id="product"  class=" flex flex-col gap-2 items-center sm:min-w-[33.2%]  md:min-w-[16.6%] h-fit hover:cursor-pointer" v-for="product in Product_List1"   >
                      <div class="flex w-[95%] mx-auto aspect-square">
                        <img class=" w-[100%] object-fill h-[100%]" :src="'http://127.0.0.1:8000/media/' + product.featuredImage1" :alt="product">
                      </div>
                      <div class="h-1/3 flex flex-col gap-2 items-center px-10 ">
                        <h1 class=" text-center text-xl font-thin">{{ product.productName }}</h1>
                        <h1 class="font-thin  text-2xl">{{ product.brandName.name }}</h1>
                        <h1 class="font-thin text-2xl">${{ product.productPrice }}</h1>
                      </div>
              </div>
            </div>
          </div>
      </div>
    </div>
  </template>

<script setup>
import { useRouter } from 'vue-router'
import{ ref } from 'vue'
const left = ref(null)
const right = ref(null)
const scroller = ref(null)



const props = defineProps({
        List_Name: {
            type: String,
            default: ''
        }
    })


const router = useRouter()

const goToProductPage = (name) => {
      router.push({
          name: 'productPage',
          params: {
              name: name
          },
      })    
  }

const scrollerReveal = () => {
  left.value.style.display = "flex"
  right.value.style.display = "flex"

}

const scrollerHide = () => {
  left.value.style.display = "none"
  right.value.style.display = "none"

}

const scrollForward = () => {
  const currentScroll =  scroller.value
  if(!currentScroll.style.animation || currentScroll.style.animation === '0.5s ease-in-out 0s 1 normal forwards running slideCarousel1R'){
    currentScroll.style.animation = 'slideCarousel1 forwards 0.5s ease-in-out'
  } else if(currentScroll.style.animation === '0.5s ease-in-out 0s 1 normal forwards running slideCarousel1'  || currentScroll.style.animation === '0.5s ease-in-out 0s 1 normal forwards running slideCarousel2R' ){
      currentScroll.style.animation = 'slideCarousel2 0.5s forwards ease-in-out'
  } else if(currentScroll.style.animation === '0.5s ease-in-out 0s 1 normal forwards running slideCarousel2'  || currentScroll.style.animation === '0.5s ease-in-out 0s 1 normal forwards running slideCarousel3R' ){
    currentScroll.style.animation = 'slideCarousel3 0.5s forwards ease-in-out'
  } else if(currentScroll.style.animation === '0.5s ease-in-out 0s 1 normal forwards running slideCarousel3'  || currentScroll.style.animation === '0.5s ease-in-out 0s 1 normal forwards running slideCarousel4R' ){
    currentScroll.style.animation = 'slideCarousel4 0.5s forwards ease-in-out'
  }
}

const scrollBackward = () => {
  const currentScroll =  scroller.value
  if(currentScroll.style.animation === '0.5s ease-in-out 0s 1 normal forwards running slideCarousel1' || currentScroll.style.animation === '0.5s ease-in-out 0s 1 normal forwards running slideCarousel2R'){
    currentScroll.style.animation = 'slideCarousel1R 0.5s forwards ease-in-out'
  } else if(currentScroll.style.animation === '0.5s ease-in-out 0s 1 normal forwards running slideCarousel2' || currentScroll.style.animation === '0.5s ease-in-out 0s 1 normal forwards running slideCarousel3R'){
    currentScroll.style.animation = 'slideCarousel2R 0.5s forwards ease-in-out'
  } else if(currentScroll.style.animation === '0.5s ease-in-out 0s 1 normal forwards running slideCarousel3' || currentScroll.style.animation === '0.5s ease-in-out 0s 1 normal forwards running slideCarousel4R'){
    currentScroll.style.animation = 'slideCarousel3R 0.5s forwards ease-in-out'
  } else if(currentScroll.style.animation === '0.5s ease-in-out 0s 1 normal forwards running slideCarousel4'  || currentScroll.style.animation === '0.5s ease-in-out 0s 1 normal forwards running slideCarousel5R'){
    currentScroll.style.animation = 'slideCarousel4R 0.5s forwards ease-in-out'
  } 
}
</script>