from django.urls import path

from hiring_app.admin_views import AdminIndex_View, user_verify, driver_verify, ApproveView, RejectView, driver_view, staff_view, user_view,\
                                    add_location, verification, staff_registration, staff_btn, View_Bookings
                                    


urlpatterns = [
    path('',AdminIndex_View.as_view(),name='admin'),
    path('user_verify',user_verify.as_view()),
    path('driver_verify',driver_verify.as_view()),
    path('verify',ApproveView.as_view()),
    path('reject',RejectView.as_view()),
    path('driver_view',driver_view.as_view()),
    path('staff_view',staff_view.as_view()),
    path('user_view',user_view.as_view()),
    path('add_location',add_location.as_view()),
    path('verification',verification.as_view()),
    path('staff_registration',staff_registration.as_view()),
    path('staff_btn',staff_btn.as_view()),
    path('View_Bookings',View_Bookings.as_view()),
]

def urls():
    return urlpatterns, 'admin', 'admin'