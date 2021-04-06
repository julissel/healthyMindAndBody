from django.urls import path
import useraccounts.views as views


app_name = 'useraccounts'

urlpatterns = [
    path('', views.StudentsGroup.as_view(), name='groups'),
    path('student/<int:pk>/', views.Student.as_view(), name='student'),
]
