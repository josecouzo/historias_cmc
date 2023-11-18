import json
import os
from audioop import reverse
from datetime import datetime, date, timedelta
from random import randrange

import boto3
from django.conf import settings
from django.contrib.auth.decorators import login_required, permission_required

from dateutil.relativedelta import relativedelta
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from django.template.loader import render_to_string
# from weasyprint import HTML, CSS
# from weasyprint.text.fonts import FontConfiguration

from .forms import HistoriaForm, ConsultaForm, ComplementarioForm
from .models import HistoriaModel, ConsultaModel, OperacionesModel, ComplementariosModel
from django.db.models import Q
from django.core.files.storage import FileSystemStorage


@login_required()
def render_index(request):
    return render(request, 'index.html')


@login_required()
def render_historias(request):
    return render(request, 'historias_index.html')


@login_required()
def render_PDF(request):
    return render(request, 'PDF_historia.html')


@login_required()
def render_add_historia(request):
    formHistoria = HistoriaForm
    formConsulta = ConsultaForm
    return render(request, 'historias_add.html', {'formHistoria': formHistoria, 'formConsulta': formConsulta})


@login_required()
def render_add_consulta(request, id_historia):
    historia = HistoriaModel.objects.get(pk=id_historia)
    listaOperaciones = OperacionesModel.objects.filter(historia=id_historia).order_by('anyo').all()
    edada = relativedelta(datetime.now(), historia.fecha_nacimiento)
    formHistoria = HistoriaForm
    formConsulta = ConsultaForm
    return render(request, 'consulta_add.html',
                  {'edada': edada.years, 'formHistoria': formHistoria, 'formConsulta': formConsulta,
                   'historia': historia, 'listaOperaciones': listaOperaciones})


@login_required()
def ajax_add_historia(request):
    data = json.loads(request.body.decode('utf-8'))
    new_historia = HistoriaModel()
    new_historia.nombre = data['historia']['nombre']
    new_historia.sexo = data['historia']['sexo']
    new_historia.ocupacion = data['historia']['ocupacion']
    new_historia.telefono = data['historia']['telefono']
    new_historia.fecha_nacimiento = data['historia']['fecha_nacimiento']
    new_historia.estado_civil = data['historia']['estado_civil']
    new_historia.antecedentes_familiares = data['historia']['antecedentes_familiares']
    new_historia.antecedentes_perosnales = data['consulta']['antecedentes_perosnales']
    new_historia.fumar = data['historia']['fumar']
    new_historia.alcohol = data['historia']['alcohol']
    new_historia.drogas = data['historia']['drogas']
    new_historia.transfuciones = data['historia']['transfuciones']
    new_historia.grupo_factor = data['historia']['grupo_factor']
    new_historia.save()
    for operacion in data['listaOperaciones']:
        new_operacion = OperacionesModel()
        new_operacion.historia = new_historia
        new_operacion.tipo = operacion['operacion']
        new_operacion.anyo = operacion['anyo']
        new_operacion.save()
    new_consulta = ConsultaModel()
    new_consulta.historia = new_historia
    new_consulta.motivo_consulta = data['consulta']['motivo_consulta']
    new_consulta.historia_enfermedad_actual = data['consulta']['historia_enfermedad_actual']
    new_consulta.inpresion_general = data['consulta']['inpresion_general']
    new_consulta.fc = data['consulta']['fc']
    new_consulta.ta = data['consulta']['ta']
    new_consulta.fr = data['consulta']['fr']
    new_consulta.pulso = data['consulta']['pulso']
    new_consulta.tAuxiliar = data['consulta']['tAuxiliar']
    new_consulta.tReactal = data['consulta']['tReactal']
    new_consulta.peso_habitual = data['consulta']['peso_habitual']
    new_consulta.peso_actual = data['consulta']['peso_actual']
    new_consulta.talla = data['consulta']['talla']
    new_consulta.imc = data['consulta']['imc']
    new_consulta.habito_constitucional = data['consulta']['habito_constitucional']
    new_consulta.marcha = data['consulta']['marcha']
    new_consulta.lesiones = data['consulta']['lesiones']
    new_consulta.tejido_celular_subcutaneo = data['consulta']['tejido_celular_subcutaneo']
    # new_consulta.lugar_infiltrado = data['consulta']['lugar_infiltrado']
    new_consulta.craneo_cara = data['consulta']['craneo_cara']
    new_consulta.cuero_cabelludo = data['consulta']['cuero_cabelludo']
    new_consulta.cuello_inspecion = data['consulta']['cuello_inspecion']
    new_consulta.cuello_palpitacion = data['consulta']['cuello_palpitacion']
    new_consulta.cuello_percucion = data['consulta']['cuello_percucion']
    new_consulta.cuello_auscultacion = data['consulta']['cuello_auscultacion']
    new_consulta.torax_piel = data['consulta']['torax_piel']
    new_consulta.torax_forma = data['consulta']['torax_forma']
    new_consulta.mama_forma = data['consulta']['mama_forma']
    new_consulta.mama_tamanyo = data['consulta']['mama_tamanyo']
    new_consulta.mama_simetria = data['consulta']['mama_simetria']
    new_consulta.mama_areolas = data['consulta']['mama_areolas']
    new_consulta.mama_pezones = data['consulta']['mama_pezones']
    new_consulta.murmullo_vesicular = data['consulta']['murmullo_vesicular']
    new_consulta.tiraje = data['consulta']['tiraje']
    new_consulta.ruidos_cardiovascular = data['consulta']['ruidos_cardiovascular']
    new_consulta.soplos = data['consulta']['soplos']
    new_consulta.abdomen_inspecion = data['consulta']['abdomen_inspecion']
    new_consulta.abdomen_palpacion = data['consulta']['abdomen_palpacion']
    new_consulta.abdomen_percucion = data['consulta']['abdomen_percucion']
    new_consulta.abdomen_auscultacion = data['consulta']['abdomen_auscultacion']
    new_consulta.obstetrico_maniobre_leopold = data['consulta']['obstetrico_maniobre_leopold']
    new_consulta.obstetrico_au = data['consulta']['obstetrico_au']
    new_consulta.genitourinario_percucion_lumbar = data['consulta']['genitourinario_percucion_lumbar']
    new_consulta.genitourinario_percucion_derecha = data['consulta']['genitourinario_percucion_derecha']
    new_consulta.genitourinario_percucion_izquierda = data['consulta']['genitourinario_percucion_izquierda']
    new_consulta.genitourinario_tacto_vaginal = data['consulta']['genitourinario_tacto_vaginal']
    new_consulta.genitourinario_vulva = data['consulta']['genitourinario_vulva']
    new_consulta.genitourinario_flujo = data['consulta']['genitourinario_flujo']
    new_consulta.genitourinario_cuello_uterino = data['consulta']['genitourinario_cuello_uterino']
    new_consulta.nervioso_estado = data['consulta']['nervioso_estado']
    new_consulta.nervioso_glasgow_ocular = data['consulta']['nervioso_glasgow_ocular']
    new_consulta.nervioso_glasgow_motor = data['consulta']['nervioso_glasgow_motor']
    new_consulta.nervioso_glasgow_verbal = data['consulta']['nervioso_glasgow_verbal']
    new_consulta.nervioso_conducta = data['consulta']['nervioso_conducta']
    new_consulta.nervioso_lenguaje = data['consulta']['nervioso_lenguaje']
    new_consulta.nervioso_paredes_craneales = data['consulta']['nervioso_paredes_craneales']
    new_consulta.nervioso_reflejos_fotomotor = data['consulta']['nervioso_reflejos_fotomotor']
    new_consulta.nervioso_reflejos_acomodacion = data['consulta']['nervioso_reflejos_acomodacion']
    new_consulta.nervioso_reflejos_osteotendinosos = data['consulta']['nervioso_reflejos_osteotendinosos']
    new_consulta.nervioso_motricidad = data['consulta']['nervioso_motricidad']
    new_consulta.nervioso_babinski = data['consulta']['nervioso_babinski']
    new_consulta.nervioso_sensibilidad = data['consulta']['nervioso_sensibilidad']
    new_consulta.nervioso_temblor = data['consulta']['nervioso_temblor']
    new_consulta.nervioso_romberg = data['consulta']['nervioso_romberg']
    new_consulta.nervioso_taxia = data['consulta']['nervioso_taxia']
    new_consulta.nervioso_dismetria = data['consulta']['nervioso_dismetria']
    new_consulta.nervioso_rigidez = data['consulta']['nervioso_rigidez']
    new_consulta.nervioso_fondo_ojo = data['consulta']['nervioso_fondo_ojo']
    new_consulta.osteomioarticular_columna_vertebral = data['consulta']['osteomioarticular_columna_vertebral']
    new_consulta.osteomioarticular_ejes_oseos = data['consulta']['osteomioarticular_ejes_oseos']
    new_consulta.osteomioarticular_articulaciones = data['consulta']['osteomioarticular_articulaciones']
    new_consulta.osteomioarticular_miembros = data['consulta']['osteomioarticular_miembros']
    new_consulta.osteomioarticular_trofismo_muscular = data['consulta']['osteomioarticular_trofismo_muscular']
    new_consulta.complementarios_entregados = data['consulta']['complementarios_entregados']
    new_consulta.complementarios_indicados = data['consulta']['complementarios_indicados']
    new_consulta.diagnostico_presuntivo = data['consulta']['diagnostico_presuntivo']
    new_consulta.plan_terapeutico = data['consulta']['plan_terapeutico']
    new_consulta.owner = request.user
    new_consulta.save()
    return JsonResponse({"data": new_historia.id}, status=200)


@login_required()
def ajax_add_consulta(request):
    data = json.loads(request.body.decode('utf-8'))
    new_historia = HistoriaModel.objects.get(pk=data['consulta']['id_historia'])
    new_historia.antecedentes_perosnales = data['consulta']['antecedentes_perosnales']
    new_historia.save()

    new_consulta = ConsultaModel()
    new_consulta.historia = new_historia
    new_consulta.motivo_consulta = data['consulta']['motivo_consulta']
    new_consulta.historia_enfermedad_actual = data['consulta']['historia_enfermedad_actual']
    new_consulta.inpresion_general = data['consulta']['inpresion_general']
    new_consulta.fc = data['consulta']['fc']
    new_consulta.ta = data['consulta']['ta']
    new_consulta.fr = data['consulta']['fr']
    new_consulta.pulso = data['consulta']['pulso']
    new_consulta.tAuxiliar = data['consulta']['tAuxiliar']
    new_consulta.tReactal = data['consulta']['tReactal']
    new_consulta.peso_habitual = data['consulta']['peso_habitual']
    new_consulta.peso_actual = data['consulta']['peso_actual']
    new_consulta.talla = data['consulta']['talla']
    new_consulta.imc = data['consulta']['imc']
    new_consulta.habito_constitucional = data['consulta']['habito_constitucional']
    new_consulta.marcha = data['consulta']['marcha']
    new_consulta.lesiones = data['consulta']['lesiones']
    new_consulta.tejido_celular_subcutaneo = data['consulta']['tejido_celular_subcutaneo']
    # new_consulta.lugar_infiltrado = data['consulta']['lugar_infiltrado']
    new_consulta.craneo_cara = data['consulta']['craneo_cara']
    new_consulta.cuero_cabelludo = data['consulta']['cuero_cabelludo']
    new_consulta.cuello_inspecion = data['consulta']['cuello_inspecion']
    new_consulta.cuello_palpitacion = data['consulta']['cuello_palpitacion']
    new_consulta.cuello_percucion = data['consulta']['cuello_percucion']
    new_consulta.cuello_auscultacion = data['consulta']['cuello_auscultacion']
    new_consulta.torax_piel = data['consulta']['torax_piel']
    new_consulta.torax_forma = data['consulta']['torax_forma']
    new_consulta.mama_forma = data['consulta']['mama_forma']
    new_consulta.mama_tamanyo = data['consulta']['mama_tamanyo']
    new_consulta.mama_simetria = data['consulta']['mama_simetria']
    new_consulta.mama_areolas = data['consulta']['mama_areolas']
    new_consulta.mama_pezones = data['consulta']['mama_pezones']
    new_consulta.murmullo_vesicular = data['consulta']['murmullo_vesicular']
    new_consulta.tiraje = data['consulta']['tiraje']
    new_consulta.ruidos_cardiovascular = data['consulta']['ruidos_cardiovascular']
    new_consulta.soplos = data['consulta']['soplos']
    new_consulta.abdomen_inspecion = data['consulta']['abdomen_inspecion']
    new_consulta.abdomen_palpacion = data['consulta']['abdomen_palpacion']
    new_consulta.abdomen_percucion = data['consulta']['abdomen_percucion']
    new_consulta.abdomen_auscultacion = data['consulta']['abdomen_auscultacion']
    new_consulta.obstetrico_maniobre_leopold = data['consulta']['obstetrico_maniobre_leopold']
    new_consulta.obstetrico_au = data['consulta']['obstetrico_au']
    new_consulta.genitourinario_percucion_lumbar = data['consulta']['genitourinario_percucion_lumbar']
    new_consulta.genitourinario_percucion_derecha = data['consulta']['genitourinario_percucion_derecha']
    new_consulta.genitourinario_percucion_izquierda = data['consulta']['genitourinario_percucion_izquierda']
    new_consulta.genitourinario_tacto_vaginal = data['consulta']['genitourinario_tacto_vaginal']
    new_consulta.genitourinario_vulva = data['consulta']['genitourinario_vulva']
    new_consulta.genitourinario_flujo = data['consulta']['genitourinario_flujo']
    new_consulta.genitourinario_cuello_uterino = data['consulta']['genitourinario_cuello_uterino']
    new_consulta.nervioso_estado = data['consulta']['nervioso_estado']
    new_consulta.nervioso_glasgow_ocular = data['consulta']['nervioso_glasgow_ocular']
    new_consulta.nervioso_glasgow_motor = data['consulta']['nervioso_glasgow_motor']
    new_consulta.nervioso_glasgow_verbal = data['consulta']['nervioso_glasgow_verbal']
    new_consulta.nervioso_conducta = data['consulta']['nervioso_conducta']
    new_consulta.nervioso_lenguaje = data['consulta']['nervioso_lenguaje']
    new_consulta.nervioso_paredes_craneales = data['consulta']['nervioso_paredes_craneales']
    new_consulta.nervioso_reflejos_fotomotor = data['consulta']['nervioso_reflejos_fotomotor']
    new_consulta.nervioso_reflejos_acomodacion = data['consulta']['nervioso_reflejos_acomodacion']
    new_consulta.nervioso_reflejos_osteotendinosos = data['consulta']['nervioso_reflejos_osteotendinosos']
    new_consulta.nervioso_motricidad = data['consulta']['nervioso_motricidad']
    new_consulta.nervioso_babinski = data['consulta']['nervioso_babinski']
    new_consulta.nervioso_sensibilidad = data['consulta']['nervioso_sensibilidad']
    new_consulta.nervioso_temblor = data['consulta']['nervioso_temblor']
    new_consulta.nervioso_romberg = data['consulta']['nervioso_romberg']
    new_consulta.nervioso_taxia = data['consulta']['nervioso_taxia']
    new_consulta.nervioso_dismetria = data['consulta']['nervioso_dismetria']
    new_consulta.nervioso_rigidez = data['consulta']['nervioso_rigidez']
    new_consulta.nervioso_fondo_ojo = data['consulta']['nervioso_fondo_ojo']
    new_consulta.osteomioarticular_columna_vertebral = data['consulta']['osteomioarticular_columna_vertebral']
    new_consulta.osteomioarticular_ejes_oseos = data['consulta']['osteomioarticular_ejes_oseos']
    new_consulta.osteomioarticular_articulaciones = data['consulta']['osteomioarticular_articulaciones']
    new_consulta.osteomioarticular_miembros = data['consulta']['osteomioarticular_miembros']
    new_consulta.osteomioarticular_trofismo_muscular = data['consulta']['osteomioarticular_trofismo_muscular']
    new_consulta.complementarios_entregados = data['consulta']['complementarios_entregados']
    new_consulta.complementarios_indicados = data['consulta']['complementarios_indicados']
    new_consulta.diagnostico_presuntivo = data['consulta']['diagnostico_presuntivo']
    new_consulta.plan_terapeutico = data['consulta']['plan_terapeutico']
    new_consulta.owner = request.user
    new_consulta.save()
    return JsonResponse({"data": new_historia.id}, status=200)


@login_required()
def historias_ajax(request):
    data = []
    # if request.user.userdata.is_admin:
    #     phones__ = HistoriaModel.objects.filter(admin=request.user).order_by('-id').all()
    # else:
    historias__ = HistoriaModel.objects.all()

    historias_ = historias__
    # SEARCH
    search = request.GET.get('search[value]')
    if search:
        historias_ = historias_.filter(Q(id__icontains=search) | Q(date_of_creation__icontains=search)
                                       | Q(nombre__icontains=search) | Q(ocupacion__icontains=search)
                                       | Q(estado_civil__icontains=search) | Q(grupo_factor__icontains=search))
    # ID
    try:
        id_historia = int(request.GET.get('columns[0][search][value]'))
    except ValueError:
        id_historia = None
    if id_historia:
        historias_ = historias_.filter(id=id_historia)

    #  Nombre
    nombre = request.GET.get('columns[1][search][value]')
    if nombre:
        historias_ = historias_.filter(nombre__icontains=nombre)

    #  Nombre
    telefono = request.GET.get('columns[3][search][value]')
    if telefono:
        historias_ = historias_.filter(telefono__icontains=telefono)

    totalFilter = historias_.count()

    # # ORDER
    # col_dict = {
    #     '0': 'id',
    #     '1': 'date_of_creation',
    #     '2': 'owner',
    #     '4': 'price_provider',
    #     '5': 'price',
    #     '6': 'client',
    #     '7': 'status',
    # }
    # try:
    #     descending = request.GET.get('order[0][dir]') == 'desc'
    #     col_index = request.GET.get(f'order[0][column]')
    #     col_name = col_dict[col_index]
    #     order_str = f"-{col_name}" if descending else col_name
    #     historias_ = historias_.order_by(order_str)
    # except KeyError:
    #     historias_ = historias_.order_by('-date_of_creation')

    # PAGINATION
    start = request.GET.get('start')
    length = request.GET.get('length')
    if int(length) >= 0:
        historias_ = historias_[int(start):int(start) + int(length)]

    for historia in historias_:
        historia_response = {
            "id": historia.id,
            "nombre": historia.nombre,
            "sexo": historia.sexo,
            "telefono": historia.telefono,
            "grupo_factor": historia.grupo_factor,
            "estado_civil": historia.estado_civil,
            "ocupacion": historia.ocupacion,
            "edad": (relativedelta(datetime.now(), historia.fecha_nacimiento).years),
            "operaciones": [p.to_dic for p in historia.operaciones.all()],
            "consultas": [p.to_dic for p in historia.conusltas.all()],
            "date_of_creation": historia.date_of_creation.strftime('%d/%m/%Y %H:%M:%S'),
        }
        data.append(historia_response)
    return JsonResponse({"data": data, 'recordsFiltered': totalFilter, 'recordsTotal': historias__.count(),
                         'draw': request.GET.get('draw')})


@login_required()
def hoja_cargo_ajax(request):
    data = []
    # if request.user.userdata.is_admin:
    #     phones__ = HistoriaModel.objects.filter(admin=request.user).order_by('-id').all()
    # else:
    consultas__ = ConsultaModel.objects.all().filter(owner_id=request.user.id)

    consultas_ = consultas__
    # SEARCH
    search = request.GET.get('search[value]')
    if search:
        consultas_ = consultas_.filter(Q(id__icontains=search) | Q(date_of_creation__icontains=search)
                                       )
    # ID
    try:
        id_historia = int(request.GET.get('columns[0][search][value]'))
    except ValueError:
        id_historia = None
    if id_historia:
        consultas_ = consultas_.filter(id=id_historia)

    print(request.GET)
    print("----------------888888----------")
    #  Nombre
    nombre = request.GET.get('columns[1][search][value]')
    if nombre:
        consultas_ = consultas_.filter(historia__nombre__icontains=nombre)

    #  Telefono
    telefono = request.GET.get('columns[4][search][value]')
    if telefono:
        consultas_ = consultas_.filter(historia__telefono__icontains=telefono)

    print(request.GET.get('columns[7][search][value]'))
    print("Hola")
    #  Fecha
    rango_fecha = request.GET.get('columns[7][search][value]')
    if rango_fecha:
        fechasplit = rango_fecha.split("|")
        consultas_ = consultas_.filter(date_of_creation__range=(fechasplit[0], fechasplit[1]))

    totalFilter = consultas_.count()

    # PAGINATION
    start = request.GET.get('start')
    length = request.GET.get('length')
    if int(length) >= 0:
        historias_ = consultas_[int(start):int(start) + int(length)]
    idx = 1
    for consula in consultas_:
        historia_response = {
            "count": idx,
            "id": consula.id,
            "nombre": consula.historia.nombre,
            "sexo": consula.historia.sexo,
            "telefono": consula.historia.telefono,
            "motivo_consulta": consula.motivo_consulta,
            # "grupo_factor": historia.grupo_factor,
            # "estado_civil": historia.estado_civil,
            # "ocupacion": historia.ocupacion,
            # "operaciones": [p.to_dic for p in historia.operaciones.all()],
            # "consultas": [p.to_dic for p in historia.conusltas.all()],
            "date_of_creation": consula.date_of_creation.strftime('%d/%m/%Y %H:%M:%S'),
        }
        data.append(historia_response)
        idx += 1
    return JsonResponse({"data": data, 'recordsFiltered': totalFilter, 'recordsTotal': consultas__.count(),
                         'draw': request.GET.get('draw')})


@login_required()
def edit_historia(request, id_):
    historia = get_object_or_404(HistoriaModel, pk=id_)
    listaOperaciones = OperacionesModel.objects.filter(historia=id_).order_by('anyo').all()
    if request.method == 'POST':
        form = HistoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('render-historias'))
    else:
        formHistoria = HistoriaForm(initial={
            "nombre": historia.nombre,
            "sexo": historia.sexo,
            "telefono": historia.telefono,
            "ocupacion": historia.ocupacion,
            "fecha_nacimiento": historia.fecha_nacimiento,
            "estado_civil": historia.estado_civil,
            "antecedentes_familiares": historia.antecedentes_familiares,
            "antecedentes_perosnales": historia.antecedentes_perosnales,
            "fumar": historia.fumar,
            "alcohol": historia.alcohol,
            "drogas": historia.drogas,
            "transfuciones": historia.transfuciones,
            "grupo_factor": historia.grupo_factor,
        })
    return render(request, "historias_edit.html", {"formHistoria": formHistoria, "historia": historia}, )


@login_required()
def get_operacionesByhistoria(request, id_):
    historia = get_object_or_404(HistoriaModel, pk=id_)
    return JsonResponse({"lista": [p.to_dic for p in historia.operaciones.all()], })


@login_required()
def ajax_edit_historia(request, id_):
    historia = get_object_or_404(HistoriaModel, pk=id_)
    data = json.loads(request.body.decode('utf-8'))
    historia.nombre = data['historia']['nombre']
    historia.sexo = data['historia']['sexo']
    historia.ocupacion = data['historia']['ocupacion']
    historia.telefono = data['historia']['telefono']
    historia.fecha_nacimiento = data['historia']['fecha_nacimiento']
    historia.estado_civil = data['historia']['estado_civil']
    historia.antecedentes_familiares = data['historia']['antecedentes_familiares']
    historia.antecedentes_perosnales = data['historia']['antecedentes_perosnales']
    historia.fumar = data['historia']['fumar']
    historia.alcohol = data['historia']['alcohol']
    historia.drogas = data['historia']['drogas']
    historia.transfuciones = data['historia']['transfuciones']
    historia.grupo_factor = data['historia']['grupo_factor']
    historia.save()
    for operacion in historia.operaciones.all():
        operacion.delete()

    for operacion in data['listaOperaciones']:
        new_operacion = OperacionesModel()
        new_operacion.historia = historia
        new_operacion.tipo = operacion['tipo']
        new_operacion.anyo = operacion['anyo']
        new_operacion.save()
    historia.save()
    return JsonResponse({"data": historia.id}, status=200)


@login_required()
def delete_complementario_ajax(request, id_):
    complementario = get_object_or_404(ComplementariosModel, pk=id_)
    complementario.delete()
    return JsonResponse({"data": "ok"}, status=200)


@login_required()
def print_receipt(request, id_):
    historia = get_object_or_404(HistoriaModel, pk=id_)
    ctx = {
        "historia": historia,
        "listaOperaciones": historia.operaciones.all(),
        "fecha_historia": historia.date_of_creation.strftime('%d/%m/%Y %H:%M'),
    }
    return render(request, "historia_print.html", {"ctx": ctx, "historia": historia}, )


@login_required()
def print_consulta(request, id_):
    consulta = get_object_or_404(ConsultaModel, pk=id_)
    # historia = get_object_or_404(HistoriaModel, consulta.historia_id)
    edada = relativedelta(datetime.now(), consulta.historia.fecha_nacimiento)
    ctx = {
        "edad": edada.years,
        "historia": consulta.historia,
        "listaOperaciones": consulta.historia.operaciones.all(),
        "fecha_historia": consulta.historia.date_of_creation.strftime('%d/%m/%Y %H:%M'),
    }
    return render(request, "consulta_print.html", {"ctx": ctx, "consulta": consulta}, )

#
# @login_required()
# def upload_complementario(request, id_):
#     complementarios = ComplementariosModel.objects.filter(consulta=id_).order_by('id').all()
#
#     if request.method == 'POST' and request.FILES:
#         myfile = request.FILES['files_complementarios']
#         datos = request.POST
#         fs = FileSystemStorage()
#         numero = randrange(10000000000, 99999999999)
#         name = f"{numero}{myfile.name}"
#         filename = fs.save(name, myfile)
#         uploated_file_url = fs.url(filename)
#         complementatio = ComplementariosModel()
#         complementatio.nombre = datos["nombre"]
#         complementatio.nota = datos["nota"]
#         complementatio.consulta_id = id_
#         complementatio.complementario = filename
#         complementatio.save()
#         formComplementario = ComplementarioForm()
#         return redirect("historias")
#     else:
#         formComplementario = ComplementarioForm
#         return render(request, "upload_complementario.html", {
#             'formComplementario': formComplementario, 'complementarios': complementarios
#         })

@login_required()
def upload_complementario(request, id_):
    complementarios = ComplementariosModel.objects.filter(consulta=id_).order_by('id').all()
    s3config = {
        "region_name": settings.OBJECT_STORAGE_REGION,
        "endpoint_url": "https://cmc.nyc3.digitaloceanspaces.com".format(settings.OBJECT_STORAGE_REGION),
        "aws_access_key_id": settings.AWS_ACCESS_KEY_ID,
        "aws_secret_access_key": settings.AWS_SECRET_ACCESS_KEY}
    # Genera la URL del archivo en S3
    s3_url = f"https://{settings.OBJECT_STORAGE_REGION}.digitaloceanspaces.com/complementarios/"

    if request.method == 'POST' and request.FILES:
        myfile = request.FILES['files_complementarios']
        datos = request.POST
        numero = randrange(10000000000, 99999999999)
        name = f"{numero}{myfile.name}"
        key = str(name)
        s3resource = boto3.resource("s3", **s3config)
        bucket = s3resource.Bucket("complementarios")
        bucket.upload_fileobj(myfile, key, ExtraArgs={'ACL': 'public-read'})

        file_name = myfile.name
        # uploated_file_url = fs.url(filename)
        complementatio = ComplementariosModel()
        complementatio.nombre = datos["nombre"]
        complementatio.nota = datos["nota"]
        complementatio.consulta_id = id_
        complementatio.complementario = name
        complementatio.save()
        formComplementario = ComplementarioForm()
        return redirect("historias")
    else:
        formComplementario = ComplementarioForm
        return render(request, "upload_complementario.html", {
            'formComplementario': formComplementario, 'complementarios': complementarios, 's3_url': s3_url
        })


