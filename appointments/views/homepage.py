from django.views.generic import TemplateView


class HomePageView(TemplateView):
    """
    View to display the home page.

    """
    template_name = "index.html"
