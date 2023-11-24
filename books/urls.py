from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [

]

router = DefaultRouter()

router.register('', views.BookViewSet)
urlpatterns += router.urls
