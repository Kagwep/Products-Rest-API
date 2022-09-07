from django.urls import path
from . import views

urlpatterns = [
     path('',views.ProductListCreateView.as_view()),
     path('<int:pk>/',views.ProductDetailapiView.as_view()),
     path('<int:pk>/update/',views.ProductUpdateapiView.as_view()),
     path('<int:pk>/destroy/',views.ProductDestroyApiView.as_view())
     #path('',views.product_alt_view),
     #path('<int:pk>/',views.product_alt_view)
     
]
