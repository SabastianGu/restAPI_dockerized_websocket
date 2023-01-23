from django.urls import path, include
from rest_framework import routers

from .views import *

cam_router = routers.SimpleRouter()
cam_router.register(r'cameras', CameraSet)

Laurent2_router = routers.SimpleRouter()
Laurent2_router.register(r'laurent2', Laurent2Set)

BlackListItem_router = routers.SimpleRouter()
BlackListItem_router.register(r'blackList', BlackListItemSet)

CarParkItem_router = routers.SimpleRouter()
CarParkItem_router.register(r'carPark', CarParkItemSet)

WorkingMode_router = routers.SimpleRouter()
WorkingMode_router.register(r'workingModes', WorkingModeSet)

AccessPoint_router = routers.SimpleRouter()
AccessPoint_router.register(r'AccessPoint', AccessPointSet)

urlpatterns = [
    path('', include(cam_router.urls)),
    path('', include(Laurent2_router.urls)),
    path('ledBoard/', LEDBoardSet.as_view()),
    path('', include(BlackListItem_router.urls)),
    path('blackList/<str:pk>', BlackListItemCheck.as_view()),
    path('', include(CarParkItem_router.urls)),
    path('', include(WorkingMode_router.urls)),
    path('', include(AccessPoint_router.urls)),
]
