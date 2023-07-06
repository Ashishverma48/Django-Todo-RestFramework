from django.urls import path,include
# import router
from rest_framework.routers import DefaultRouter
#import TodoViewSet 
from api.views import TodoViewSet

# create routers.DefaultRouter() class  objects

router =DefaultRouter()
# register 
router.register(r'todo',TodoViewSet)

urlpatterns = [
    path('api/',include(router.urls)), #create route urls
    
]
