from django.shortcuts import redirect, render
from django.views.generic import TemplateView, View
from django.contrib.auth.models import User

from hiring_app.models import staff_reg, driver_reg, user_reg, location, UserType, trips

# Create your views here.

class AdminIndex_View(TemplateView):
    template_name="admin/index.html"

class staff_btn(TemplateView):
    template_name="admin/staff_btn.html"

class staff_registration(TemplateView):
    template_name="admin/staff_register.html"
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
        pincode=request.POST['pincode']
        print(pincode)
        address=request.POST['address']
        print(address)
        try:
            user = User.objects.create_user(first_name=first_name,email=email,password=password,username=username,last_name='1')
            table_staff=staff_reg()
            table_staff.user =user
            table_staff.mobile =mobile
            table_staff.con_password =con_password
            table_staff.address =address
            table_staff.pincode =pincode
            table_staff.save()
            usertype = UserType()
            usertype.user = user
            usertype.type ='staff'
            usertype.save()
            return render(request,'index.html',{'message':'successfully registered'})
        except:
            messages = "Enter Another Username, user already exist"
            return render(request,'admin/index.html',{'message':messages})


class user_verify(TemplateView):
    template_name="admin/user_verify.html"

    def get_context_data(self, **kwargs):
        context = super(user_verify,self).get_context_data(**kwargs)

        app_staff = user_reg.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1')

        context['app_staff'] = app_staff
        return context
    
class driver_verify(TemplateView):
    template_name="admin/driver_verify.html"

    def get_context_data(self, **kwargs):
        context = super(driver_verify,self).get_context_data(**kwargs)

        app_driver = driver_reg.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1')

        context['app_driver'] = app_driver
        return context
    
class ApproveView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.save()
        return redirect('/admin')

class RejectView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        User.objects.get(pk=id).delete()
        return redirect('/admin')
    

class driver_view(TemplateView):
    template_name="admin/driver_view.html"

    def get_context_data(self, **kwargs):
        context = super(driver_view,self).get_context_data(**kwargs)

        app_driver = driver_reg.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1')

        context['app_driver'] = app_driver
        return context
    

class staff_view(TemplateView):
    template_name="admin/staff_view.html"

    def get_context_data(self, **kwargs):
        context = super(staff_view,self).get_context_data(**kwargs)

        app_staff = staff_reg.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1')

        context['app_staff'] = app_staff
        return context
    

class user_view(TemplateView):
    template_name="admin/user_view.html"

    def get_context_data(self, **kwargs):
        context = super(user_view,self).get_context_data(**kwargs)

        app_user = user_reg.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1')

        context['app_user'] = app_user
        return context
    
class add_location(TemplateView):
    template_name="admin/add_location.html"
    def post(self,request,*arg,**kwargs):
        name=request.POST['location']
        print(name)

        table_loc=location()
        table_loc.location =name
        table_loc.save()
           
        return render(request,'admin/index.html',{'messages':'successfully registered'})
    
class verification(TemplateView):
    template_name="admin/verification_btn.html"


class View_Bookings(TemplateView):
    template_name="admin/view_booking.html"
    def get_context_data(self, **kwargs):
        context = super(View_Bookings,self).get_context_data(**kwargs)

        book = trips.objects.all()

        context['book'] = book
        return context