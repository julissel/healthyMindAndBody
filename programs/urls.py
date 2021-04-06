from django.urls import path
import programs.views as views
from programs.forms import CourseCreateView, CourseUpdateView, CourseDeleteView

app_name = 'programs'

urlpatterns = [
    path('', views.index, name='index'),
    path('courses/', views.CoursesListView.as_view(), name='courses'),
    path('course/<int:pk>/', views.CourseItem.as_view(), name='course'),
    path('addcourse/', CourseCreateView.as_view(), name='addcourse'),
    path('course/<int:pk>/update', CourseUpdateView.as_view(), name='update'),
    path('course/<int:pk>/delete', CourseDeleteView.as_view(), name='delete'),
]
