<template>
    <div @click="caretFlipper()" class="flex gap-2">
        <div class="flex items-center" >
            <i ref="caretDown" class="fa-solid fa-caret-down"></i>
            <i ref="caretUp" class="fa-solid fa-caret-up" style="display: none;"></i>
        </div>
        <h1>{{ Filter_Name }}</h1>
    </div>
</template>

<script setup>
import { ref } from 'vue'


const props = defineProps({
        Filter_Name: {
            type: String,
            default: ''
        },

    })



</script>

