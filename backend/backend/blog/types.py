import graphene
from graphene_django import DjangoObjectType
from blog import models


class SiteType(DjangoObjectType):
    class Meta:
        model = models.Site


class UserType(DjangoObjectType):
    class Meta:
        model = models.User


class Featured_ListType(DjangoObjectType):
    class Meta:
        model = models.Featured_List



class Banner_ListType(DjangoObjectType):
    class Meta:
        model = models.Banner_List




class ProductType(DjangoObjectType):
    class Meta:
        model = models.Product

class TagType(DjangoObjectType):
    class Meta:
        model = models.Tag



class  BrandType(DjangoObjectType):
    class Meta:
        model = models.Brand

class Battery_TypeType(DjangoObjectType):
    class Meta:
        model = models.Battery_Type

class Battery_SizeType(DjangoObjectType):
    class Meta:
        model = models.Battery_Size

class Max_WattageType(DjangoObjectType):
    class Meta:
        model = models.Max_Wattage

class Tank_CapacityType(DjangoObjectType):
    class Meta:
        model = models.Tank_Capacity

class Tank_Airflow_StyleType(DjangoObjectType):
    class Meta:
        model = models.Tank_Airflow_Style

class Tank_Coil_StyleType(DjangoObjectType):
    class Meta:
        model = models.Tank_Coil_Style

class Tank_Drip_TipType(DjangoObjectType):
    class Meta:
        model = models.Tank_Drip_Tip

class EJuice_FlavorType(DjangoObjectType):
    class Meta:
        model = models.EJuice_Flavor

class EJuice_Bottle_SizeType(DjangoObjectType):
    class Meta:
        model = models.EJuice_Bottle_Size

class EJuice_Nicotine_AmountType(DjangoObjectType):
    class Meta:
        model = models.EJuice_Nicotine_Amount

class EJuice_Tobacco_FreeType(DjangoObjectType):
    class Meta:
        model = models.EJuice_Tobacco_Free

class EJuice_Sub_OhmType(DjangoObjectType):
    class Meta:
        model = models.EJuice_Sub_Ohm

class EJuice_Salt_NicotineType(DjangoObjectType):
    class Meta:
        model = models.EJuice_Salt_Nicotine

class Disposable_FlavorType(DjangoObjectType):
    class Meta:
        model = models.Disposable_Flavor

class Disposable_Puff_CountType(DjangoObjectType):
    class Meta:
        model = models.Disposable_Puff_Count

class Disposable_EJuice_CapacityType(DjangoObjectType):
    class Meta:
        model = models.Disposable_EJuice_Capacity