from django.urls import path
from . import views


#Esses urls vão ser usados pelo swagger para fazer requests na db
urlpatterns = [
    path('cheff/', views.Cheffs.as_view()),
    path('cheff/<str:cheff_id>/', views.CheffsDetail.as_view()),
    path('cheff/<str:cheff_id>/recipes/', views.Recipes.as_view()),
]
