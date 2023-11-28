from django.urls import path, include
from .views import homepage
from .views import CourseView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'course', CourseView)

urlpatterns = [
    path('', homepage, name='homepage'),
    path('api/', include(router.urls))
]
