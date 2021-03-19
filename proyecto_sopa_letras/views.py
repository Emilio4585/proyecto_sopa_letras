from django.views.generic.base import TemplateView

class Template(TemplateView):
    template_name='index.html'
    def get_context_data(self, *args, **kwargs):
        #context = super(Home. self).get_context_data(*args, **kwargs)
        context = {
            'Dato1': '1',
            'Dato2': '2',
            'Dato3': '3',
            'Dato4': '4',
            'Dato5': '5',
            'Dato6': '6',
            'Dato7': '7',
            'Dato8': '8',
            'Dato9': '9',
            'Dato10': '10',
        }
        return context
