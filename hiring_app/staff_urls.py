from django.urls import path

from hiring_app.staff_views import StaffIndex_View, View_Bookings, View_Drivers, RejectView

urlpatterns = [
    path('',StaffIndex_View.as_view()),
    path('View_Bookings',View_Bookings.as_view()),
    path('View_Drivers',View_Drivers.as_view()),
    path('Reject',RejectView.as_view()),
]

def urls():
    return urlpatterns, 'staff', 'staff'