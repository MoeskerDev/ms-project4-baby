"""
URLS related to the profiles app
"""
from django.urls import path
from . import views

urlpatterns = [
     path('', views.profile, name='profile'),
     path('order_history/<order_number>',
          views.order_history, name='order_history'),
     path('wishlist/', views.wishlist, name='wishlist'),
     path('add_to_wishlist/<item_id>',
          views.add_to_wishlist, name='add_to_wishlist'),
     path('review/', views.rev, name='review'),
     path('add_review/<int:product_id>',
          views.add_rev, name='add_review'),
     path('edit_review/<int:review_id>',
          views.edit_rev, name='edit_review'),
     path('delete_review/<int:review_id>',
          views.delete_rev, name='delete_review'),
]
