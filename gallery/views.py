from .models import Gallery
from django.views.generic import CreateView, ListView
from .forms import GalleryUploadForm


class GalleryView(CreateView):
    model = Gallery
    form_class = GalleryUploadForm
    template_name = 'gallery/load_file.html'
    success_url = '/gallery/load_image/'


class ListGallery(ListView):
    model = Gallery
    template_name = 'gallery/list_file.html'
    context_object_name = 'records'
