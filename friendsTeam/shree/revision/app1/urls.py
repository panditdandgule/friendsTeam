from app1.models import order,customer
from app1.views import ordercustomer,customer_
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api',ordercustomer)
urlpatterns = router.urls
