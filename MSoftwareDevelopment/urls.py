from django.urls import path
from .views import*
app_name="DFramework"
urlpatterns = [
      path('framework',frameworks,name="framework"),
      path('framework/<int:pk>/<slug:slug>',frameworkdetail,name="framework-detail"),
      path('framework/framework-detail/topic/<int:pk>/<str:slug>',topicdetail,name="topic-detail"),
]
