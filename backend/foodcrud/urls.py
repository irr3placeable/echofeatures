from django.urls import path
from .views import RecipeCreateView
from .views import RecipeRequestListView
urlpatterns = [
    path('recipes/create/', RecipeCreateView.as_view(), name='recipe-create'),
    path('requests/', RecipeRequestListView.as_view(), name='recipe-request-list'),
]