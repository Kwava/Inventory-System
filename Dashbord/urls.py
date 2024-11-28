
from django.urls import path
from Dashbord.views import index, product, order, staff,delete_product,update_product,staff_detail


urlpatterns = [
    path('dashbord/', index, name='Dashbord-index'),
    path('product', product, name='Dashbord-product'),
    path('product/update/<int:pk>/', update_product, name='update-product'),
    path('product/delete/<int:pk>/', delete_product, name='delete-product'),
    path('order', order, name='Dashbord-order'),
    path('staff', staff, name='Dashbord-staff'),
    path('staff/detail/<int:pk>/', staff_detail, name='Dashbord-staff-detail'),
    
]
 