from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter
from unologbase.views import PatientViewSet


router = SimpleRouter()
router.register(r'patients', PatientViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^api/home/', APIHomeView.as_view({'get':'list'}), name='home'),
    # url(r'^api/admin/', APIAdminView.as_view(), name='admin'),
    # url(r'^api/admin/', APIAdminView, name='admin'),
]
