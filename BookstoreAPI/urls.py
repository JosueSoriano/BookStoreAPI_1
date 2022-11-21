from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'Author', views.AuthorViewSet)
router.register(r'Book', views.BookViewSet)
router.register(r'BookTitle', views.BookTitleViewSet)
router.register(r'AuthorName', views.AuthorNameViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
