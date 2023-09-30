from django.urls import path
from django.views.generic.base import TemplateView
from . import views

app_name = "hello"
urlpatterns = [
    # path('', TemplateView.as_view(template_name='hello/main.html'), name='hello'),
    path("", views.HelloPageView.as_view(), name="index"),

]

# from django.urls import path
# from . import views
# from django.views.generic import TemplateView

# app_name='session'
# urlpatterns = [
#     path('', views.hellow_view),
# ]
