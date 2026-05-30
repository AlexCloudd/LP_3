from django.urls import path
from .views import *

app_name = 'productproject'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('plates/', PlateListView.as_view(), name='plate_list'),
    path('plates/<int:pk>/', PlateDetailView.as_view(), name='plate_detail'),
    path('artists/', ArtistListView.as_view(), name='artist_list'),
    path('artists/<int:pk>/', ArtistDetailView.as_view(), name='artist_detail'),
    path('labels/', LabelListView.as_view(), name='label_list'),
    path('labels/<int:pk>/', LabelDetailView.as_view(), name='label_detail'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('collections/', CollectionListView.as_view(), name='collection_list'),
    path('collections/<int:pk>/', CollectionDetailView.as_view(), name='collection_detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('plate/create/', PlateCreateView.as_view(), name='plate_create'),
    path('plate/<int:pk>/update/', PlateUpdateView.as_view(), name='plate_update'),
    path('plate/<int:pk>/delete/', PlateDeleteView.as_view(), name='plate_delete'),
    path('artist/create/', ArtistCreateView.as_view(), name='artist_create'),
    path('artist/<int:pk>/update/', ArtistUpdateView.as_view(), name='artist_update'),
    path('artist/<int:pk>/delete/', ArtistDeleteView.as_view(), name='artist_delete'),
    path('label/create/', LabelCreateView.as_view(), name='label_create'),
    path('label/<int:pk>/update/', LabelUpdateView.as_view(), name='label_update'),
    path('label/<int:pk>/delete/', LabelDeleteView.as_view(), name='label_delete'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/update/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
    path('collection/create/', CollectionCreateView.as_view(), name='collection_create'),
    path('collection/<int:pk>/update/', CollectionUpdateView.as_view(), name='collection_update'),
    path('collection/<int:pk>/delete/', CollectionDeleteView.as_view(), name='collection_delete'),
]
