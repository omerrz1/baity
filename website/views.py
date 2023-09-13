from django.views.generic import TemplateView


# class based view for django template
class HomePage(TemplateView):
    template_name = 'homepage.html'


class docs(TemplateView):
    template_name = 'doc.html'

class houseDocs(TemplateView):
    template_name = 'houseDocs.html'