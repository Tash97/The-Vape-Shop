from django.db import models
from django.contrib.auth.models import AbstractUser


class Site(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    logo = models.ImageField(upload_to='site/logo/')

    class Meta:
        verbose_name = 'site'
        verbose_name_plural = '1. Site'

    def __str__(self):
        return self.name


# New user model
class User(AbstractUser):
    avatar = models.ImageField(
        upload_to='users/avatars/%Y/%m/%d/',
        default='users/avatars/default.jpg'
    )
    bio = models.TextField(max_length=500, null=True)
    location = models.CharField(max_length=30, null=True)
    website = models.CharField(max_length=100, null=True)
    joined_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = '2. Users'

    def __str__(self):
        return self.username
    

class Battery_Type(models.Model):
    option = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.option


class Battery_Size(models.Model):
    option = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.option

class Max_Wattage(models.Model):
    option = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.option
    
class Tank_Capacity(models.Model):
    option = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.option
    
class Tank_Airflow_Style(models.Model):
    option = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.option
    
class Tank_Coil_Style(models.Model):
    option = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.option
    
class Tank_Drip_Tip(models.Model):
    option = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.option
        
class EJuice_Flavor(models.Model):
    option = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.option
    
class EJuice_Bottle_Size(models.Model):
    option = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.option
    
class EJuice_Nicotine_Amount(models.Model):
    option = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.option
    
class EJuice_Tobacco_Free(models.Model):
    option = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.option
    
class EJuice_Sub_Ohm(models.Model):
    option = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.option
    
class EJuice_Salt_Nicotine(models.Model):
    option = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.option

class Disposable_Flavor(models.Model):
    option = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.option
    
class Disposable_Puff_Count(models.Model):
    option = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.option
    
class Disposable_EJuice_Capacity(models.Model):
    option = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.option

    
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.FloatField(default=1)
    brand_name = models.ForeignKey(
        "Brand",
        related_name="BrandName",
        default="",
        to_field="name",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    category_choices = {
        "starter_kits": "Starter Kits",
        "devices": "Devices",
        "tanks": "Tanks",
        "accessories": "Accessories",
        "e-liquids": "E-Liquids",
        "alternatives": "Alternatives",
        "disposables": "Disposables",
    }

    category = models.CharField(
        max_length=20,
        choices= category_choices,
        blank=True,
        default="e-liquids",
        null=True,
    )

    device_battery_type = models.ForeignKey(
        "Battery_Type",
        related_name="BatteryType",
        default="",
        on_delete=models.CASCADE,
        to_field="option",
        null=True,
        blank=True
    )
    device_battery_size = models.ForeignKey(
        "Battery_size",
        related_name="BatterySize",
        default="",
        on_delete=models.CASCADE,
        to_field="option",
        null=True,
        blank=True
    )

    device_max_wattage = models.ForeignKey(
        "Max_Wattage",
        related_name="MaxWattage",
        default="",
        on_delete=models.CASCADE,
        to_field="option",
        null=True,
        blank=True
    )

    tank_capacity = models.ForeignKey(
        "Tank_Capacity",
        related_name="TankCapity",
        default="",
        on_delete=models.CASCADE,
        to_field="option",
        null=True,
        blank=True
    )

    tank_airflow_style = models.ForeignKey(
        "Tank_Airflow_Style",
        related_name="TankAirflowStyle",
        default="",
        on_delete=models.CASCADE,
        to_field="option",
        null=True,
        blank=True
    )

    tank_coil_style = models.ForeignKey(
        "Tank_Coil_Style",
        related_name="TankCoilStyle",
        default="",
        on_delete=models.CASCADE,
        to_field="option",
        null=True,
        blank=True
    )

    tank_drip_tip = models.ForeignKey(
        "Tank_Drip_Tip",
        related_name="TankDripTip",
        default="",
        on_delete=models.CASCADE,
        to_field="option",
        null=True,
        blank=True
    )

    ejuice_flavor = models.ForeignKey(
        "EJuice_Flavor",
        related_name="EJuiceFlavor",
        default="",
        on_delete=models.CASCADE,
        to_field="option",
        null=True,
        blank=True
    )

    ejuice_bottle_size = models.ForeignKey(
        "EJuice_Bottle_Size",
        related_name="EJuiceBottleSize",
        default="",
        on_delete=models.CASCADE,
        to_field="option",
        null=True,
        blank=True
    )

    ejuice_nicotine_amount = models.ForeignKey(
        "EJuice_Nicotine_Amount",
        related_name="EJuiceNicotineAmount",
        default="",
        on_delete=models.CASCADE,
        to_field="option",
        null=True,
        blank=True
    )

    ejuice_tobacco_free = models.ForeignKey(
        "EJuice_Tobacco_Free",
        related_name="EJuiceTobaccoFree",
        default="",
        on_delete=models.CASCADE,
        to_field="option",
        null=True,
        blank=True
    )

    ejuice_sub_ohm = models.ForeignKey(
        "EJuice_Sub_Ohm",
        related_name="EJuiceSubOhm",
        default="",
        on_delete=models.CASCADE,
        to_field="option",
        null=True,
        blank=True
    )

    ejuice_salt_nicotine = models.ForeignKey(
        "EJuice_Salt_Nicotine",
        related_name="EJuiceSaltNicotine",
        default="",
        on_delete=models.CASCADE,
        to_field="option",
        null=True,
        blank=True
    )

    disposable_flavor = models.ForeignKey(
        "Disposable_Flavor",
        related_name="DisposableFlavor",
        default="",
        on_delete=models.CASCADE,
        to_field="option",
        null=True,
        blank=True
    )

    disposable_puff_count = models.ForeignKey(
        "Disposable_Puff_Count",
        related_name="DisposablePuffCount",
        default="",
        on_delete=models.CASCADE,
        to_field="option",
        null=True,
        blank=True
    )

    disposable_ejuice_capacity = models.ForeignKey(
        "Disposable_EJuice_Capacity",
        related_name="DisposableEJuiceCapacity",
        default="",
        on_delete=models.CASCADE,
        to_field="option",
        null=True,
        blank=True
    )


    product_inventory = models.IntegerField()
    product_options1_title = models.CharField(max_length=200, default='', blank=True)
    product_options1_option1 = models.CharField(max_length=200, default='', blank=True)
    product_options1_option2 = models.CharField(max_length=200, default='', blank=True)
    product_options1_option3 = models.CharField(max_length=200, default='', blank=True)
    product_options1_option4 = models.CharField(max_length=200, default='', blank=True)
    product_options1_option5 = models.CharField(max_length=200, default='', blank=True)
    product_options2_title = models.CharField(max_length=200, default='', blank=True)
    product_options2_option1 = models.CharField(max_length=200, default='', blank=True)
    product_options2_option2 = models.CharField(max_length=200, default='', blank=True)
    product_options2_option3 = models.CharField(max_length=200, default='', blank=True)
    product_options2_option4 = models.CharField(max_length=200, default='', blank=True)
    product_options2_option5 = models.CharField(max_length=200, default='', blank=True)
    slug = models.SlugField()
    description = models.TextField()
    banner_image = models.ImageField(
        upload_to='banners/%Y/%m/%d/', blank=True, default=''
    )
    featured_image1 = models.ImageField(
                upload_to='product/main_images/%Y/%m/%d/', blank=True, default='')
    featured_image2 = models.ImageField(
                upload_to='product/main_images/%Y/%m/%d/', blank=True, default='')
    featured_image3 = models.ImageField(
                upload_to='product/main_images/%Y/%m/%d/', blank=True, default='')
    featured_image4 = models.ImageField(
                upload_to='product/main_images/%Y/%m/%d/', blank=True, default='')
    featured_image5 = models.ImageField(
                upload_to='product/main_images/%Y/%m/%d/', blank=True, default='')
    tag = models.ManyToManyField("Tag")




    class Meta:
        verbose_name = 'product'
        verbose_name_plural = '5. Products'

    def __str__(self):
        return self.product_name
    

    
class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True)
    tag = models.ManyToManyField('Tag')

    def __str__(self):
        return self.name


    

class Banner_List(models.Model):
    banner_list_name = models.CharField(max_length=100)
    banner_1 = models.ForeignKey(
        "Product",
        on_delete=models.CASCADE,
        related_name="Banner_1",
        default="",
        limit_choices_to=~models.Q(banner_image = ''),
    )
    banner_2 = models.ForeignKey(
        "Product",
        on_delete=models.CASCADE,
        related_name="Banner_2",
        default="",
        limit_choices_to=~models.Q(banner_image = ''),

    )
    banner_3 = models.ForeignKey(
        "Product",
        on_delete=models.CASCADE,
        related_name="Banner_3",
        default="",
        limit_choices_to=~models.Q(banner_image = ''),

    )
    banner_4 = models.ForeignKey(
        "Product",
        on_delete=models.CASCADE,
        related_name="Banner_4",
        default="",
        limit_choices_to=~models.Q(banner_image = ''),
    )
    
class Featured_List(models.Model):
    featured_list_name = models.CharField(max_length=100)
    featured_product_1 = models.ForeignKey(
        "Product",
        on_delete=models.CASCADE,
        related_name="Featured_Product_1",
        default="",
    )
    featured_product_2 = models.ForeignKey(
        "Product",
        on_delete=models.CASCADE,
        related_name="Featured_product_2",
        default="",
    )
    featured_product_3 = models.ForeignKey(
        "Product",
        on_delete=models.CASCADE,
        related_name="Featured_product_3",
        default="",
    )
    featured_product_4 = models.ForeignKey(
        "Product",
        on_delete=models.CASCADE,
        related_name="Featured_product_4",
        default="",
    )
    featured_product_5 = models.ForeignKey(
        "Product",
        on_delete=models.CASCADE,
        related_name="Featured_product_5",
        default="",
    )
    featured_product_6 = models.ForeignKey(
        "Product",
        on_delete=models.CASCADE,
        related_name="Featured_product_6",
        default="",
    )
    featured_product_7 = models.ForeignKey(
        "Product",
        on_delete=models.CASCADE,
        related_name="Featured_product_7",
        default="",
    )
    featured_product_8 = models.ForeignKey(
        "Product",
        on_delete=models.CASCADE,
        related_name="Featured_product_8",
        default="",
    )
    featured_product_9 = models.ForeignKey(
        "Product",
        on_delete=models.CASCADE,
        related_name="Featured_product_9",
        default="",
    )
    featured_product_10 = models.ForeignKey(
        "Product",
        on_delete=models.CASCADE,
        related_name="Featured_product_10",
        default="",
    )

    
