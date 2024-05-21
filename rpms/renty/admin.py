from django.contrib import admin
from renty.models import contact_us,Profile,Property_Details

# Register your models here.
admin.site.register(Profile)
admin.site.register(contact_us)
admin.site.register(Property_Details)