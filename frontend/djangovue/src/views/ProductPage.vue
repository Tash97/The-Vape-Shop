<script>
import { SITE_INFO } from "@/queries";
import{ ref } from 'vue'
import gql from "graphql-tag";
import { useRoute } from 'vue-router'

  


export default {
  data() {
    return {
      Product: null,
    };
  },

  

  async created() {
    
     try {

       const Product_Info = await this.$apollo.query({
         query: gql`
           query ($productName: String) {
             productPage(productName: $productName) {
               productName,
               productPrice,
               brandName{
                name
               },
               description,
               featuredImage1,
               featuredImage2,
               featuredImage3,
               featuredImage4,
               featuredImage5,
               productOptions1Title,
               productOptions1Option1,
               productOptions1Option2,
               productOptions1Option3,
               productOptions1Option4,
               productOptions1Option5,
               productOptions2Title,
               productOptions2Option1,
               productOptions2Option2,
               productOptions2Option3,
               productOptions2Option4,
               productOptions2Option5,


              }
           }
         `,
        variables: {
            productName: this.$route.params.name,
        },
       });
       this.Product = Product_Info.data.productPage;

     } catch (error) {
       console.error("Error fetching site data:", error);
       // Handle the error, e.g., display an error message to the user
     }
   }
   
};






</script>

<template>
  
  <div class=" w-full  flex flex-col items-center md:mt-10">
    <div v-if="Product"  class=" w-full rounded-xl shadow-2xl  flex flex-col"   >
        <div class="flex items-start sm:flex-col md:flex-row ">
          <div class=" md:py-10 sm:w-full md:w-3/5 h-fit flex justify-end  md:pe-5" >
            <div class=" flex sm:w-[100vw] md:w-[47vw] ">
              <div v-if="Product[0].featuredImage2" @click="scrollBackward()"  class=" w-[5%] flex justify-center items-center text-2xl text-black h-full">
                <i class="fa-solid fa-chevron-left"></i>
              </div>
                <div class="w-[90%] min-w-[90%] overflow-hidden">
                  <div id="scroller" class="flex min-w-[100%]">
                    <div v-if="Product[0].featuredImage1" class="flex  min-w-[100%] w-[100%]  bg-blue-500">
                      <img id="img1" class="min-w-[100%]" :src="'http://127.0.0.1:8000/media/' + Product[0].featuredImage1" :alt="'http://127.0.0.1:8000/media/' + Product[0].featuredImage1" >
                    </div>
                    <div v-if="Product[0].featuredImage2" class="flex justify-center min-w-[100%] w-[100%]  bg-blue-500">
                      <img id="img2" class="min-w-[100%] " :src="'http://127.0.0.1:8000/media/' + Product[0].featuredImage2" :alt="'http://127.0.0.1:8000/media/' + Product[0].featuredImage1" >
                    </div>
                    <div v-if="Product[0].featuredImage3" class="flex justify-center min-w-[100%] w-[100%]  bg-blue-500">
                      <img id="img3" class="min-w-[100%] " :src="'http://127.0.0.1:8000/media/' + Product[0].featuredImage3" :alt="'http://127.0.0.1:8000/media/' + Product[0].featuredImage1" >
                    </div>
                    <div v-if="Product[0].featuredImage4" class="flex justify-center min-w-[100%] w-[100%]  bg-blue-500">
                      <img id="img4" class="min-w-[100%] " :src="'http://127.0.0.1:8000/media/' + Product[0].featuredImage4" :alt="'http://127.0.0.1:8000/media/' + Product[0].featuredImage1" >
                    </div>
                    <div v-if="Product[0].featuredImage5" class="flex justify-center min-w-[100%] w-[100%]  bg-blue-500">
                      <img id="img5"  class="min-w-[100%] " :src="'http://127.0.0.1:8000/media/' + Product[0].featuredImage5" :alt="'http://127.0.0.1:8000/media/' + Product[0].featuredImage1" >
                    </div>
                  </div>
                </div>
              <div v-if="Product[0].featuredImage2" @click="scrollForward()" class=" w-[5%] flex justify-center items-center text-2xl text-black h-full">
                <i  class="fa-solid fa-chevron-right"></i>
              </div>
            </div>
          </div>
          <div class="sm:w-full md:w-2/5 flex flex-col gap-5 px-16  pt-14">
            <h1 class="text-2xl font-thin">{{ Product[0].productName }}</h1>
            <h1 class="text-2xl font-thin">${{ Product[0].productPrice }}</h1>
            <div class="w-full">
              <h1 v-if="Product[0].productOptions1Title" class="text-md font-semibold">{{ Product[0].productOptions1Title }}</h1>
              <select class="w-[100%] font-thin py-2 border-black border-[1px] rounded-sm" name="cars" id="cars">
                <option v-if="Product[0].productOptions1Option1"  :value="Product[0].productOptions1Option1" >{{ Product[0].productOptions1Option1 }}</option>
                <option v-if="Product[0].productOptions1Option2" :value="Product[0].productOptions1Option2" >{{ Product[0].productOptions1Option2 }}</option>
                <option v-if="Product[0].productOptions1Option3" :value="Product[0].productOptions1Option3" >{{ Product[0].productOptions1Option3 }}</option>
                <option v-if="Product[0].productOptions1Option4" :value="Product[0].productOptions1Option4" >{{ Product[0].productOptions1Option4 }}</option>
                <option v-if="Product[0].productOptions1Option5" :value="Product[0].productOptions1Option5" >{{ Product[0].productOptions1Option5 }}</option>
              </select>
            </div>
            <div class="w-full">
              <h1 v-if="Product[0].productOptions2Title" class="text-md font-semibold">{{ Product[0].productOptions2Title }}</h1>
              <select  v-if="Product[0].productOptions2Title" class="w-[100%] py-2 border-black font-thin border-[1px] rounded-sm" name="cars" id="cars">
                <option v-if="Product[0].productOptions2Option1"  :value="Product[0].productOptions2Option1" >{{ Product[0].productOptions2Option1 }}</option>
                <option v-if="Product[0].productOptions2Option2" :value="Product[0].productOptions2Option2" >{{ Product[0].productOptions2Option2 }}</option>
                <option v-if="Product[0].productOptions2Option3" :value="Product[0].productOptions2Option3" >{{ Product[0].productOptions2Option3 }}</option>
                <option v-if="Product[0].productOptions2Option4" :value="Product[0].productOptions2Option4" >{{ Product[0].productOptions2Option4 }}</option>
                <option v-if="Product[0].productOptions2Option5" :value="Product[0].productOptions2Option5" >{{ Product[0].productOptions2Option5 }}</option>
              </select>
            </div>
            <div class=' flex justify-between w-full h-12'>
              <div class="flex w-[48%]">
                <div @click="quantityDown()" class="w-1/4 h-full border-[1px] border-gray-300 flex justify-center items-center bg-gray-200">
                  <i class="fa-solid fa-minus"></i>
                </div>
                <input id="quantity" class="w-1/2 text-center border-y-[1px] border-gray-300 focus:outline-none" type='number' value="1">
                <div @click="quantityUp()" class="w-1/4 h-full border-[1px] border-gray-300 flex justify-center items-center bg-gray-200">
                  <i class="fa-solid fa-plus"></i>
                </div>
              </div>
              <button class="w-[48%] bg-blue-500 font-semibold text-white">ADD TO CART</button>

            </div>
            <h1 class="text-2xl">{{ Product[0].description }}</h1>

          </div>
        </div>
        
    </div>
  </div>

</template>

<script setup>

  const quantityUp = () => {
    document.getElementById("quantity").value = Number(document.getElementById("quantity").value) + 1
  }

  const quantityDown = () => {
    document.getElementById("quantity").value = Number(document.getElementById("quantity").value) - 1
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