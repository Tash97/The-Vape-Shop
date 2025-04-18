<template>
    <div class="flex justify-center items-center w-[100%] h-[100%] rounded-r-lg">
        <div class="flex flex-col justify-start w-[95%] h-[95%] shadow-lg rounded-lg border-[2px] border-slate-300">
			<div class="flex justify-between items-center w-full h-[7.5%] rounded-t-lg px-2">
				<div class="flex h-full justify-center items-center text-lg text-black font-semibold ">
					<h1>Products</h1>
				</div>
				<div class="flex h-full items-center  gap-x-3">
					<button class="bg-transparent hover:bg-black text-black h-2/3 flex items-center gap-x-1 font-semibold hover:text-white px-2 border border-black hover:border-transparent rounded">
						<i class="fa-solid fa-filter text-sm"></i>
						<div>Filter</div>
					</button>
					<button class="bg-transparent hover:bg-black text-black h-2/3 flex items-center gap-x-1 font-semibold hover:text-white px-2 border border-black hover:border-transparent rounded">
						See All
					</button>
					<button class="bg-transparent hover:bg-black text-black h-2/3 flex items-center gap-x-1 font-semibold hover:text-white px-2 border border-black hover:border-transparent rounded">
						<i class="fa-solid fa-plus text-sm"></i>
						<div>Add Product</div>
					</button>
				</div>

			</div>
			<div class="flex justify-start items-center ps-2 w-full h-[5.5%] border-y-[2px] border-slate-200">
				<div class="flex gap-x-2 w-[25%]">
					<input type="checkbox">
					<div class="flex items-center gap-x-2 ">
						<div>Product Name</div>
						<i class="fa-solid fa-caret-down text-sm mt-1"></i>
					</div>
				</div>
				<div class="flex items-center w-[15%] gap-x-3">
					
					<div @click="dropdowner(categoryDropDown)" >Category</div>
					<i class="fa-solid fa-caret-down text-sm mt-1"></i>
					<div ref="categoryDropDown" class="absolute translate-y-[59%] translate-x-[-5%] w-22 px-2 py-1 hidden flex-col bg-slate-100">
						<div @click="selectCategory('starter-kits')">Starter Kits</div>
						<div @click="selectCategory('devices')" >Devices</div>
						<div @click="selectCategory('tanks')">Tanks</div>
						<div @click="selectCategory('e-liquids')">ELiquids</div>
						<div @click="selectCategory('alternatives')">Alternatives</div>
						<div @click="selectCategory('disposables')">Disposables</div>

					</div>
					
				</div>
				<div class="flex items-center w-[15%] gap-x-2">
					<div>Price</div>
					<i class="fa-solid fa-caret-down text-sm mt-1"></i>
				</div>
				<div class="flex items-center w-[15%] gap-x-2">
					<div>Stock</div>
					<i class="fa-solid fa-caret-down text-sm mt-1"></i>
				</div>
				<div class="flex items-center w-[15%] gap-x-2">
					<div>Status</div>
					<i class="fa-solid fa-caret-down text-sm mt-1"></i>
				</div>
				<div class="flex items-center w-[15%] gap-x-2">
					<div>Action</div>
					<i class="fa-solid fa-caret-down text-sm mt-1"></i>
				</div>
			</div>
			<div ref="table" v-for="(product, index) in Products" :id="index" class="flex justify-start items-center w-full h-[8%] ">
				<div class="flex h-full items-center w-[7%]">
					<div class="flex gap-x-2 aspect-square h-[80%] ps-2" >
							<input type="checkbox">
							<img class="hover:brightness-50 border-[1px] border-slate-400" :src="'http://127.0.0.1:8000/media/' + product.featuredImage1" alt="">
					</div>
				</div>
				<div class="flex text-ellipsis truncate w-[13%] mr-[5.5%]">
						{{ product.productName.charAt(0) +  product.productName.toLowerCase().slice(1) }}
				</div>
				<div class="flex w-[10%] mr-[5%]">
					{{ product.category.charAt(0) +  product.category.toLowerCase().slice(1) }}
				</div>
				<div class="flex w-[10%] mr-[5%]">
					{{ product.productPrice }}
				</div>
				<div class="flex w-[10%] mr-[4.5%]">
					{{ product.productInventory }}
				</div>
				<div class="flex w-[10%] mr-[5%]">
					Status(TODO)
				</div>
				<div class="flex justify-start items-center h-2/3 w-[7%] ">
					<button class=" flex justify-center  items-center h-full w-[80%] border-black border bg-white text-black  rounded-y rounded-s hover:bg-black hover:text-white hover:border-transparent">
						<div class="font-semibold">Edit</div>
					</button>
					<button class="h-full w-[20%] flex flex-col justify-center gap-y-1 border-black border-y border-r bg-white rounded-r hover:bg-black  hover:border-transparent hover:text-white pe-[2px] ">
						<i class="fa-solid fa-circle text-[3px] "></i>
						<i class="fa-solid fa-circle text-[3px] "></i>
						<i class="fa-solid fa-circle text-[3px] "></i>
					</button>
				</div>
			</div>
			<div class="flex justify-between items-center w-full border-t-[2px] border-slate-200 h-[7%] rounded-b-lg px-5">
				<button class="flex items-center gap-x-2   bg-transparent  text-black h-2/3 font-semibold px-2 border border-white hover:border-black rounded">
					<i class="fa-solid fa-arrow-left"></i>
					<div>Previous</div>
				</button>
				<div>
					Page Number
				</div>
				<button class="flex items-center gap-x-2  bg-transparent  text-black h-2/3 font-semibold px-2 border border-white hover:border-black rounded">
					<div>Next</div>
					<i class="fa-solid fa-arrow-right mt-1"></i>
				</button>
			</div>
		</div>
    </div>
</template>

<script setup>
import { useRouter,useRoute } from 'vue-router'
import{ ref, watch, computed } from 'vue'
import gql from 'graphql-tag'
import { useQuery } from '@vue/apollo-composable'


const router = useRouter()
const route = useRoute()


const CHARACTERS_QUERY = gql`
	query(
		$CategoryName: String, 
  		$Brand: String,
	  	$BatteryType : String,
		$BatterySize : String,
  		$MaxWattage : String,
  		$Capacity : String,
  		$AirflowStyle : String,
        $CoilStyle : String,
	  	$DripTip : String,
		$Flavor : String,
  		$BottleSize : String,
		$NicotineAmount : String,
  		$TobaccoFree : String,
  		$SubOhm : String,
  		$SaltNicotine : String,
        $PuffCount : String,
  		$EliquidCapacity : String,
		$PriceMin : Float,       
		$PriceMax : Float
        ) {
	        productsFiltering(
							CategoryName: $CategoryName, 
			                Brand: $Brand,
    			            BatteryType: $BatteryType,
        			        BatterySize: $BatterySize,
            			    MaxWattage: $MaxWattage,
                			Capacity: $Capacity,
	                    	AirflowStyle: $AirflowStyle,
    	                    CoilStyle: $CoilStyle,
        	                DripTip: $DripTip,
            	            Flavor: $Flavor,
                	        BottleSize: $BottleSize,
                    	    NicotineAmount: $NicotineAmount,
                        	TobaccoFree: $TobaccoFree,
		            		SubOhm: $SubOhm,
    			            SaltNicotine: $SaltNicotine,
        			        PuffCount: $PuffCount,
            			    EliquidCapacity: $EliquidCapacity,
							PriceMin: $PriceMin,
							PriceMax: $PriceMax
                	    ){
                        	productName,
							productInventory,
    						category,
    						productPrice,
                        	brandName{
                        		name
                        	},
                        	productPrice,
                        	featuredImage1,
                        	deviceBatteryType{
                        	    option
                        	},
                        	deviceBatterySize{
                        	    option
                        	},
                        	deviceMaxWattage{
                        	    option
                        	},
                        	tankCapacity{
                        	    option
                        	},
                        	tankAirflowStyle{
                        	    option
                        	},
                        	tankCoilStyle{
                        	    option
                        	},
                        	tankDripTip{
                        	    option
                        	},
                        	ejuiceFlavor{
                        	    option
                        	},
                        	ejuiceBottleSize{
                        	    option
                        	},
                        	ejuiceNicotineAmount{
                        	    option
                        	},
                        	ejuiceTobaccoFree{
                        	    option
                        	},
                        	ejuiceSubOhm{
                        	    option
                        	},
                        	ejuiceSaltNicotine{
                        	    option
                        	},
                        	disposableFlavor{
                        	    option
                        	},
                        	disposablePuffCount{
                        	    option
                        	},
                        	disposableEjuiceCapacity{
                        	    option
                        	},
                    	}  
                	}  
                `

const variables = ref({
				CategoryName : route.params.category,
                Brand : route.query.brand,
                BatteryType : route.query.battery_type,
                BatterySize : route.query.battery_size,
                MaxWattage : route.query.max_wattage,
                Capacity : route.query.capacity,
                AirflowStyle : route.query.airflow_style,
                CoilStyle : route.query.coil_style,
                DripTip : route.query.drip_tip,
                Flavor : route.query.flavor,
                BottleSize : route.query.bottle_size,
                NicotineAmount : route.query.nicotine_amounts,
                TobaccoFree : route.query.tobacco_free,
                SubOhm : route.query.sub_ohm,
                SaltNicotine : route.query.salt_nicotine,
                PuffCount : route.query.puff_count,
                EliquidCapacity : route.query.eliquid_capacity,
				PriceMin : Number(route.query.price_min),
				PriceMax : Number(route.query.price_max)
})


const { result, loading, error  } = useQuery(CHARACTERS_QUERY, variables)



const Products = computed(() => {
	if(result && result.value){
		return result.value.productsFiltering
		}	
})

	const table = ref(null)

watch(table, () => {
	table.value.forEach((element) => {
		if(Number(element.id) % 2 !== 0){
			element.style.backgroundColor = "rgba(150,150,150, .3)"
		}
	})	
})

const categoryDropDown = ref(null)

const dropdowner = (drop) => {
	if(drop.style.display === 'flex'){
		drop.style.display = 'none'
	} else {
		drop.style.display = 'flex'
	}		
}

const selectCategory = (category) => {
	router.replace({
          name: 'adminProducts',
          params: {
              category: category
          },
      })   
}

</script>

