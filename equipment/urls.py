from django.urls import path, include
from rest_framework import routers

from equipment.views import GPAPIView, KipAPIViewSet, KipAPIViewDetail, CopyAPIView

router = routers.DefaultRouter()
router.register(r'kip', KipAPIViewSet, basename='kip')

# print(router.urls)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/detail/', KipAPIViewDetail.as_view()),
    path('api/v1/gp/', GPAPIView.as_view()),
    path('copy/', CopyAPIView.as_view())
]
