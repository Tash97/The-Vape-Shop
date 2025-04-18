


<script> 
import { SITE_INFO } from "@/queries";
import{ ref, onUpdated, onMounted } from 'vue'
import gql from "graphql-tag";
import noUiSlider from 'nouislider';
import 'nouislider/dist/nouislider.css';
import { useRouter } from 'vue-router'
import { useRoute } from 'vue-router'








  
export default {
	data() {
		return {
    		Products: null,
    		Category_Filters: null,
    		Brands: null,
    		Prices:	{
        				min: null,
        				max: null
      				}
    	};
	},
  
	async created() {
    	try {

			const router = useRouter()
			const route = useRoute()

			
			onUpdated(() => {
				const min = Math.trunc(this.Prices.min)
				const max = Math.trunc(this.Prices.max)
				const difference = Math.trunc(max - min)
				const oneFourth = Math.trunc(min + (difference / 4))
				const half = Math.trunc(min + (difference / 2))
				const threeFourths = Math.trunc(max - (difference / 4))
				const valuesForSlider = [min,oneFourth,half,threeFourths,max]

				noUiSlider.create(this.$refs.slider, {

					start: [valuesForSlider[0], valuesForSlider[valuesForSlider.length - 1]],
					// A linear range from 0 to 15 (16 values)
					range: { 
						min: min,
						max: max
					},
					// steps of 1
					step: 1,
					connect: true,
					pips: {
						mode: 'positions',
						values: [0, 25, 50, 75, 100],
						density: 100
					}
				});	

				this.$refs.slider.noUiSlider.on('slide', priceRangeUpdater);
			})


    		//Variable for data retrieved
            const Product_Info = await this.$apollo.query({
                query: gql`
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
                    	},
                    	allBatteryTypes{
                    		option
                    	},
                    	allBatterySizes{
                    	    option
                    	},
                    	allMaxWattages{
                    	    option
                    	},
                    	allTankCapacities{
                    		option
                    	},
                    	allTankAirflowStyles{
                    		option
                    	},
                    	allTankCoilStyles{
                    		option
                    	},
                    	allTankDripTips{
                    		option
                    	},
                    	allEjuiceFlavors{
                    		option
                    	},
                    	allEjuiceBottleSizes{
                    		option
                    	},
                    	allEjuiceNicotineAmounts{
                    		option
                    	},
                    	allEjuiceTobaccoFrees{
                    		option
                    	},
                    	allEjuiceSubOhms{
                    		option
                    	},
                    	allEjuiceSaltNicotines{
                    		option
                    	},
                    	allDisposableFlavors{
                    		option
                    	},
                    	allDisposablePuffCounts{
                    		option
                    	},
                    	allDisposableEjuiceCapacities{
                    		option
                    	}    
                	}  
                `,
                variables: {
                    CategoryName: this.$route.params.category,
                    Brand: this.$route.query.brand,
                    BatteryType: this.$route.query.battery_type,
                    BatterySize: this.$route.query.battery_size,
                    MaxWattage: this.$route.query.max_wattage,
                    Capacity: this.$route.query.capacity,
                    AirflowStyle: this.$route.query.airflow_style,                          
                    CoilStyle: this.$route.query.coil_style,
                    DripTip: this.$route.query.drip_tip,
                    Flavor: this.$route.query.flavor,
                    BottleSize: this.$route.query.bottle_size,
                    NicotineAmount: this.$route.query.nicotine_amounts,
                    TobaccoFree: this.$route.query.tobacco_free,
                    SubOhm: this.$route.query.sub_ohm,
                    SaltNicotine: this.$route.query.salt_nicotine,
                    PuffCount: this.$route.query.puff_count,
                    EliquidCapacity: this.$route.query.eliquid_capacity,
					PriceMin: Number(this.$route.query.price_min),
					PriceMax: Number(this.$route.query.price_max)


					
                },
            });

            this.Products = Product_Info.data.productsFiltering;
			

        	// if statement to filter product list by category
        	if(this.$route.params.category === "devices"){

                //function to provide array for options in product list as well as the number of products matching that option, i.e. "option: battery type. list: [dual battery, 6]" there are 6 products in the product list that are dual battery.
                const BatteryTypeArray = []
				const BatterySizeArray = []
				const MaxWattageArray = []

				this.Products.forEach(element => {
					if(BatteryTypeArray.length !== 0){
						for(let i = 0; i < BatteryTypeArray.length; i++){
							if(BatteryTypeArray[i][0] === element.deviceBatteryType.option){
								BatteryTypeArray[i][1] = BatteryTypeArray[i][1] + 1
								break;
							} else if(BatteryTypeArray[i][0] !== element.deviceBatteryType.option && i === BatteryTypeArray.length -1){
								BatteryTypeArray.push([
                        			element.deviceBatteryType.option, 1
                    			])	
								break;
							}	
						}		
					}else{
						BatteryTypeArray.push([
                        	element.deviceBatteryType.option, 1
                    	])	
					}

					if(BatterySizeArray.length !== 0){
						for(let i = 0; i < BatterySizeArray.length; i++){
							if(BatterySizeArray[i][0] === element.deviceBatterySize.option){
								BatterySizeArray[i][1] = BatterySizeArray[i][1] + 1
								break;
							} else if(BatterySizeArray[i][0] !== element.deviceBatterySize.option && i === BatterySizeArray.length - 1){
								BatterySizeArray.push([
                        			element.deviceBatterySize.option, 1
                    			])	
								break;
							}	
						}		
					}else{
						BatterySizeArray.push([
                        	element.deviceBatterySize.option, 1
                    	])	
					}

					if(MaxWattageArray.length !== 0){
						for(let i = 0; i < MaxWattageArray.length; i++){
							if(MaxWattageArray[i][0] === element.deviceMaxWattage.option){
								MaxWattageArray[i][1] = MaxWattageArray[i][1] + 1
								break;
							} else if(MaxWattageArray[i][0] !== element.deviceMaxWattage.option && i === MaxWattageArray.length - 1){
								MaxWattageArray.push([
                        			element.deviceMaxWattage.option, 1
                    			])	
								break;
							}	
						}		
					}else{
						MaxWattageArray.push([
                        	element.deviceMaxWattage.option, 1
                    	])	
					}

				})

                this.Category_Filters = [
                    [BatteryTypeArray, "BATTERY TYPE"],
                    [BatterySizeArray, "BATTERY SIZE"],
                    [MaxWattageArray, "MAX WATTAGE"],
                ];

        	} else if(this.$route.params.category === "tanks"){

				const TankCapacityArray = []
				const TankAirflowStyleArray = []
				const TankCoilStyleArray = []
				const TankDripTipArray = []

				this.Products.forEach(element => {
					if(TankCapacityArray.length !== 0){
						for(let i = 0; i < TankCapacityArray.length; i++){
							if(TankCapacityArray[i][0] === element.tankCapacity.option){
								TankCapacityArray[i][1] = TankCapacityArray[i][1] + 1
								break;
							} else if(TankCapacityArray[i][0] !== element.tankCapacity.option && i === TankCapacityArray.length -1){
								TankCapacityArray.push([
                        			element.tankCapacity.option, 1
                    			])	
								break;
							}	
						}		
					}else{
						TankCapacityArray.push([
                        	element.tankCapacity.option, 1
                    	])	
					}

					if(TankAirflowStyleArray.length !== 0){
						for(let i = 0; i < TankAirflowStyleArray.length; i++){
							if(TankAirflowStyleArray[i][0] === element.tankAirflowStyle.option){
								TankAirflowStyleArray[i][1] = TankAirflowStyleArray[i][1] + 1
								break;
							} else if(TankAirflowStyleArray[i][0] !== element.tankAirflowStyle.option && i === TankAirflowStyleArray.length -1){
								TankAirflowStyleArray.push([
                        			element.tankAirflowStyle.option, 1
                    			])	
								break;
							}	
						}		
					}else{
						TankAirflowStyleArray.push([
                        	element.tankAirflowStyle.option, 1
                    	])	
					}

					if(TankCoilStyleArray.length !== 0){
						for(let i = 0; i < TankCoilStyleArray.length; i++){
							if(TankCoilStyleArray[i][0] === element.tankCoilStyle.option){
								TankCoilStyleArray[i][1] = TankCoilStyleArray[i][1] + 1
								break;
							} else if(TankCoilStyleArray[i][0] !== element.tankCoilStyle.option && i === TankCoilStyleArray.length -1){
								TankCoilStyleArray.push([
                        			element.tankCoilStyle.option, 1
                    			])	
								break;
							}	
						}		
					}else{
						TankCoilStyleArray.push([
                        	element.tankCoilStyle.option, 1
                    	])	
					}

				   if(TankDripTipArray.length !== 0){
						for(let i = 0; i < TankDripTipArray.length; i++){
							if(TankDripTipArray[i][0] === element.tankDripTip.option){
								TankDripTipArray[i][1] = TankDripTipArray[i][1] + 1
								break;
							} else if(TankDripTipArray[i][0] !== element.tankDripTip.option && i === TankDripTipArray.length -1){
								TankDripTipArray.push([
                        			element.tankDripTip.option, 1
                    			])	
								break;
							}	
						}		
					}else{
						TankDripTipArray.push([
                        	element.tankDripTip.option, 1
                    	])	
					}
				})

    			this.Category_Filters = [
        			[TankCapacityArray, "CAPACITY"],
        			[TankAirflowStyleArray, "AIRFLOW STYLE"],
        			[TankCoilStyleArray, "COIL STYLE"],
        			[TankDripTipArray, "DRIP TIP"],
       			];
      		} else if(this.$route.params.category === "e-liquids"){

				const ejuiceFlavorArray = []
				const ejuiceBottleSizeArray = []
				const ejuiceNicotineAmountArray = []
				const ejuiceTobaccoFreeArray = []
				const ejuiceSubOhmArray = []
				const ejuiceSaltNicotineArray = []
				
				this.Products.forEach(element => {
					if(ejuiceFlavorArray.length !== 0){
						for(let i = 0; i < ejuiceFlavorArray.length; i++){
							if(ejuiceFlavorArray[i][0] === element.ejuiceFlavor.option){
								ejuiceFlavorArray[i][1] = ejuiceFlavorArray[i][1] + 1
								break;
							} else if(ejuiceFlavorArray[i][0] !== element.ejuiceFlavor.option && i === ejuiceFlavorArray.length -1){
								ejuiceFlavorArray.push([
                        			element.ejuiceFlavor.option, 1
                    			])	
								break;
							}	
						}		
					}else{
						ejuiceFlavorArray.push([
                        	element.ejuiceFlavor.option, 1
                    	])	
					}

				   if(ejuiceBottleSizeArray.length !== 0){
						for(let i = 0; i < ejuiceBottleSizeArray.length; i++){
							if(ejuiceBottleSizeArray[i][0] === element.ejuiceBottleSize.option){
								ejuiceBottleSizeArray[i][1] = ejuiceBottleSizeArray[i][1] + 1
								break;
							} else if(ejuiceBottleSizeArray[i][0] !== element.ejuiceBottleSize.option && i === ejuiceBottleSizeArray.length -1){
								ejuiceBottleSizeArray.push([
                        			element.ejuiceBottleSize.option, 1
                    			])	
								break;
							}	
						}		
					}else{
						ejuiceBottleSizeArray.push([
                        	element.ejuiceBottleSize.option, 1
                    	])	
					}

				   if(ejuiceNicotineAmountArray.length !== 0){
						for(let i = 0; i < ejuiceNicotineAmountArray.length; i++){
							if(ejuiceNicotineAmountArray[i][0] === element.ejuiceNicotineAmount.option){
								ejuiceNicotineAmountArray[i][1] = ejuiceNicotineAmountArray[i][1] + 1
								break;
							} else if(ejuiceNicotineAmountArray[i][0] !== element.ejuiceNicotineAmount.option && i === ejuiceNicotineAmountArray.length -1){
								ejuiceNicotineAmountArray.push([
                        			element.ejuiceNicotineAmount.option, 1
                    			])	
								break;
							}	
						}		
					}else{
						ejuiceNicotineAmountArray.push([
                        	element.ejuiceNicotineAmount.option, 1
                    	])	
					}

				   if(ejuiceTobaccoFreeArray.length !== 0){
						for(let i = 0; i < ejuiceTobaccoFreeArray.length; i++){
							if(ejuiceTobaccoFreeArray[i][0] === element.ejuiceTobaccoFree.option){
								ejuiceTobaccoFreeArray[i][1] = ejuiceTobaccoFreeArray[i][1] + 1
								break;
							} else if(ejuiceTobaccoFreeArray[i][0] !== element.ejuiceTobaccoFree.option && i === ejuiceTobaccoFreeArray.length -1){
								ejuiceTobaccoFreeArray.push([
                        			element.ejuiceTobaccoFree.option, 1
                    			])	
								break;
							}	
						}		
					}else{
						ejuiceTobaccoFreeArray.push([
                        	element.ejuiceTobaccoFree.option, 1
                    	])	
					}

				   if(ejuiceSubOhmArray.length !== 0){
						for(let i = 0; i < ejuiceSubOhmArray.length; i++){
							if(ejuiceSubOhmArray[i][0] === element.ejuiceSubOhm.option){
								ejuiceSubOhmArray[i][1] = ejuiceSubOhmArray[i][1] + 1
								break;
							} else if(ejuiceSubOhmArray[i][0] !== element.ejuiceSubOhm.option && i === ejuiceSubOhmArray.length -1){
								ejuiceSubOhmArray.push([
                        			element.ejuiceSubOhm.option, 1
                    			])	
								break;
							}	
						}		
					}else{
						ejuiceSubOhmArray.push([
                        	element.ejuiceSubOhm.option, 1
                    	])	
					}

				   if(ejuiceSaltNicotineArray.length !== 0){
						for(let i = 0; i < ejuiceSaltNicotineArray.length; i++){
							if(ejuiceSaltNicotineArray[i][0] === element.ejuiceSaltNicotine.option){
								ejuiceSaltNicotineArray[i][1] = ejuiceSaltNicotineArray[i][1] + 1
								break;
							} else if(ejuiceSaltNicotineArray[i][0] !== element.ejuiceSaltNicotine.option && i === ejuiceSaltNicotineArray.length -1){
								ejuiceSaltNicotineArray.push([
                        			element.ejuiceSaltNicotine.option, 1
                    			])	
								break;
							}	
						}		
					}else{
						ejuiceSaltNicotineArray.push([
                        	element.ejuiceSaltNicotine.option, 1
                    	])	
					}
				})

       			this.Category_Filters = [
        			[ejuiceFlavorArray, "FLAVOR"],
        			[ejuiceBottleSizeArray, "BOTTLE SIZE"],
        			[ejuiceNicotineAmountArray, "NICOTINE AMOUNTS"],
        			[ejuiceTobaccoFreeArray, "TOBACCO FREE"],
        			[ejuiceSubOhmArray, "SUB-OHM"],
        			[ejuiceSaltNicotineArray, "SALT NICOTINE"],
       			];
      		} else if(this.$route.params.category === "disposables"){

				const disposableFlavorArray = []
				const disposablePuffCountArray = []
				const disposableEjuiceCapacityArray = []

				this.Products.forEach(element => {
					if(disposableFlavorArray.length !== 0){
						for(let i = 0; i < disposableFlavorArray.length; i++){
							if(disposableFlavorArray[i][0] === element.disposableFlavor.option){
								disposableFlavorArray[i][1] = disposableFlavorArray[i][1] + 1
								break;
							} else if(disposableFlavorArray[i][0] !== element.disposableFlavor.option && i === disposableFlavorArray.length -1){
								disposableFlavorArray.push([
                        			element.disposableFlavor.option, 1
                    			])	
								break;
							}	
						}		
					}else{
						disposableFlavorArray.push([
                        	element.disposableFlavor.option, 1
                    	])	
					}


				   if(disposablePuffCountArray.length !== 0){
						for(let i = 0; i < disposablePuffCountArray.length; i++){
							if(disposablePuffCountArray[i][0] === element.disposablePuffCount.option){
								disposablePuffCountArray[i][1] = disposablePuffCountArray[i][1] + 1
								break;
							} else if(disposablePuffCountArray[i][0] !== element.disposablePuffCount.option && i === disposablePuffCountArray.length -1){
								disposablePuffCountArray.push([
                        			element.disposablePuffCount.option, 1
                    			])	
								break;
							}	
						}		
					}else{
						disposablePuffCountArray.push([
                        	element.disposablePuffCount.option, 1
                    	])	
					}



				   if(disposableEjuiceCapacityArray.length !== 0){
						for(let i = 0; i < disposableEjuiceCapacityArray.length; i++){
							if(disposableEjuiceCapacityArray[i][0] === element.disposableEjuiceCapacity.option){
								disposableEjuiceCapacityArray[i][1] = disposableEjuiceCapacityArray[i][1] + 1
								break;
							} else if(disposableEjuiceCapacityArray[i][0] !== element.disposableEjuiceCapacity.option && i === disposableEjuiceCapacityArray.length -1){
								disposableEjuiceCapacityArray.push([
                        			element.disposableEjuiceCapacity.option, 1
                    			])	
								break;
							}	
						}		
					}else{
						disposableEjuiceCapacityArray.push([
                        	element.disposableEjuiceCapacity.option, 1
                    	])	
					}
				})

       			this.Category_Filters = [
        			[disposableFlavorArray, "FLAVOR"],
        			[disposablePuffCountArray, "PUFF COUNT"],
        			[disposableEjuiceCapacityArray, "ELIQUID CAPACITY"],
       			];
      		}

			this.Brands = []      

			this.Products.forEach(element => {
			  		if(this.Brands.length !== 0){
						for(let i = 0; i < this.Brands.length; i++){
							if(this.Brands[i][0] === element.brandName.name){
								this.Brands[i][1] = this.Brands[i][1] + 1
								break;
							} else if(this.Brands[i][0] !== element.brandName.name && i === this.Brands.length -1){
								this.Brands.push([
                        			element.brandName.name, 1
                    			])	
								break;
							}	
						}		
					}else{
						this.Brands.push([
                        	element.brandName.name, 1
                    	])	
					}
			})



      		this.Prices = {}      
      		for(let i = 0; i < this.Products.length; i++){
          		if(i === 0){
              		this.Prices['min'] = this.Products[i].productPrice
              		this.Prices['max'] = this.Products[i].productPrice
          		} else if(this.Products[i].productPrice > this.Prices.max){
              		this.Prices.max = this.Products[i].productPrice
          		} else if(this.Products[i].productPrice < this.Prices.min){
              		this.Prices.min = this.Products[i].productPrice
          		}
      		}

			const priceRangeUpdater = () => {
				const interval = setInterval(() => {
					this.$refs.priceRangeMin.value = Math.trunc(this.$refs.slider.noUiSlider.get(true)[0])
					this.$refs.priceRangeMax.value = Math.trunc(this.$refs.slider.noUiSlider.get(true)[1])
					console.log('hi');
				}, 100)
				document.addEventListener("mouseup", () =>{

					if(this.$refs.priceRangeMin){
						const object = {...route.query, price_min: this.$refs.priceRangeMin.value, price_max: this.$refs.priceRangeMax.value}

						router.push({
							name: 'categoryPage',
							params: {
								category: route.params.category
							},
							query: object
						}) 
					}
					clearInterval(interval)

				})
			}

     	} catch (error) {
       		console.error("Error fetching site data:", error);
       		// Handle the error, e.g., display an error message to the user
     	}
   	}
};
</script>

<template>
	<div class="flex w-full justify-center">
      	<div class="flex w-[80%]">
        	<div class="flex flex-col w-[25%] gap-y-6 border-r-2 ps-4 pe-6">
          		<div class="w-full flex gap-y-5 flex-col">
            		<div @click="caretFlipper('brands')" class="flex gap-2">
              			<div class="flex items-center" >
                			<i ref="caretDownBrands" class="fa-solid fa-caret-down"></i>
                			<i ref="caretUpBrands" class="fa-solid fa-caret-up" style="display: none;"></i>
              			</div>
              			<h1 class="font-semibold">BRANDS</h1>
            		</div>
            		<div class="max-h-48 overflow-y-auto" ref="collapseBrand">
              			<div @click="goToCatPageQuery(brands[0], 'brand')" ref="queryRef" class="flex font-thin text-lg hover:cursor-pointer w-full justify-between" :key="index" v-for="(brands, index) in Brands">
                			<CheckBoxer :Option_Name="brands[0]" :Option_Items="brands[1]" />
              			</div>
            		</div>
          		</div>
          		<div  class="w-full flex  pt-6 border-t-2 gap-y-5 flex-col">
            		<div @click="caretFlipper('price')" class="flex gap-2">
              			<div class="flex items-center" >
                			<i ref="caretDownPrice" class="fa-solid fa-caret-down"></i>
                			<i ref="caretUpPrice" class="fa-solid fa-caret-up" style="display: none;"></i>
              			</div>
              			<h1 class="font-semibold">Price</h1>
            		</div>
            		<div class="flex w-full gap-y-5 flex-col items-center" ref="collapsePrice">
              			<div class="flex w-full justify-between">
                			<div class="flex relative w-[40%]">
                  				<div class="absolute bg-white left-1 self-center text-gray-500 text-center text-lg w-[20%]">$</div>
                  				<input ref="priceRangeMin" class="w-full border-2 p-1 px-2 text-end focus:outline-0" type="number" :value="Math.floor(Prices.min)" >
                			</div>
                			<div class="flex relative w-[40%]">
                  				<div class="absolute bg-white left-1 self-center text-gray-500 text-center text-lg w-[20%]">$</div>
                  				<input ref="priceRangeMax" class="w-full border-2 p-1 px-2 text-end focus:outline-0" type="number" :value="Math.floor(Prices.max)" >
                			</div>
              			</div>
              			<div ref="" v-show="Prices['max'] != Prices['min']"  class="flex justify-center items-start mt-3 h-10 w-full">
                			<div   ref="slider" class="w-[90%]">

                			</div>
              			</div>
            		</div>
          		</div>
          		<div v-for="(filter, index) in Category_Filters" ref="attempt" :key="index" class="w-full flex  pt-6 border-t-2 gap-y-5 flex-col">
            		<div @click="caretFlipper(index)" class="flex gap-2  ">
              			<div class="flex items-center" >
                			<i ref="caretDown" class="fa-solid fa-caret-down"></i>
                			<i ref="caretUp" class="fa-solid fa-caret-up" style="display: none;"></i>
              			</div>
              			<h1 class="font-semibold">{{ filter[1] }}</h1>
            		</div>
            		<div ref="collapse" class="flex flex-col pr-4 gap-y-1 max-h-48 overflow-y-auto">
              			<div @click="goToCatPageQuery(options[0], filter[1])" class="flex hover:cursor-pointer font-thin text-lg w-full justify-between" v-for="options in filter[0]">
                			<CheckBoxer :Option_Name="options[0]" :Option_Items="options[1]" :Option_Filter="filter[1]" />
              			</div>
            		</div>
          		</div>
        	</div>
        	<div class="flex w-[75%] flex-wrap">
          		<div v-for="products in Products" @click="goToProductPage(products.productName)"  class="flex flex-col items-center w-1/3 h-[65vh]">
            		<div class="relative aspect-square w-[90%]" >
              			<img class="hover:brightness-50" :src="'http://127.0.0.1:8000/media/' + products.featuredImage1" alt="">
            		</div>
            		<div class="w-full mt-5 gap-3 px-8 text-center flex flex-col items-center">
              			<h1 class="text-xl font-thin">
                			{{ products.productName }}
              			</h1>
              			<p class="text-2xl font-thin">
                			{{ products.brandName.name }}
              			</p>
              			<p class="text-2xl font-thin">
                			${{ products.productPrice }}
              			</p>
            		</div>
          		</div>
        	</div>
      	</div>
  	</div>
</template>


<script setup>
import{ onMounted, ref } from 'vue'
import CheckBoxer from '../components/CheckBoxer.vue'
import { useRouter } from 'vue-router'
import { useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()

const object = ref(null)


const slider = ref(null)
const priceRangeMin = ref(null)
const priceRangeMax = ref(null)






const queryRef = ref(null)

const goToProductPage = (name) => {
    const fixedName = name.split(" ").join("-").toLowerCase()
    router.push({
        name: 'productPage',
        params: {
        	name: name
        },
    })    
}

	// Function to apply filter when checking checkbox, filter is the filter(max wattage, battery type, etc..) 
	// Choice is the chosen option(100W, Dual battery).

const goToCatPageQuery = (choice, filter) => {
  	if(filter === "brand"){
    	if(route.query.brand !== choice){
        	object.value = {...route.query, brand: choice}
      	} else{
        	const query = Object.assign({}, route.query);
        	delete query.brand
        	object.value = query
      	}
	}
  	if(route.params.category === "devices"){
    	if(filter === "BATTERY TYPE"){
      		if(route.query.battery_type !== choice){
        		object.value = {...route.query, battery_type: choice}
      		} else{
        		const query = Object.assign({}, route.query);
        		delete query.battery_type
        		object.value = query
      		}
    	} else if(filter === "BATTERY SIZE"){
      		if(route.query.battery_size !== choice){
        		object.value = {...route.query, battery_size: choice}
      		} else{
        		const query = Object.assign({}, route.query);
        		delete query.battery_size
        		object.value = query
      		}
    	} else if(filter === "MAX WATTAGE"){
      		if(route.query.max_wattage !== choice){
        		object.value = {...route.query, max_wattage: choice}
      		} else{
        		const query = Object.assign({}, route.query);
        		delete query.max_wattage
        		object.value = query
      		}
    	}
  	} else if(route.params.category === "tanks"){
    	if(filter === "CAPACITY"){
      		if(route.query.capacity !== choice){
        		object.value = {...route.query, capacity: choice}
      		} else{
        		const query = Object.assign({}, route.query);
        		delete query.capacity
        		object.value = query
      		}
    	} else if(filter === "AIRFLOW STYLE"){
      		if(route.query.airflow_style !== choice){
        		object.value = {...route.query, airflow_style: choice}
      		} else{
        		const query = Object.assign({}, route.query);
        		delete query.airflow_style
        		object.value = query
      		}
    	} else if(filter === "COIL STYLE"){
      		if(route.query.coil_style !== choice){
        		object.value = {...route.query, coil_style: choice}
      		} else{
        		const query = Object.assign({}, route.query);
        		delete query.coil_style
        		object.value = query
      		}
    	} else if(filter === "DRIP TIP"){
      		if(route.query.drip_tip !== choice){
        		object.value = {...route.query, drip_tip: choice}
      		} else{
        		const query = Object.assign({}, route.query);
        		delete query.drip_tip
        		object.value = query
      		}
    	}
  	} else if(route.params.category === "e-liquids"){
    	if(filter === "FLAVOR"){
      		if(route.query.flavor !== choice){
        		object.value = {...route.query, flavor: choice}
      		} else{
        		const query = Object.assign({}, route.query);
        		delete query.flavor
        		object.value = query
      		}
    	} else if(filter === "BOTTLE SIZE"){
      		if(route.query.bottle_size !== choice){
        		object.value = {...route.query, bottle_size: choice}
      		} else{
        		const query = Object.assign({}, route.query);
        		delete query.bottle_size
        		object.value = query
      		}
    	} else if(filter === "NICOTINE AMOUNTS"){
      		if(route.query.nicotine_amounts !== choice){
        		object.value = {...route.query, nicotine_amounts: choice}
      		} else{
        		const query = Object.assign({}, route.query);
        		delete query.nicotine_amounts
        		object.value = query
      		}
    	} else if(filter === "TOBACCO FREE"){
      		if(route.query.tobacco_free !== choice){
        		object.value = {...route.query, tobacco_free: choice}
      		} else{
        		const query = Object.assign({}, route.query);
        		delete query.tobacco_free
        		object.value = query
      		}
    	} else if(filter === "SUB-OHM"){
      		if(route.query.sub_ohm !== choice){
        		object.value = {...route.query, sub_ohm: choice}
      		} else{
        		const query = Object.assign({}, route.query);
        		delete query.sub_ohm
        		object.value = query
      		}
    	} else if(filter === "SALT NICOTINE"){
      		if(route.query.salt_nicotine !== choice){
        		object.value = {...route.query, salt_nicotine: choice}
      		} else{
        		const query = Object.assign({}, route.query);
        		delete query.salt_nicotine
        		object.value = query
      		}
    	}
  	} else if(route.params.category === "disposables"){
    	if(filter === "FLAVOR"){
      		if(route.query.flavor !== choice){
        		object.value = {...route.query, flavor: choice}
      		} else{
        		const query = Object.assign({}, route.query);
        		delete query.flavor
        		object.value = query
      		}
    	} else if(filter === "PUFF COUNT"){
      		if(route.query.puff_count !== choice){
        		object.value = {...route.query, puff_count: choice}
      		} else{
        		const query = Object.assign({}, route.query);
        		delete query.puff_count
        		object.value = query
      		}
    	} else if(filter === "ELIQUID CAPACITY"){
      		if(route.query.eliquid_capacity !== choice){
        		object.value = {...route.query, eliquid_capacity: choice}
      		} else{
        		const query = Object.assign({}, route.query);
        		delete query.eliquid_capacity
        		object.value = query
      		}
    	} 
  	}
  	router.push({
        name: 'categoryPage',
        params: {
            category: route.params.category
        },
        query: object.value
    })  
}

const attempt = ref(null)

const caretUp = ref(null)
const caretDown = ref(null)

const collapse = ref(null)
const collapseBrand = ref(null)
const collapsePrice = ref(null)

const caretUpBrands = ref(null)
const caretDownBrands = ref(null)
const caretUpPrice = ref(null)
const caretDownPrice = ref(null)

const caretFlipper = (index) => {
	if(index === 'brands'){
    	if(caretUpBrands.value.style.display === 'none'){
        	caretUpBrands.value.style.display = 'flex'
        	caretDownBrands.value.style.display = 'none'
        	collapseBrand.value.style.display = 'none'
    	} else{
        	caretUpBrands.value.style.display = 'none'
        	caretDownBrands.value.style.display = 'flex'
        	collapseBrand.value.style.display = 'initial'
    	}
  	} else if(index === 'price'){
    	if(caretUpPrice.value.style.display === 'none'){
        	caretUpPrice.value.style.display = 'flex'
        	caretDownPrice.value.style.display = 'none'
        	collapsePrice.value.style.display = 'none'
    	} else{
        	caretUpPrice.value.style.display = 'none'
        	caretDownPrice.value.style.display = 'flex'
        	collapsePrice.value.style.display = 'initial'
    	}
  	} else{
      	if(caretUp.value[index].style.display === 'none'){
          	caretUp.value[index].style.display = 'flex'
        	caretDown.value[index].style.display = 'none'
          	collapse.value[index].style.display = 'none'
      	} else{
          	caretUp.value[index].style.display = 'none'
        	caretDown.value[index].style.display = 'flex'
          	collapse.value[index].style.display = 'initial'
      	}
	}

}

const filterCheckBox = ref(null)
const checkCheckBox = () => {
    if(filterCheckBox.value.style.visibility !== 'visible'){
        filterCheckBox.value.style.visibility = 'visible'
    } else{
        filterCheckBox.value.style.visibility = 'hidden'
    }
}
</script>