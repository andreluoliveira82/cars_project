from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import HomeView, NewBrandCreateView, CarsListView, NewCarCreateView, CarDetailView, CarUpdateView, CarDeleteView
from accounts.views import register_view, login_view, logout_view

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("", HomeView.as_view()),
    path("home/", HomeView.as_view(), name="home"),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("new_brand/", NewBrandCreateView.as_view(), name="new_brand"),
    path("cars/", CarsListView.as_view(), name="cars_list"),
    path("new_car/", NewCarCreateView.as_view(), name="new_car"),
    path("car/<int:pk>/", CarDetailView.as_view(), name="car_detail"),
    path("car/<int:pk>/update/", CarUpdateView.as_view(),name="car_update"),
    path("car/<int:pk>/delete", CarDeleteView.as_view(),name="car_delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
