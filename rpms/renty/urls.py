from django.contrib import admin
from django.urls import path, include
from renty import views

urlpatterns = [
    path("",views.home,name='home'),
    path("contact",views.contact,name='contact'),
    path("register",views.register,name='register'),
    path("login",views.user_login,name='user_login'),
    path("logout",views.user_logout,name='user_logout'),
    path("add-property-form",views.addproperty,name='addprop_page'),
    path("contact-us",views.contact_page,name='conpage'),
    path("add-property-submit",views.propdetail,name='addprop_submit'),
    path("rentinfo",views.rent,name='rent_details'),
    path("properties",views.all_prop,name='all_property'),
    path("propdetails/<int:id>",views.prop_detail_view,name='property_details'),
    path("apartment",views.apart,name='propert_apartment'),
    path("villa",views.villa,name='propert_villa'),
    path("flat",views.flat,name='propert_flat'),
    path("office",views.office,name='propert_office'),
    path("building",views.building,name='propert_building'),
    path("farmhouse",views.farmhouse,name='propert_farmhouse'),
    path("shop",views.shop,name='propert_shop'),
    path("garage",views.garage,name='propert_garage'),
    path("terms",views.tc,name='terms_Conditions'),
    path("firstp",views.firstprop,name='first_prop'),
    path("search",views.search,name="searched_prop"),
    path('paymenthandler', views.paymenthandler, name='paymenthandler'),
    
    
]
