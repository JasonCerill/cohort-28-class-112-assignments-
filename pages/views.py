from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "pages/home.hmtl"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"
