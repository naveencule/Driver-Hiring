from django.shortcuts import render
from django.views.generic import TemplateView, View

from hiring_app.models import trips, driver_reg

# Create your views here.

class DriverIndex_View(TemplateView):
    template_name="driver/index.html"


class View_Bookings(TemplateView):
    template_name="driver/view_booking.html"
    def get_context_data(self, **kwargs):
        context = super(View_Bookings,self).get_context_data(**kwargs)
        com=driver_reg.objects.get(user_id=self.request.user.id)
        book = trips.objects.filter(driver_id=com.id)

        context['book'] = book
        return context
    
class ApproveView(View):
    def dispatch(self, request, *args, **kwargs):
        ad=driver_reg.objects.get(user_id=request.user.id)
        abb=driver_reg.objects.get(id=ad.id)
        id = request.GET['id']
        book = trips.objects.get(pk=id)
        book.status='approved'
        abb.status='notavailable'
        book.save()
        abb.save()
        return render(request,'driver/index.html',{'message':"Booking Approved"})

class RejectView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        book = trips.objects.get(pk=id)
        book.status='rejected'
        book.save()
        return render(request,'driver/index.html',{'message':"Booking Rejected"})

class add_payment(TemplateView):
    template_name="driver/add_payment.html"
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        com=driver_reg.objects.get(user_id=self.request.user.id)

        dri= trips.objects.filter(driver_id=com.id)
        context['dri']= dri
       
        return context

    def post(self, request, *args, **kwargs):
        id = self.request.GET['id']
        trip_amt = request.POST['trip_amt']
        kms = request.POST['kms']
        total=int(trip_amt)*int(kms)
        se=trips.objects.get(id=id)
        se.km_per_amt=trip_amt
        se.kms=kms
        se.total_amt=total
        se.status="Payment Added"
        se.save()
        return render(request, 'driver/index.html', {'message': "successfully added"})
    
class Trip_completed(View):
    def dispatch(self, request, *args, **kwargs):
        ad=driver_reg.objects.get(user_id=request.user.id)
        abb=driver_reg.objects.get(id=ad.id)
        id = request.GET['id']
        book = trips.objects.get(pk=id)
        book.status='completed'
        abb.status='available'
        book.save()
        abb.save()
        return render(request,'driver/index.html',{'message':"Booking Completed"})