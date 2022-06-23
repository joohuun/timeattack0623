from django.urls import path, include
from item import views


urlpatterns = [
    # path('', include(router.urls)),
    path('', views.ItemView.as_view()),          
]