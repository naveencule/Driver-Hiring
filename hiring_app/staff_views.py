from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.contrib.auth.models import User

from hiring_app.models import trips, driver_reg

# Create your views here.

class StaffIndex_View(TemplateView):
    template_name="staff/index.html"

class View_Bookings(TemplateView):
    template_name="staff/view_booking.html"
    def get_context_data(self, **kwargs):
        context = super(View_Bookings,self).get_context_data(**kwargs)

        book = trips.objects.all()

        context['book'] = book
        return context
    
    
class View_Drivers(TemplateView):
    template_name="staff/view_drivers.html"
    def get_context_data(self, **kwargs):
        context = super(View_Drivers,self).get_context_data(**kwargs)

        drv = driver_reg.objects.all()

        context['drv'] = drv
        return context
    
class RejectView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.is_active='0'
        user.save()
        return render(request,'admin/index.html',{'message':"Rejected"})