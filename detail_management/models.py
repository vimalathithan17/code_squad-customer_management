from django.db import models
from django.core.validators import MinLengthValidator
from PIL import Image
# Create your models here.
NATIONAL_ID=B_GROUPS= [
    ("Aadhar Number", "Aadhar Number"),
    ("Civil Id", "Civil Id"),
    ("PAN card", "PAN card"),
    ]
MODE=[
    ("Domestic", "Domestic"),
    ("International", "International"),
]
class Customer(models.Model):
    customer_id=models.CharField(primary_key=True,null=False,blank=False,max_length=100)
    name=models.CharField(null=False,max_length=100)
    def __str__(self):
        return f'{ self.name }-{self.customer_id}'
    
class CustomerProfile(models.Model):
    customer=models.OneToOneField(Customer,on_delete=models.CASCADE)
    nationality=models.CharField(null=False,max_length=100)
    phone_number=models.CharField(null=True,max_length=10,validators=[MinLengthValidator(10)])
    email=models.EmailField(null=False)
    passport_number=models.CharField(null=True,blank=True,max_length=100)
    national_id_type=models.CharField(null=False,max_length=100,choices=NATIONAL_ID)
    national_id=models.CharField(max_length=100)
    address=models.TextField(null=False)
    profile_image=models.ImageField(default='default.jpg',upload_to='profile_images',blank=True,null=True)

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img=Image.open(self.profile_image.path)
        if img.height>200 or img.width > 200:
            output_size=(200,200)
            img.thumbnail(output_size)
            img.save(self.profile_image.path)
    def __str__(self):
        return f'{ self.customer.name } profile'
class TravelHistory(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    start=models.CharField(null=False,max_length=100)
    destination=models.CharField(null=False,max_length=100)
    flight_number=models.CharField(null=False,max_length=100)
    year=models.CharField(null=False,max_length=4)
    mode=models.CharField(choices=MODE,max_length=100)
    def __str__(self):
        return f'{ self.customer.name } History'
    
