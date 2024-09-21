from rest_framework.routers import DefaultRouter 
from django.urls import path, include 
from .views import PatientViewSet, AppointmentViewSet 

router = DefaultRouter()
router.register(r'Patients', PatientViewSet)
router.register(r'Appointment', AppointmentViewSet)

urlpatterns = [
    path('', include(router.urls))
]

