from django.views.generic import TemplateView


# class based view for django template
class HomePage(TemplateView):
    template_name = 'homepage.html'