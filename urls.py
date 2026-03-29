from django.urls import path
from . import views

urlpatterns = [
    path('Salom/', views.salom_view),
    path('Xanifa/', views.xanifa_view),
    path('Admin/', views.Index),
    path('bubble/', views.bubble_view, name='bubble'),
    path('selection/', views.selection_view, name='selection'),
    path('qidirish' , views.qidirish_view , name = 'qidirish' ) ,
     path('saralash' , views.saralash , name = 'saralash' ) ,
]