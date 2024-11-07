from django.urls import path, include
from rest_framework.routers import DefaultRouter
from saude.adapters.http.consultation_controller import ConsultationController
from saude.adapters.http.professional_controller import ProfessionalController

# Criando o roteador
router = DefaultRouter()

# Registrando os ViewSets com os respectivos basenames
router.register(r'professional', ProfessionalController,
                basename='professional')
router.register(r'consultation', ConsultationController,
                basename='consultation')

# Incluindo as rotas do roteador no urlpatterns
urlpatterns = [
    path('', include(router.urls)),
]
