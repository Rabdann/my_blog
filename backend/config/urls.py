from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from my_blog.views import CategoryViewSet, ArticleViewSet
from custom_auth.views import RegisterAPIView, LoginAPIView, LogoutAPIView, PersonalCabinetAPIView


router = routers.SimpleRouter()
router.register('categories', CategoryViewSet, "category")
router.register('articles', ArticleViewSet, "article")

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('register/', RegisterAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('logout/', LogoutAPIView.as_view()),
    path('account/', PersonalCabinetAPIView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
