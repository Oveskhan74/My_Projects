from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile") # Delete profile when user is deleted
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile' #show how we want it to be displayed

class contact_us(models.Model):
    fullname = models.CharField( max_length=100,null=False,blank=False)
    email = models.CharField( max_length=100,null=False,blank=False)
    phone = models.CharField( max_length=100,null=False,blank=False)
    subject = models.CharField( max_length=100,null=False,blank=False)
    message = models.CharField( max_length=100,null=False,blank=False)

    def __str__(self):
        return self.fullname

class Property_Details(models.Model):
    fullname = models.CharField( max_length=100,null=False,blank=False)
    dob = models.DateField( max_length=100,null=False,blank=False)
    email = models.CharField( max_length=100,null=False,blank=False)
    mob_number = models.CharField( max_length=100,null=False,blank=False)
    gender = models.CharField( max_length=100,null=False,blank=False) 
    Occupation = models.CharField( max_length=100,null=False,blank=False)
    id_type = models.CharField( max_length=100,null=False,blank=False)
    id_num = models.CharField( max_length=100,null=False,blank=False)
    issue_auth = models.CharField( max_length=100,null=False,blank=False)
    issue_state = models.CharField( max_length=100,null=False,blank=False)
    issue_date = models.DateField( max_length=100,null=False,blank=False)
    exp_date = models.DateField( max_length=100,null=False,blank=False)
#    1 add_type = models.CharField( max_length=100,null=False,blank=False)
#     1nationality = models.CharField( max_length=100,null=False,blank=False)
#    1 state = models.CharField( max_length=100,null=False,blank=False)
#    1 district = models.CharField( max_length=100,null=False,blank=False)
#    1 block_no = models.CharField( max_length=100,null=False,blank=False)
    price = models.CharField( max_length=100,null=False,blank=False)
    prop_type = models.CharField( max_length=100,null=False,blank=False)
    bedroom_no = models.CharField( max_length=100,null=False,blank=False)
    floors = models.CharField( max_length=100,null=False,blank=False)
    area = models.CharField( max_length=100,null=False,blank=False)
    address = models.CharField( max_length=100,null=False,blank=False)
    tenant_type = models.CharField( max_length=100,null=False,blank=False)
    prop_img1 = models.ImageField(null=True, blank=True, upload_to='property')
    # prop_img2 = models.ImageField(null=True, blank=True, upload_to='property')
    # prop_img3 = models.ImageField(null=True, blank=True, upload_to='property')
    # prop_img4 = models.ImageField(null=True, blank=True, upload_to='property')
    
    city = models.CharField( max_length=100,null=True,blank=False)

    def __str__(self):
        return self.fullname
    
    # class Files(models.Model):
    #     file = models.FileField(upload_to='file')
    
