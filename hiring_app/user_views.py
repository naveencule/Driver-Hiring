from django.shortcuts import render
from django.views.generic import TemplateView, View

from hiring_app.models import driver_reg, location, trips, user_reg

# Create your views here.

class UserIndex_View(TemplateView):
    template_name="user/index.html"

class view_drivers(TemplateView):
    template_name="user/view_drivers.html"

    def get_context_data(self, **kwargs):
        context = super(view_drivers,self).get_context_data(**kwargs)

        app_driver = driver_reg.objects.filter(status='available')

        context['app_driver'] = app_driver
        return context
    
class book_trip(TemplateView):
    template_name="user/book_trip.html"

    def get_context_data(self, **kwargs):
        context = super(book_trip,self).get_context_data(**kwargs)

        loc = location.objects.all()
        id = self.request.GET['id']
        driver = driver_reg.objects.get(id=id)
        context['loc'] = loc
        context['driver'] = driver
        return context
    
    def post(self,request,*arg,**kwargs):
        user=user_reg.objects.get(user_id=self.request.user.id)
        id = self.request.GET['id']
        driver = driver_reg.objects.get(id=id)
        name=request.POST['name']
        print(name)
        mobile=request.POST['mobile']
        print(mobile)
        from_loc=request.POST['from_loc']
        print(from_loc)
        to_loc=request.POST['to_loc']
        print(to_loc)
        time=request.POST['time']
        print(time)
        date=request.POST['date']
        print(date)
        car_type=request.POST['car_type']
        print(car_type)
        
        table_trip=trips()
        table_trip.user_id =user.id
        table_trip.driver_id =driver.id
        table_trip.mobile =mobile
        table_trip.name =name
        table_trip.pickup_place =from_loc
        table_trip.to_place =to_loc
        table_trip.time =time
        table_trip.date =date
        table_trip.car_type =car_type
        table_trip.status ="added"
        table_trip.save()
       
        return render(request,'user/index.html',{'message':'successfully registered'})
    

class view_trip(TemplateView):
    template_name="user/view_trip.html"

    def get_context_data(self, **kwargs):
        context = super(view_trip,self).get_context_data(**kwargs)
        user=user_reg.objects.get(user_id=self.request.user.id)
        trip = trips.objects.filter(user_id=user.id)

        context['trip'] = trip
        return context

class payment(TemplateView):
    template_name="user/payment_details.html"
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        com=user_reg.objects.get(user_id=self.request.user.id)

        dri= trips.objects.filter(user_id=com.id)
        context['dri']= dri
       
        return context
    
    def post(self,request,*args,**kwargs):
        id = request.POST['id']
        usr = trips.objects.get(id=id)
        usr.status="paid"
        usr.payment="paid"
        usr.save()
        return render(request,'user/index.html',{'message':"Payment successful"})