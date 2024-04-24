from django.urls import path

from hiring_app.user_views import UserIndex_View, view_drivers, book_trip, view_trip, payment

urlpatterns = [
    path('',UserIndex_View.as_view()),
    path('view_drivers',view_drivers.as_view()),
    path('book_trip',book_trip.as_view()),
    path('view_trip',view_trip.as_view()),
    path('payment',payment.as_view()),
]

def urls():
    return urlpatterns, 'user', 'user'