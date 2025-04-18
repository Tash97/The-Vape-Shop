from django.contrib import admin
from .models import *


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'date_joined')

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ('product_name',)

class Featured_ListAdmin(admin.ModelAdmin):
    list_display = ('featured_list_name',)

class Banner_ListAdmin(admin.ModelAdmin):
    list_display = ('banner_list_name',)

class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)

class BrandAdmin(admin.ModelAdmin):
    list_display = ("name",)

class Battery_TypeAdmin(admin.ModelAdmin):
    list_display = ("option",)


class  Battery_SizeAdmin(admin.ModelAdmin):
    list_display = ("option",)

class Max_WattageAdmin(admin.ModelAdmin):
    list_display = ("option",)


class Tank_CapacityAdmin(admin.ModelAdmin):
    list_display = ("option",)

class Tank_Airflow_StyleAdmin(admin.ModelAdmin):
    list_display = ("option",)

class Tank_Coil_StyleAdmin(admin.ModelAdmin):
    list_display = ("option",)

class Tank_Drip_TipAdmin(admin.ModelAdmin):
    list_display = ("option",)

class EJuice_FlavorAdmin(admin.ModelAdmin):
    list_display = ("option",)

class EJuice_Bottle_SizeAdmin(admin.ModelAdmin):
    list_display = ("option",)

class EJuice_Nicotine_AmountAdmin(admin.ModelAdmin):
    list_display = ("option",)

class EJuice_Tobacco_FreeAdmin(admin.ModelAdmin):
    list_display = ("option",)

class EJuice_Sub_OhmAdmin(admin.ModelAdmin):
    list_display = ("option",)

class EJuice_Salt_NicotineAdmin(admin.ModelAdmin):
    list_display = ("option",)

class Disposable_FlavorAdmin(admin.ModelAdmin):
    list_display = ("option",)

class Disposable_Puff_CountAdmin(admin.ModelAdmin):
    list_display = ("option",)

class Disposable_EJuice_CapacityAdmin(admin.ModelAdmin):
    list_display = ("option",)





admin.site.register(Site)
admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Featured_List, Featured_ListAdmin)
admin.site.register(Banner_List, Banner_ListAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Battery_Type, Battery_TypeAdmin)
admin.site.register(Battery_Size, Battery_SizeAdmin)
admin.site.register(Max_Wattage, Max_WattageAdmin)
admin.site.register(Tank_Capacity, Tank_CapacityAdmin)
admin.site.register(Tank_Airflow_Style, Tank_Airflow_StyleAdmin)
admin.site.register(Tank_Coil_Style, Tank_Coil_StyleAdmin)
admin.site.register(Tank_Drip_Tip, Tank_Drip_TipAdmin)
admin.site.register(EJuice_Flavor, EJuice_FlavorAdmin)
admin.site.register(EJuice_Bottle_Size, EJuice_Bottle_SizeAdmin)
admin.site.register(EJuice_Nicotine_Amount, EJuice_Nicotine_AmountAdmin)
admin.site.register(EJuice_Tobacco_Free, EJuice_Tobacco_FreeAdmin)
admin.site.register(EJuice_Sub_Ohm, EJuice_Sub_OhmAdmin)
admin.site.register(EJuice_Salt_Nicotine, EJuice_Salt_NicotineAdmin)
admin.site.register(Disposable_Flavor, Disposable_FlavorAdmin)
admin.site.register(Disposable_Puff_Count, Disposable_Puff_CountAdmin)
admin.site.register(Disposable_EJuice_Capacity ,Disposable_EJuice_CapacityAdmin)




