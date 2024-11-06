from django.urls import path
from saude.adapters.http.consultation_controller import ConsultationController
from saude.adapters.http.professional_controller import ProfessionalController

urlpatterns = [
    path('professional/create', ProfessionalController.create_professional),
    path('professional/list-all', ProfessionalController.list_all_professionals),
    path('professional/<str:id>/list', ProfessionalController.list_professional),
    path('professional/<str:id>/delete',
         ProfessionalController.delete_professional),
    path('professional/<str:id>/update',
         ProfessionalController.update_professional),



    path('consultation/create', ConsultationController.create_consultation),
    path('consultation/list-all', ConsultationController.list_all_consultations),
    path('consultation/<str:id>/list', ConsultationController.list_consultation),
    path('consultation/<str:id>/delete',
         ConsultationController.delete_consultation),
    path('consultation/<str:id>/update',
         ConsultationController.update_consultation),
]
