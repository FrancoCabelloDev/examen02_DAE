from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarpetaViewSet, EtiquetaViewSet, NotaViewSet, DocumentoViewSet

router = DefaultRouter()
router.register('carpetas', CarpetaViewSet)
router.register('etiquetas', EtiquetaViewSet)
router.register('notas', NotaViewSet)
router.register('documentos', DocumentoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
