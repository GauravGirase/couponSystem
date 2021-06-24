from django.urls import path
from demoapi import views

urlpatterns = [
    path('', views.coupans_list),
    path('coupon/<int:pk>', views.code_detail),
    path('redeem/<str:code>', views.code_redeem),

]
