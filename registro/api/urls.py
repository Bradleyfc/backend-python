from rest_framework.routers import DefaultRouter
from registro.api.views import RegistroViewSet


router = DefaultRouter()
router.register('registro' , RegistroViewSet, basename = 'registro' )
urlpatterns = router.urls

