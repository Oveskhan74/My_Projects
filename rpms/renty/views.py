from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib.auth import authenticate,login,logout
from renty.models import *
from django.contrib.auth.models import User
import pdb
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest



# from .models import Files
# Create your views here.

def home(request):
    # if request.user.is_anonymous:
    #     return redirect("/register")
    return render(request,"index.html")

def register(request):
    if request.method == 'GET':
        return render(request, "form.html")
    elif request.method == 'POST':
        fullname = request.POST.get('full_name')
        email_id = request.POST.get('email')
        pass_word = request.POST.get('password')
        uploaded_image = request.FILES.get('pro_img')
        print(uploaded_image)
        
        # reg_obj = registration.objects.create(full_name = fullname, email = email_id, password = pass_word)
        user = User.objects.create_user(fullname, email_id, pass_word)
        user_profile = Profile(user=user, image=uploaded_image )
        
        user_profile.save()
        login(request,user)


        return redirect('/')

def user_login(request):
    if request.method == 'GET':
        return render(request, "form.html")
    elif request.method == 'POST':
        username = request.POST.get('Username')
        pass_word = request.POST.get('password')
        user = authenticate(username = username, password = pass_word)
        

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request,"form.html")

@login_required(login_url='register')
def user_logout(request):
    logout(request)
    return redirect('/')



def contact_page(request):
    return render(request, "contact.html")


def contact(request):
    if request.method == 'GET':
        return render(request, "contact.html")
    elif request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("mail")
        phone = request.POST.get("phone")
        subject = request.POST.get("sub")
        msg = request.POST.get("msg")

        con_us = contact_us.objects.create(fullname = name, email = email,phone = phone, subject = subject, message = msg)
        con_us.save()
        return redirect('/contact-us')

def addproperty(request):
    return render(request, 'add_property.html')



def propdetail(request):
    if request.method == 'GET':
        return render(request, "add_property.html")
    elif request.method == 'POST':
        full_name = request.POST.get("name")
        DOB = request.POST.get("dob")
        mail = request.POST.get("email")
        mobile = request.POST.get("mob")
        gen = request.POST.get("gender")
        occupation = request.POST.get("occupation")
        id_type = request.POST.get("id_type")
        id_num = request.POST.get("id_num")
        issue_auth = request.POST.get("issue_auth")
        issue_state = request.POST.get("issue_state")
        issue_date = request.POST.get("issue_date")
        exp = request.POST.get("exp_date")
        # add_type = request.POST.get("add_type")
        # nat = request.POST.get("nat")
        # state = request.POST.get("state")
        # dist = request.POST.get("district")
        # bl_no = request.POST.get("bl_no")
        price = request.POST.get("price")
        prop_type = request.POST.get("prop_type")
        bed_no = request.POST.get("bed_no")
        flr = request.POST.get("floor")
        area = request.POST.get("area")
        address = request.POST.get("address")
        tenant = request.POST.get("tenant")
        image_1 = request.FILES["img1"]
        # image_2 = request.FILES["img2"]
        # image_3 = request.FILES["img3"]
        # image_4 = request.FILES["img4"]

        city = request.POST.get("city")
        

        

        obj_prop_detail = Property_Details.objects.create(fullname=full_name,dob=DOB,email=mail,mob_number=mobile,gender=gen,Occupation=occupation,id_type=id_type,id_num=id_num,issue_auth=issue_auth,issue_state=issue_state,issue_date=issue_date,exp_date=exp,price=price,prop_type=prop_type,bedroom_no=bed_no,floors=flr,area=area,address=address,tenant_type=tenant,prop_img1=image_1,city=city)
        
        obj_prop_detail.save()
        return redirect("/add-property-form")



def rent(request):
    return render(request,"rent_info.html")


def all_prop(request):
    prop_list = Property_Details.objects.all()
    return render(request,"property_listing.html",{'prop_list':prop_list}) 


razorpay_client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))



def prop_detail_view(request,id):
    prop = Property_Details.objects.get(id=id) 
    

    currency = 'INR'
    amount = 20000  # Rs. 200
 
    # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=amount,currency=currency,payment_capture='0'))
 
    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'paymenthandler/'
 
    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url
    context['prop'] = prop
    return render(request,"rent_info.html",context)


# def prop_list(request):
#     searched = request.POST.get("search")
#     prop = Property_Details.objects.filter(prop_type__contains=searched)

#     return render(request, "property_listing.html",{"prop":prop})

def apart(request):
    prop_list = Property_Details.objects.filter(prop_type__contains="apartment")
    return render(request,"property_listing.html",{'prop_list':prop_list}) 

def villa(request):
    prop_list = Property_Details.objects.filter(prop_type__contains="villa")
    return render(request,"property_listing.html",{'prop_list':prop_list}) 

def flat(request):
    prop_list = Property_Details.objects.filter(prop_type__contains="flat")
    return render(request,"property_listing.html",{'prop_list':prop_list}) 

def office(request):
    prop_list = Property_Details.objects.filter(prop_type__contains="office")
    return render(request,"property_listing.html",{'prop_list':prop_list}) 

def building(request):
    prop_list = Property_Details.objects.filter(prop_type__contains="building")
    return render(request,"property_listing.html",{'prop_list':prop_list}) 

def farmhouse(request):
    prop_list = Property_Details.objects.filter(prop_type__contains="farmhouse")
    return render(request,"property_listing.html",{'prop_list':prop_list}) 

def shop(request):
    prop_list = Property_Details.objects.filter(prop_type__contains="shop")
    return render(request,"property_listing.html",{'prop_list':prop_list}) 

def garage(request):
    prop_list = Property_Details.objects.filter(prop_type__contains="garage")
    return render(request,"property_listing.html",{'prop_list':prop_list}) 



def tc(request):
    return render(request,"tc.html")
def firstprop(request):
    return render(request,"firstprop.html")

def search(request):
    p_type = request.POST.get("prop_type")
    t_type = request.POST.get("tenant_type")
    loc = request.POST.get("location")

    prop_list = Property_Details.objects.filter(prop_type__contains=p_type,tenant_type__contains=t_type,city__contains=loc) 
    return render(request,"property_listing.html",{'prop_list':prop_list})







def homepage(request):
    currency = 'INR'
    amount = 20000  # Rs. 200
 
    # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=amount,currency=currency,payment_capture='0'))
 
    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'paymenthandler/'
 
    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url
 
    return render(request, 'rent_info.html', context=context)
 
 
# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@csrf_exempt
def paymenthandler(request):
 
    # only accept POST request.
    if request.method == "POST":
        try:
           
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(params_dict)
            if result is not None:
                amount = 20000
                try:
 
                    # capture the payemt
                    razorpay_client.payment.capture(payment_id, amount)
 
                    # render success page on successful caputre of payment
                    return render(request, 'paymentsuccess.html')
                except:
 
                    # if there is an error while capturing payment.
                    return render(request, 'paymentfail.html')
            else:
 
                # if signature verification fails.
                return render(request, 'paymentfail.html')
        except:
 
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
       # if other than POST request is made.
        return HttpResponseBadRequest()