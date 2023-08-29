from django.urls import path
from . import views
urlpatterns = [
    path('select/',views.select,name='select'),
    path('create_customer/',views.create_customer,name='create_customer'),
    path('view_customer/',views.view_customer,name='view_customer'),
    path('to_view_customer/',views.to_view_customer,name='to_view_customer'),
    path('create_profile/',views.create_profile,name='create_profile'),
    path('update_profile/',views.update_profile,name='update_profile'),
    path('add_travel/',views.add_travel,name='add_travel'),

    

]
