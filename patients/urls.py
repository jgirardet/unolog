from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from patients.views import PatientViewSet

router = DefaultRouter()

router.register(r'patients', PatientViewSet)
urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^api/home/', APIHomeView.as_view({'get':'list'}), name='home'),
    # url(r'^api/admin/', APIAdminView.as_view(), name='admin'),
    # url(r'^api/admin/', APIAdminView, name='admin'),
]
