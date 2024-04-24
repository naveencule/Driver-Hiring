from django.urls import path

from hiring_app.driver_views import DriverIndex_View, View_Bookings, ApproveView, RejectView, add_payment, Trip_completed

urlpatterns = [
    path('',DriverIndex_View.as_view()),
    path('View_Bookings',View_Bookings.as_view()),
    path('ApproveView',ApproveView.as_view()),
    path('RejectView',RejectView.as_view()),
    path('add_payment',add_payment.as_view()),
    path('Trip_completed',Trip_completed.as_view()),
]

def urls():
    return urlpatterns, 'driver', 'driver'