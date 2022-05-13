from django.urls import path
from .views import*
app_name="Courses"
urlpatterns = [
      path('courses',CoursesView.as_view(),name="courses"),
      path('courses/<int:pk>/<slug:slug>',coursedetail,name="course-detail"),
      path('courses/course-detail/topic/<int:pk>/<slug:slug>',topicdetail,name="topic-detail"),
]
