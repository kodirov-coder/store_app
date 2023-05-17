from django.urls import path

from .views import ProductsListView, add_to_basket, del_from_basket

urlpatterns = [
    path("", ProductsListView.as_view(), name="products-page"),
    path("/category/<int:category_id>", ProductsListView.as_view(), name="category"),
    path("/page/<int:page>", ProductsListView.as_view(), name="paginator"),
    path("/baskets/add/<int:product_id>", add_to_basket, name="add-to-basket"),
    path("/baskets/remove/<int:basket_id>", del_from_basket, name="del_from_basket"),
]