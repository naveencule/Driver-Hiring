from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import login
from  django.contrib.auth.models import auth,User
from django.core.files.storage import FileSystemStorage

from hiring_app.models import UserType, user_reg, driver_reg, staff_reg

# Create your views here.

class Index_View(TemplateView):
    template_name="index.html"
    def post(self,request,*args,**kwargs):
        username=request.POST['username']
        print(username)
        password =request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not  None:
            login(request,user)
            if user.last_name=='1':
                if user.is_superuser:
                    return redirect('/admin')
                elif UserType.objects.get(user_id=user.id).type=="driver":
                    return redirect('/driver')
                elif UserType.objects.get(user_id=user.id).type == "staff":
                    return redirect('/staff')
                elif UserType.objects.get(user_id=user.id).type == "user":
                    return redirect('/user')
                else:
                    return render(request,'index.html',{'message':" User Account Not Authenticated"})

            else:
                return render(request,'index.html',{'message':" User Account Not Authenticated"})
        else:
            return render(request,'index.html',{'message':"Invalid Username or Password"})
        

class user_registration(TemplateView):
    template_name="user_register.html"
    def post(self,request,*arg,**kwargs):
        first_name=request.POST['first_name']
        print(first_name)
        mobile=request.POST['mobile']
        print(mobile)
        email=request.POST['email']
        print(email)
        username=request.POST['username']
        print(username)
        password=request.POST['password']
        print(password)
        con_password=request.POST['con_password']
        print(con_password)
        try:
            user = User.objects.create_user(first_name=first_name,email=email,password=password,username=username,last_name='1')
            table_user=user_reg()
            table_user.user =user
            table_user.mobile =mobile
            table_user.con_password =con_password
            table_user.save()
            usertype = UserType()
            usertype.user = user
            usertype.type ='user'
            usertype.save()
            return render(request,'index.html',{'messages':'successfully registered'})
        except:
            messages = "Enter Another Username, user already exist"
            return render(request,'index.html',{'message':messages})
        

class driver_registration(TemplateView):
    template_name="driver_register.html"
    def post(self,request,*arg,**kwargs):
        first_name=request.POST['first_name']
        print(first_name)
        mobile=request.POST['mobile']
        print(mobile)
        email=request.POST['email']
        print(email)
        username=request.POST['username']
        print(username)
        password=request.POST['password']
        print(password)
        con_password=request.POST['con_password']
        print(con_password)
        experience=request.POST['experience']
        print(experience)
        pincode=request.POST['pincode']
        print(pincode)
        address=request.POST['address']
        print(address)
        veh_type=request.POST['car_type']
        print(veh_type)
        license_no=request.FILES['license_no']
        fii=FileSystemStorage()
        filesss=fii.save(license_no.name,license_no)
        image=request.FILES['image']
        fii1=FileSystemStorage()
        filesss1=fii1.save(image.name,image)
        try:
            user = User.objects.create_user(first_name=first_name,email=email,password=password,username=username,last_name='0')
            table_driver=driver_reg()
            table_driver.user =user
            table_driver.mobile =mobile
            table_driver.con_password =con_password
            table_driver.experience =experience
            table_driver.license_no =filesss
            table_driver.image =filesss1
            table_driver.address =address
            table_driver.pincode =pincode
            table_driver.veh_type =veh_type
            table_driver.status ='available'
            table_driver.save()
            usertype = UserType()
            usertype.user = user
            usertype.type ='driver'
            

            usertype.save()
            return render(request,'index.html',{'message':'successfully registered'})
        except:
            messages = "Enter Another Username, user already exist"
            return render(request,'index.html',{'message':messages})
        

        

