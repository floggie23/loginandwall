from django.shortcuts import render , redirect ,HttpResponse
from django.contrib import messages 
import bcrypt
from .models import *


def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    quantity_from_form = int(request.POST["quantity"])
    price_from_form = float(request.POST["price"])
    total_charge = quantity_from_form * price_from_form
    print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    return render(request, "store/checkout.html")

def login(request):
    if "userid" in request.session :
        id=request.session['userid']
        return redirect("/success/"+str(id))
    return render(request, "login.html")

def create(request):
    
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect("/login")
    else :
        password=request.POST['pass']
        re_pass =request.POST['re_pass']
        if password==re_pass :
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            print(pw_hash) 
            user= User.objects.create(first_name=request.POST['name'],email=request.POST['email'],last_name=request.POST['last_name'],password=pw_hash)
        return redirect("/login")
def signin(request):
    user = User.objects.filter(email=request.POST['email2'])
    if user:
        logged_user = user[0] 
        if bcrypt.checkpw(request.POST['password2'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            return redirect('/success/'+str(logged_user.id))
    return redirect("/login")
def success(request,id):
    user =User.objects.get(id=id)
    message=Message.objects.all()
    context = {
        "user": user ,
        "messages": message,
    }
    return render(request, "succes.html",context)
def logout(request):
    request.session.flush()
    return redirect("/login")

def createmessage(request,id):
    message= Message.objects.create(text=request.POST['message'],user_id=id)
    return redirect("/success/"+str(id))

def createcomment(request,id,smsid):
    comment= Comment.objects.create(comment=request.POST['comment'],user_id=id,message_id=smsid)
    return redirect("/success/"+str(id))



