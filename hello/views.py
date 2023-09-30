from django.views.generic import TemplateView

class HelloPageView(TemplateView):
    template_name = 'hello/main.html'
    cookie_name = "dj43_view_count"

    def view_count(self):
        current_cookie_val = self.request.COOKIES.get(self.cookie_name, 0)
        return current_cookie_val

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        response.set_cookie(self.cookie_name, int(self.view_count()) + 1)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cookie_value'] = self.view_count()
        return context
