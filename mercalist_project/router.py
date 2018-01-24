from rest_framework.routers import SimpleRouter
from mercalistAPI.API.resources import UsuarioViewSet
from django.urls import path, include

router = SimpleRouter()
router.register(r'usuarios', viewset=UsuarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
