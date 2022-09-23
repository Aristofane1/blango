# other imports
from . import views
from django.urls import path

urlpatterns = [
    # other patterns
    path("", views.index)
]