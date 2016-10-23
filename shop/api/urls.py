from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from api import views


router = DefaultRouter()
router.register(r'category_list', views.CategoryListViewSet)
router.register(r'item_list', views.ItemListViewSet)
# router.register(r'?(<item_name>\d+)/$', views.ItemDetailView.as_view())
# router.register(r'item/add', views.ItemAddView.as_view())
router.register(r'category/add', views.CategoryAddView.as_view())
router.register(r'users', views.UserViewSet)

schema_view = get_swagger_view(title='Shop API')

urlpatterns = [
    url(r'^$', schema_view),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]