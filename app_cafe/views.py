
from .models      import Cafe
from django.views import View
from django.urls  import reverse_lazy


from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , UpdateView , DeleteView


# Create your views here.
class CafeViewBase(View):
 template_name="Cafe.html"
 model = Cafe
 fields = "__all__"
 success_url = reverse_lazy("cafe:all")

class CafeListView(CafeViewBase, ListView):
    ...
class CafeDetailView(CafeViewBase, DetailView):
    template_name = "Cafe_detail.html"

class CafeCreateView(CafeViewBase, CreateView):
    template_name = "Cafe_create.html"
    extra_context = {
        "tipo" : "Create cafe"
    }

class CafeUpdateView(CafeViewBase, UpdateView):
   template_name = "Cafe_update.html"
   extra_context = {
        "tipo" : "Update cafe"
   }

class CafeDeleteView(CafeViewBase, DeleteView):
    template_name="Cafe_delete.html"
    extra_context = {
        "tipo" : "Delete cafe"
    }