from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Plate, Artist, Label, Category, Collection
from .forms import PlateForm, ArtistForm, LabelForm, CategoryForm, CollectionForm


class HomeView(TemplateView):
    template_name = 'home.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class CartView(TemplateView):
    template_name = 'cart.html'

class PlateListView(ListView):
    model = Plate
    template_name = 'plates/plate_list.html'
    context_object_name = 'plates'

class PlateDetailView(DetailView):
    model = Plate
    template_name = 'plates/plate_detail.html'
    context_object_name = 'plate'

class PlateCreateView(CreateView):
    model = Plate
    form_class = PlateForm
    template_name = 'plates/plate_form.html'
    success_url = reverse_lazy('productproject:plate_list')  

class PlateUpdateView(UpdateView):
    model = Plate
    form_class = PlateForm
    template_name = 'plates/plate_form.html'
    success_url = reverse_lazy('productproject:plate_list')

class PlateDeleteView(DeleteView):
    model = Plate
    template_name = 'plates/plate_confirm_delete.html'
    success_url = reverse_lazy('productproject:plate_list')

class ArtistListView(ListView):
    model = Artist
    template_name = 'artists/artist_list.html'
    context_object_name = 'artists'


class ArtistDetailView(DetailView):
    model = Artist
    template_name = 'artists/artist_detail.html'
    context_object_name = 'artist'


class ArtistCreateView(CreateView):
    model = Artist
    form_class = ArtistForm
    template_name = 'artists/artist_form.html'
    success_url = reverse_lazy('productproject:artist_list')

class ArtistUpdateView(UpdateView):
    model = Artist
    form_class = ArtistForm
    template_name = 'artists/artist_form.html'
    success_url = reverse_lazy('productproject:artist_list')

class ArtistDeleteView(DeleteView):
    model = Artist
    template_name = 'artists/artist_confirm_delete.html'
    success_url = reverse_lazy('productproject:artist_list')

class LabelListView(ListView):
    model = Label
    template_name = 'labels/label_list.html'
    context_object_name = 'labels'

class LabelDetailView(DetailView):
    model = Label
    template_name = 'labels/label_detail.html'
    context_object_name = 'label'

class LabelCreateView(CreateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/label_form.html'
    success_url = reverse_lazy('productproject:label_list')

class LabelUpdateView(UpdateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/label_form.html'
    success_url = reverse_lazy('productproject:label_list')

class LabelDeleteView(DeleteView):
    model = Label
    template_name = 'labels/label_confirm_delete.html'
    success_url = reverse_lazy('productproject:label_list')

class CategoryListView(ListView):
    model = Category
    template_name = 'categories/category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'categories/category_detail.html'
    context_object_name = 'category'

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories/category_form.html'
    success_url = reverse_lazy('productproject:category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories/category_form.html'
    success_url = reverse_lazy('productproject:category_list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'categories/category_confirm_delete.html'
    success_url = reverse_lazy('productproject:category_list')
 
class CollectionListView(ListView):
    model = Collection
    template_name = 'collections/collection_list.html'
    context_object_name = 'collections'

class CollectionDetailView(DetailView):
    model = Collection
    template_name = 'collections/collection_detail.html'
    context_object_name = 'collection'

class CollectionCreateView(CreateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'collections/collection_form.html'
    success_url = reverse_lazy('productproject:collection_list')

class CollectionUpdateView(UpdateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'collections/collection_form.html'
    success_url = reverse_lazy('productproject:collection_list')

class CollectionDeleteView(DeleteView):
    model = Collection
    template_name = 'collections/collection_confirm_delete.html'
    success_url = reverse_lazy('productproject:collection_list')