from django.views.generic.base import TemplateView

class Template(TemplateView):
    template_name='index.html'
    def get_context_data(self, *args, **kwargs):
        #context = super(Home. self).get_context_data(*args, **kwargs)
        context = {
            'Dato1': 'analisis',
            'Dato2': 'sintesis',
            'Dato3': 'the take away',
            'Dato4': 'historias de usuarios',
            'Dato5': 'Mapa de empatia',
            'Dato6': 'Personas',
            'Dato7': 'Definicion del problema ',
            'Dato8': 'etapa de definición',
        }
        return context
