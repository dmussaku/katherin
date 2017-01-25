from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from .forms import CityForm
from .models import City, Image


class CityListView(ListView):
    model = City
    template_name = 'realestate/cities-list.html'


class CityFormView(FormView):
    model = City
    form_class = CityForm
    template_name = 'realestate/cities-create.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        files = request.FILES.getlist('file')

        if form.is_valid():
            for f in files:
                pass
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
