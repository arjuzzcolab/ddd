from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.CreateBook.as_view(),name='create'),
    path('auth/',views.Authentication.as_view(),name='auth'),
    path('login_user/',views.Login.as_view(),name='login'),
    path('update/<int:pk>/',views.UpdateBook.as_view(),name='update'),
    path('update_user/<int:pk>/',views.UpdateUser.as_view(),name='update_user'),
    path('details/<int:pk>/',views.DetailsBook.as_view(),name='details'),
    path('details_user/<int:pk>/',views.DetailsUser.as_view(),name='details_user'),
    path('delete/<int:pk>/',views.DeleteBook.as_view(),name='delete'),
    path('delete_user/<int:pk>/',views.DeleteUser.as_view(),name='delete_user'),


]
