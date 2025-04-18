import graphene
from blog import models
from blog import types
from django.db.models import Q


# The Query class
class Query(graphene.ObjectType):
    site = graphene.Field(types.SiteType)
    all_products = graphene.List(types.ProductType)
    product_page = graphene.List(types.ProductType, productName=graphene.String())
    featured_list_by_name = graphene.List(types.Featured_ListType, featured_list_name=graphene.String())
    banner_list_by_name = graphene.List(types.Banner_ListType, banner_list_name=graphene.String())
    products_by_category = graphene.List(types.ProductType, category=graphene.String())
    all_battery_types = graphene.List(types.Battery_TypeType)
    all_battery_sizes = graphene.List(types.Battery_SizeType)
    all_max_wattages = graphene.List(types.Max_WattageType)
  
    all_tank_capacities = graphene.List(types.Tank_CapacityType)
    all_tank_airflow_styles = graphene.List(types.Tank_Airflow_StyleType)
    all_tank_coil_styles = graphene.List(types.Tank_Coil_StyleType)
    all_tank_drip_tips = graphene.List(types.Tank_Drip_TipType)
    all_ejuice_flavors = graphene.List(types.EJuice_FlavorType)
    all_ejuice_bottle_sizes = graphene.List(types.EJuice_Bottle_SizeType)
    all_ejuice_nicotine_amounts = graphene.List(types.EJuice_Nicotine_AmountType)
    all_ejuice_tobacco_frees = graphene.List(types.EJuice_Tobacco_FreeType)
    all_ejuice_sub_ohms = graphene.List(types.EJuice_Sub_OhmType)
    all_ejuice_salt_nicotines = graphene.List(types.EJuice_Salt_NicotineType)
    all_disposable_flavors = graphene.List(types.Disposable_FlavorType)
    all_disposable_puff_counts = graphene.List(types.Disposable_Puff_CountType)
    all_disposable_ejuice_capacities = graphene.List(types.Disposable_EJuice_CapacityType)





    products_filtering = graphene.List(types.ProductType, 
                                                   CategoryName=graphene.String(), 
                                                   Brand=graphene.String(), 
                                                   BatteryType=graphene.String(), 
                                                   BatterySize=graphene.String(), 
                                                   MaxWattage=graphene.String(), 
                                                   Capacity=graphene.String(), 
                                                   AirflowStyle=graphene.String(), 
                                                   CoilStyle=graphene.String(), 
                                                   DripTip=graphene.String(), 
                                                   Flavor=graphene.String(), 
                                                   BottleSize=graphene.String(), 
                                                   NicotineAmount=graphene.String(), 
                                                   TobaccoFree=graphene.String(), 
                                                   SubOhm=graphene.String(), 
                                                   SaltNicotine=graphene.String(), 
                                                   PuffCount=graphene.String(), 
                                                   EliquidCapacity=graphene.String(),
                                                   PriceMin=graphene.Float(),
                                                   PriceMax=graphene.Float())





















    def resolve_site(root, info):
        return (
            models.Site.objects.first()
        )

    def resolve_all_products(root, info):
        return (
            models.Product.objects.all()
        )

    def resolve_product_page(root, info, productName):
        return (
            models.Product.objects.filter(product_name= productName)
        )
    def resolve_featured_list_by_name(root, info, featured_list_name):
        return (
            models.Featured_List.objects.filter(featured_list_name=featured_list_name)
        )
    def resolve_banner_list_by_name(root, info, banner_list_name):
        return (
            models.Banner_List.objects.filter(banner_list_name=banner_list_name)
        )
    def resolve_products_by_category(root, info, category):
        return(
            models.Product.objects.filter(category=category)
        )
    def resolve_all_battery_types(root, info):
        return (
            models.Battery_Type.objects.all()
            
        )
    def resolve_all_battery_sizes(root, info):
        return (
            models.Battery_Size.objects.all()
            
        )

    def resolve_all_max_wattages(root, info):
        return (
            models.Max_Wattage.objects.all()
            
        )
    
    def resolve_all_tank_capacities(root, info):
        return (
            models.Tank_Capacity.objects.all()
            
        )

    def resolve_all_tank_airflow_styles(root, info):
        return (
            models.Tank_Airflow_Style.objects.all()
            
        )
    
    def resolve_all_tank_coil_styles(root, info):
        return (
            models.Tank_Coil_Style.objects.all()
            
        )
    
    def resolve_all_tank_drip_tips(root, info):
        return (
            models.Tank_Drip_Tip.objects.all()
            
        )
    
    def resolve_all_ejuice_flavors(root, info):
        return (
            models.EJuice_Flavor.objects.all()
            
        )
    
    def resolve_all_ejuice_bottle_sizes(root, info):
        return (
            models.EJuice_Bottle_Size.objects.all()
            
        )
    
    def resolve_all_ejuice_nicotine_amounts(root, info):
        return (
            models.EJuice_Nicotine_Amount.objects.all()
            
        )
    
    def resolve_all_ejuice_tobacco_frees(root, info):
        return (
            models.EJuice_Tobacco_Free.objects.all()
            
        )
    
    def resolve_all_ejuice_sub_ohms(root, info):
        return (
            models.EJuice_Sub_Ohm.objects.all()
            
        )
    
    def resolve_all_ejuice_salt_nicotines(root, info):
        return (
            models.EJuice_Salt_Nicotine.objects.all()
            
        )
    
    def resolve_all_disposable_flavors(root, info):
        return (
            models.Disposable_Flavor.objects.all()
            
        )
    
    def resolve_all_disposable_puff_counts(root, info):
        return (
            models.Disposable_Puff_Count.objects.all()
            
        )
    
    def resolve_all_disposable_ejuice_capacities(root, info):
        return (
            models.Disposable_EJuice_Capacity.objects.all()
            
        )
    
    
    def resolve_products_filtering(root, info,
            CategoryName=None, 
            Brand=None, 
            BatteryType=None, 
            BatterySize=None, 
            MaxWattage=None, 
            Capacity=None, 
            AirflowStyle=None, 
            CoilStyle=None, 
            DripTip=None, 
            Flavor=None, 
            BottleSize=None, 
            NicotineAmount=None, 
            TobaccoFree=None, 
            SubOhm=None, 
            SaltNicotine=None, 
            PuffCount=None, 
            EliquidCapacity=None,
            PriceMin=None,
            PriceMax=None
            ):
            filters = {'category': CategoryName}
            if Brand:
                filters['brand_name'] = Brand
            if BatteryType:
                filters['device_battery_type'] = BatteryType
            if BatterySize:
                filters['device_battery_size'] = BatterySize
            if MaxWattage:
                filters['device_max_wattage'] = MaxWattage
            if Capacity:
                filters['tank_capacity'] = Capacity
            if AirflowStyle:
                filters['tank_airflow_style'] = AirflowStyle
            if CoilStyle:
                filters['tank_coil_style'] = CoilStyle
            if DripTip:
                filters['tank_drip_tip'] = DripTip
            if Flavor:
                filters['ejuice_flavor'] = Flavor
            if BottleSize:
                filters['ejuice_bottle_size'] = BottleSize
            if NicotineAmount:
                filters['ejuice_nicotine_amount'] = NicotineAmount
            if TobaccoFree:
                filters['ejuice_tobacco_free'] = TobaccoFree
            if SubOhm:
                filters['ejuice_sub_ohm'] = SubOhm
            if SaltNicotine:
                filters['ejuice_salt_nicotine'] = SaltNicotine
            if PuffCount:
                filters['disposable_puff_count'] = PuffCount
            if EliquidCapacity:
                filters['disposable_ejuice_capacity'] = EliquidCapacity
            if PriceMin:
                filters['product_price__gte'] = PriceMin
            if PriceMax:
                filters['product_price__lte'] = PriceMax

            return (
                models.Product.objects.filter(
                    **filters
                )
            )
       
        

    