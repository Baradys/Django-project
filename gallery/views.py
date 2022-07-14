from .models import Gallery
from django.views.generic.edit import CreateView
from .forms import GalleryUploadForm


class GalleryView(CreateView):
    model = Gallery
    form_class = GalleryUploadForm
    template_name = 'gallery/load_file.html'
    success_url = '/gallery/load_image/'
