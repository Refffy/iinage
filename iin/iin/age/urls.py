from django.urls import path, include
from .views import PersonIin


urlpatterns = [
    path('people/', PersonIin.as_view()),
    path('people/<iin>', PersonIin.as_view())
]
