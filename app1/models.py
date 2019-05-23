from django.db import models


class Shopkeeper(models.Model):
    shopkeeper_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=254)
    photo = models.ImageField(upload_to='image/shopkeeper', null=True)
    phone_no = models.IntegerField(null=True)
    address = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.shopkeeper_name + ' ' + self.password + ' ' + self.email


class Shop(models.Model):
    Type_Of_Shop = (
         ('Electronics', 'Electronics'),
         ('Fashion', 'Fashion'), ('Photo & Gifts', 'Photo & Gifts'),
         ('Home Decor', 'Home Decor'),
         ('Sports', 'Sports'),
         ('Food', 'Food'),
         ('All', 'All')
    )
    shopkeeper = models.ForeignKey(Shopkeeper, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=50)
    shop_address = models.CharField(max_length=500)
    shop_type = models.CharField(max_length=50, choices=Type_Of_Shop, default='All')
    shop_image = models.ImageField(upload_to='image/shop')
    shop_rating = models.IntegerField()

    def __str__(self):
        return self.shop_name


class Product(models.Model):
    Type_Of_Product = (
         ('Electronics', 'Electronics'),
         ('Fashion', 'Fashion'), ('Photo & Gifts', 'Photo & Gifts'),
         ('Home Decor', 'Home Decor'),
         ('Sports', 'Sports'),
         ('Food', 'Food'),
         ('etc', 'etc')
    )
    from_shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    product_Image = models.ImageField(upload_to='image/products')
    product_Image1 = models.ImageField(upload_to='image/products')
    product_Image2 = models.ImageField(upload_to='image/products')
    product_type = models.CharField(max_length=50, choices=Type_Of_Product, default='Nice')
    product_name = models.CharField(max_length=200)
    product_cost = models.IntegerField()
    product_sale = models.IntegerField()
    product_rating = models.IntegerField()
    product_in_stock = models.BooleanField(default=True)
    product_description = models.CharField(max_length=500)
    product_wish_list = models.BooleanField(default=False)

    def __str__(self):
        return self.product_name


class Consumer(models.Model):
    user_name = models.CharField(max_length=255)
    user_email = models.CharField(max_length=255)
    user_password = models.CharField(max_length=255)
    user_photo = models.ImageField(upload_to='image/user', width_field=250, height_field=300)
    phone_no = models.IntegerField()
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.user_name


class PurchaseId(models.Model):
    number_of_items = models.IntegerField()
    total_price = models.IntegerField()


class Purchase(models.Model):
    purchase_id = models.OneToOneField(PurchaseId, on_delete=models.CASCADE)
    user_id = models.OneToOneField(Consumer, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id.user_name
