

<template>
                <div @click="checkCheckBox()" class="flex items-center gap-1 w-full ">
                  <div class="border-gray-400 text-xs h-[55%] flex justify-center items-center aspect-square border-[1px]">
                    <i ref="filterCheckBox"  class="fa-solid fa-check invisible" ></i>
                  </div>
                  <h1>{{ Option_Name }}</h1>
                </div>
                <h1 class="text-gray-400">({{ Option_Items }})</h1>

</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router';

const filterCheckBox = ref(null)


const props = defineProps({
        Option_Name: {
            type: String,
            default: ''
        },
        Option_Items: {
            type: Number,
            default: 1
        },
        Option_Filter: {
            type: String,
            default: ''
        }
    })

    const checkCheckBox = () => {
        if(filterCheckBox.value.style.visibility !== 'visible'){
            filterCheckBox.value.style.visibility = 'visible'
        } else{
            filterCheckBox.value.style.visibility = 'hidden'
        }
    }

const route = useRoute()
const hi = Object.entries(route.query)



const initialize = () => {
    for(let i = 0; i < hi.length; i++){
        if(props.Option_Filter !== ''){
            if(props.Option_Filter.includes("-")){
                if(hi[i].includes(props.Option_Name) && hi[i].includes(props.Option_Filter.split("-").join("_").toLowerCase())){
                    checkCheckBox();
                }
            } else{
                if(hi[i].includes(props.Option_Name) && hi[i].includes(props.Option_Filter.split(" ").join("_").toLowerCase())){
                checkCheckBox();
                }
            }

        } else{
            if(hi[i].includes(props.Option_Name)){
                checkCheckBox();
            }
        }
    }
}
setTimeout(initialize, 100)



</script>
