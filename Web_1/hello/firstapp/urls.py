from django.urls import path
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    # path('', home, name='home'),
    path('', index),
    path('create/', create),
    path('edit/<int:id>/', edit),
    path('delete/<int:id>/', delete),
    path('login/', login),
    path('about/', TemplateView.as_view(template_name="firstapp/about.html")),
    path('contact/', TemplateView.as_view(template_name="firstapp/contact.html",
                                          extra_context={"work": "Разработка программных продуктов"})),
    path('details/', details),
]
