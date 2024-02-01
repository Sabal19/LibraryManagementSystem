from django.urls import path
from . import views

from .generics import ModelListCreateView, ModelUpdateDeleteView, DetailModelUpdateDeleteView


from .mixins import CreateListMixinView ,UpdateDeleteMixinView



urlpatterns=[
    


    #Generic API View ----> This is also extension of model apiview
    path('',ModelListCreateView.as_view(),name='genericapiview'),
    path('genericapiview/<str:pk>',ModelUpdateDeleteView.as_view(),name='genericapiviewupdate'),
    path('detailgenericapiview/<str:pk>',DetailModelUpdateDeleteView.as_view(),name='genericapiviewdetailupdate'),
    

    # Generic Mixin view ---> combination of genericapiview, mixins, and concrete views
    path('mixinview',CreateListMixinView.as_view(),name='mixinview'),
    path('mixinview/<str:pk>', UpdateDeleteMixinView.as_view(),name='mixinviewupdate'),

]
