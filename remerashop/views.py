from django.views.generic import TemplateView

class CafeView(TemplateView):
    template_name = "index.html"

class login(TemplateView):
    template_name = "login.html"

class logueado(TemplateView):
    template_name = "logueado.html"