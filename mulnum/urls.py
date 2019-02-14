from django.urls import path
from . import views

app_name = 'm'
urlpatterns = [
    path('input/', views.inputnum, name='index'),   # show text box
    path('<int:id>',views.show,name='mul'),         #multiplication by number in url
    path('mult/',views.mul,name='mult'),            #multiplication by number from text box
]


    