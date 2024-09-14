
from django.urls import path
from .views import HomePageView,Product_DetailViews,CommentForms_views,faveriteForm,Faverite_items
# from .views import Filter_home_page_star

urlpatterns = [
    
    path('',HomePageView, name='homepage'),
    path('size-wise-filter/<str:size_slug>',HomePageView, name='SizeWise_Filter'),
    path('color-wise-filter/<str:color_slug>',HomePageView, name='SizeWise_Filter'),
    path('Cloth-wise-filter/<int:id>',Product_DetailViews, name='product_detail'), 
    path('Comment/<int:id>',CommentForms_views, name='CommentForms_views'),
    path('Faverite/<int:id>',faveriteForm, name='faveriteForm'),
    path('Faverite-items',Faverite_items, name='Faverite_items'),
    path('Faverite-items/<int:id>',Faverite_items, name='Faverite_items'),
    # path('Home-page-star-filter/<int:id>',Filter_home_page_star, name='Filter_home_page_star' )
    
]
