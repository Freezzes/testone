from django.urls import path
from . import views

app_name = 'm'
urlpatterns = [
    path('input/', views.show, name='index'),
    # path('<int:num>',views.)
    
]


    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:num_text>',views.show,name='show')
    