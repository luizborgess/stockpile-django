from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("item/new", views.new_item),
    path("item/create", views.create_item),
    # novos:
    path("item/<int:item_id>/add", views.add_qty),
    path("item/<int:item_id>/remove", views.remove_qty),
]
