from django.urls import path
from . import views

urlpatterns = [
  # path('',VistaPaginaHome.as_view(), name='home'),
  path('',views.login, name='login')

]
