from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    # TokenRefreshView,
)


urlpatterns = [
    path('',views.endPoints),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('advocates/',views.advocate_list, name='advocates'),
    # path('advocates/<str:username>/',views.advocate_detail),
    path('advocates/<str:username>/',views.Advocate_detail.as_view()),

    path('companies/',views.companies_list, name='companies'),
    # path('advocates/<str:username>/',views.advocate_detail),
    path('companies/<str:name>/',views.Company_detail.as_view())


]
