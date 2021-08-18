from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

# Create your models here.
CATEGORY=[
    ('Stationary','Stationary'),
    ('Electronics','Electronics'),
    ('Food','Food')
]

class Product(models.Model):
    name=models.CharField(max_length=100,null=True)
    category=models.CharField(max_length=20,choices=CATEGORY,null=True)
    quantity=models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return f'{self.name}-{self.quantity}'

@receiver(post_save,sender=Product)
def total(sender,instance,created,**kwargs):
    product=Product.objects.get(id=instance.id)
    if created:
        instance.total_price=product.quantity*product.price    
        instance.save()
    else:#if you want to update field
        total_price=product.quantity*product.price 
        product=Product.objects.filter(id=instance.id).update(total_price=total_price)
        
post_save.connect(total,sender=Product)


class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    staff=models.ForeignKey(User,models.CASCADE,null=True)
    order_quantity=models.PositiveBigIntegerField(null=True)
    date=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='Staff Product' # means instead of Order i will show on django admin as Staff Product Table' 

    def __str__(self):
        return f"{self.product} ordered by {self.staff.username}"

class FileUpload(models.Model):
    file_upload=models.FileField(upload_to='documents')
