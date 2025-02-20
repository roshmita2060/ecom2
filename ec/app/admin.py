from django.contrib import admin
from .models import Customer, Product, Cart, Payment, OrderPlaced

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discounted_price', 'category', 'product_image']


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'locality', 'city', 'state', 'zipcode']


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'get_products', 'quantity']

    # Custom method to get the products in the cart (if products is a related field)
    def get_products(self, obj):
        return ", ".join([str(product) for product in obj.products.all()])  # Assuming it's a ManyToManyField
    get_products.short_description = 'Products'


@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'amount', 'razorpay_order_id', 'razorpay_payment_status', 'get_razorpay_payment_id', 'paid']

    # Custom method for razorpay_payment_id if it's not a direct field in the Payment model
    def get_razorpay_payment_id(self, obj):
        return obj.razorpay_payment_id if obj.razorpay_payment_id else "N/A"
    get_razorpay_payment_id.short_description = 'Razorpay Payment ID'


@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer', 'get_products', 'quantity', 'ordered_date', 'status', 'get_payments']

    # Custom method for products if it's a related field
    def get_products(self, obj):
        return ", ".join([str(product) for product in obj.product.all()])  # Assuming it's a related field (ManyToMany)
    get_products.short_description = 'Products'

    # Custom method for payments if it's a related field
    def get_payments(self, obj):
        return ", ".join([str(payment) for payment in obj.payments.all()])  # Assuming it's a related field
    get_payments.short_description = 'Payments'




# from django.contrib import admin
# from . models import Customer,Product,Cart,Payment,OrderPlaced
# # Register your models here.

# @admin.register(Product)
# class ProductModelAdmin(admin.ModelAdmin):
#     list_display = ['id','title','discounted_price','category','product_image']

# @admin.register(Customer)
# class CustomerModelAdmin(admin.ModelAdmin):
#     list_display = ['id','user','locality','city','state','zipcode']    

# @admin.register(Cart)
# class CartModelAdmin(admin.ModelAdmin):
#     list_display=['id','user','products','quantity']

# @admin.register(Payment)   
# class PaymentModelAdmin(admin.ModelAdmin):
#     list_display=['id','user','amount','razorpay_order_id','razorpay_payment_status','razorpay_payment_id','paid']

# @admin.register(OrderPlaced)
# class OrderPlacedModelAdmin(admin.ModelAdmin):
#     list_display=['id','user','customer','product','quantity','ordered_date','status','payments']
