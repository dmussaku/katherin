
from rest_framework import routers

from .api import AuthViewSet


router = routers.SimpleRouter()
router.register(r'auth', AuthViewSet, base_name='auth')
