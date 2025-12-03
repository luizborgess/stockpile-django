from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("item/new", views.new_item),
    path("item/create", views.create_item),
    path("item/<int:item_id>/delete", views.delete_item, name="delete_item"),

    # novos:
    path("item/<int:item_id>/add", views.add_qty),
    path("item/<int:item_id>/remove", views.remove_qty),
# NOVAS ROTAS
    path('item/<int:id>/add10', views.add_10, name='add_10'),
    path('item/<int:id>/sub10', views.sub_10, name='sub_10'),
]
