from django.urls import path

# from .views import ListTodo,DetailTodo

# urlpatterns = [
#     path('',ListTodo.as_view()),
#     path('<int:pk>/',DetailTodo.as_view()),
# ]


from .views import KayitViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('',KayitViewSet,basename='kayitlarimiz')

urlpatterns = router.urls
