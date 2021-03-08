from rest_framework import routers

from . import views

app_name = 'accounts'

urlpatterns = []

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
urlpatterns += router.urls
