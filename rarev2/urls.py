from django.conf.urls import include
from rarev2api.views import register_user, check_user
from django.contrib import admin
from rarev2api.views.post import PostView
from django.contrib import admin
from django.urls import path
from rarev2api.views.rare_user import RareUserView
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', RareUserView, 'user')
router.register (r'posts', PostView, 'post')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('register', register_user),
    path('checkuser', check_user),
]
