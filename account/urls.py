from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginuser, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('waste/', views.waste, name='waste'),
    path('settings/', views.settings, name='settings'),
    path('profile/', views.profile, name='profile'),

    path('api/list/', views.WasteList.as_view(), name='api-device'),
    path('api/bin/<str:ref>/', views.BinDetail.as_view(), name='led'),
    path('api/update/<str:ref>', views.ConfigDetail.as_view(), name='api-config'),
    # path('api/config/response/<int:ref>', views.ConfigResponse.as_view(), name='api-config-response'),
]