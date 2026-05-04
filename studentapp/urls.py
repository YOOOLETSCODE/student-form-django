from django.urls import path
# from .views import registration
# from .views import student_list

from .import views

urlpatterns = [
    path('', views.registration, name='registration'),
    path('students/', views.student_list, name='student_list'),
    path('student/<int:id>/update/', views.student_update, name='student_update'),
    path('student/<int:id>/delete/', views.student_delete, name='student_delete'),
]