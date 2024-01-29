from django.contrib import admin

# Register your models here.
from .models import HistoriaModel, ConsultaModel, OperacionesModel, ComplementariosModel, ProcederesModel, \
    ProcederesRealizadosModel

admin.site.register(HistoriaModel)
admin.site.register(ConsultaModel)
admin.site.register(OperacionesModel)
admin.site.register(ComplementariosModel)
admin.site.register(ProcederesModel)
admin.site.register(ProcederesRealizadosModel)
