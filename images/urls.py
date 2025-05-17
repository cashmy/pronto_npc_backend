from django.urls import path, include
from images import views

urlpatterns = [
    path("", views.images_list),
    path("<int:pk>/", views.image_detail),
    path("options/<str:image_type>/<int:owner>/", views.image_select_options),
]
