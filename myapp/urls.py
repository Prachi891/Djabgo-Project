from django.contrib import admin
from django.urls import path
from myapp import views


urlpatterns = [
    path('addnewmember/',views.addnewmember,name='addnewmember'),
    path('contact/',views.contact,name='contact'),
    path('prachi/',views.prachi,name='prachi'),
    path('main/',views.main,name='main'),
    path('image/',views.image,name='image'),
    path('hello/',views.hello,name='hello'),
    path('newmember/',views.newmember,name='newmember'),
    path('main/hello/<int:id>',views.hello,name='hello'),
    path('main/hello/update/<int:id>/',views.update,name='update'),
    path('main/hello/delete/<int:id>/',views.delete,name='delete'),

]