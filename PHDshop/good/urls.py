from django.urls import path
from .views import GoodListView, GetDetailFromID, GetListViewFromCategory, GetListViewFromBrand

urlpatterns = [
    path('api/goods/list', GoodListView.as_view(), name='good-list'),
    path('api/goods/<int:pk>/detail', GetDetailFromID.as_view(), name='good-detail'),
    path('api/goods/<int:category_id>/getByCategoryId', GetListViewFromCategory.as_view(), name='good-by-category'),
    path('api/goods/<int:brand_id>/getByBrandId', GetListViewFromBrand.as_view(), name='good-by-brand')
]