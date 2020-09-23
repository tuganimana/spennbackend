from django.urls import path,include
from django.http import HttpResponse
from .import views
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('', views.home,name='home'),
    path('moneysendapi/', views.moneysendapi, name='moneysend'),
    path('users/create', CreateUserView.as_view()),
    path('byose/', UserViewSet.as_view()),

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)