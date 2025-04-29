from django.urls import path
from age_category import views

urlpatterns = [
    path("", views.age_category_list, name="age_category_list"),
    path("<int:pk>/", views.age_category_detail, name="age_category_detail"),
    path("options/", views.age_category_options, name="age_category_options"),
]
