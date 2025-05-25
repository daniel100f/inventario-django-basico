from rest_framework import routers
from cliente.api.views import CustomerViewSet

router = routers.DefaultRouter()
router.register('customers',CustomerViewSet,basename='customer')

urlpatterns=router.urls
