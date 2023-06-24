from django import forms


class HistoriaForm(forms.Form):
    gen = [
        ("M", "Masculino"),
        ("F", "Femenino")
    ]
    e_civil = [
        ("Soltero", "Soltero"),
        ("Casado", "Casado"),
        ("Divorciado", "Divorciado"),
        ("Viudo", "Viudo"),
    ]
    nombre = forms.CharField(label="Nombre", max_length=300,
                             widget=forms.TextInput(attrs={'class': 'form-control historia'}))
    sexo = forms.ChoiceField(label="Sexo", choices=gen, widget=forms.Select(
        attrs={'class': 'form-control demo_select2 historia '}))
    ocupacion = forms.CharField(label="Ocupación", max_length=300,
                                widget=forms.TextInput(attrs={'class': 'form-control historia'}))
    telefono = forms.CharField(label="Teléfono", max_length=300,
                                widget=forms.TextInput(attrs={'class': 'form-control historia'}))
    fecha_nacimiento = forms.DateField(label="Fecha de Nacimiento",
                                    widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control historia'}))
    # fecha_nacimiento = forms.CharField(label="Fecha de Naciemiento", max_length=300,
    #                                    widget=forms.TextInput(attrs={'class': 'form-control historia'}))
    estado_civil = forms.ChoiceField(label="Estado Civil", choices=e_civil, widget=forms.Select(
        attrs={'class': 'form-control select2 historia '}))
    antecedentes_familiares = forms.CharField(label="Antecedentes Familiares", required=False, max_length=300,
                                              widget=forms.Textarea(
                                                  attrs={'class': 'form-control', 'rows': '6',
                                                         'style': "height:100%;"}))
    antecedentes_perosnales = forms.CharField(label="Antecedentes Personales", required=False, max_length=300,
                                              widget=forms.Textarea(
                                                  attrs={'class': 'form-control', 'rows': '6',
                                                         'style': "height:100%;"}))
    fumar = forms.BooleanField(label="Fuma", required=False, widget=forms.CheckboxInput(
        attrs={'class': 'magic-checkbox historia'}))
    alcohol = forms.BooleanField(label="Alcohol", required=False, widget=forms.CheckboxInput(
        attrs={'class': 'magic-checkbox historia'}))
    drogas = forms.BooleanField(label="Drogas", required=False, widget=forms.CheckboxInput(
        attrs={'class': 'magic-checkbox historia'}))
    transfuciones = forms.BooleanField(label="Transfuciones", required=False, widget=forms.CheckboxInput(
        attrs={'class': 'magic-checkbox historia'}))
    grupo_factor = forms.CharField(label="Grupo factor", max_length=50,
                                   widget=forms.TextInput(attrs={'class': 'form-control historia'}))

class ConsultaForm(forms.Form):
    habito_const = [
        ("", "Selecionar"),
        ("Brevilineo", "Brevilineo"),
        ("Longilineo", "Longilineo"),
        ("Normolineo", "Normolineo")
    ]
    tejido_celular_sub = [
        ("", "Selecionar"),
        ("Infiltrado", "Infiltrado"),
        ("No Infiltrado", "No Infiltrado"),
    ]
    murmullo_ves = [
        ("", "Selecionar"),
        ("Rudo", "Rudo"),
        ("Concervado", "Concervado"),
        ("Disminuido", "Disminuido"),
        ("Abolido", "Abolido"),
    ]
    ruidos_card = [
        ("", "Selecionar"),
        ("Ritmico, Buen Tono", "Ritmico, Buen Tono"),
        ("Ritmico, Bajo Tono", "Ritmico, Bajo Tono"),
        ("Arritmico, Buen Tono", "Arritmico, Buen Tono"),
        ("Arritmico, Bajo Tono", "Arritmico, Bajo Tono"),
    ]
    motivo_consulta = forms.CharField(label="Motivo de Consulta", max_length=300,
                                      widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    historia_enfermedad_actual = forms.CharField(label="Historia de la Enfermedad Actual", required=False,
                                                 max_length=300,
                                                 widget=forms.Textarea(
                                                     attrs={'class': 'form-control', 'rows': '6',
                                                            'style': "height:100%;"}))
    inpresion_general = forms.CharField(label="Inpresion General", required=False, max_length=300,
                                        widget=forms.Textarea(
                                            attrs={'class': 'form-control', 'rows': '4',
                                                   'style': "height:100%;"}))
    fc = forms.CharField(label="FC", max_length=300, widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    ta = forms.CharField(label="TA", max_length=300, widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    fr = forms.CharField(label="FR", max_length=300, widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    pulso = forms.CharField(label="Pulso", max_length=300,
                            widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    tAuxiliar = forms.CharField(label="T°Auxiliar", max_length=300,
                                widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    tReactal = forms.CharField(label="T°Reactal", max_length=300,
                               widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    peso_habitual = forms.CharField(label="Peso Habitual", max_length=300,
                                    widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    peso_actual = forms.CharField(label="Peso Actual", max_length=300,
                                  widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    talla = forms.CharField(label="Talla", max_length=300,
                            widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    imc = forms.CharField(label="IMC", max_length=300, widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    habito_constitucional = forms.ChoiceField(label="Hábito Constitucional", choices=habito_const, widget=forms.Select(
        attrs={'class': 'form-control demo_select2 consulta '}))
    marcha = forms.CharField(label="Marcha", max_length=300,
                             widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    lesiones = forms.CharField(label="Lesiones", max_length=300,
                               widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    tejido_celular_subcutaneo = forms.CharField(label="Tejido Celular Subcutaneo", max_length=300,
                                                widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    craneo_cara = forms.CharField(label="Craneo y Cara", max_length=300,
                                  widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    cuero_cabelludo = forms.CharField(label="Cuero Cabelludo", max_length=300,
                                      widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    cuello_inspecion = forms.CharField(label="Inspección", max_length=300,
                                       widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    cuello_palpitacion = forms.CharField(label="Palpitación", max_length=300,
                                         widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    cuello_percucion = forms.CharField(label="Percución", max_length=300,
                                       widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    cuello_auscultacion = forms.CharField(label="Auscultación", max_length=300,
                                          widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    torax_piel = forms.CharField(label="Piel", max_length=300,
                                 widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    torax_forma = forms.CharField(label="Forma", max_length=300,
                                  widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    mama_forma = forms.CharField(label="Forma", max_length=300,
                                 widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    mama_tamanyo = forms.CharField(label="Tamaño", max_length=300,
                                   widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    mama_simetria = forms.CharField(label="Simetría", max_length=300,
                                    widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    mama_areolas = forms.CharField(label="Áreolas", max_length=300,
                                   widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    mama_pezones = forms.CharField(label="Pezones", max_length=300,
                                   widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    murmullo_vesicular = forms.ChoiceField(label="Murmullo Vesicular", choices=murmullo_ves, widget=forms.Select(
        attrs={'class': 'form-control demo_select2 consulta '}))
    tiraje = forms.CharField(label="Tiraje", max_length=300,
                             widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    ruidos_cardiovascular = forms.ChoiceField(label="Ruidos Cardiacos", choices=ruidos_card, widget=forms.Select(
        attrs={'class': 'form-control demo_select2 consulta '}))
    soplos = forms.CharField(label="Soplos", max_length=300,
                             widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    # Abdomen
    abdomen_inspecion = forms.CharField(label="Inspección", max_length=300,
                                        widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    abdomen_palpacion = forms.CharField(label="Palpación", max_length=300,
                                        widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    abdomen_percucion = forms.CharField(label="Percusión", max_length=300,
                                        widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    abdomen_auscultacion = forms.CharField(label="Auscultación", max_length=300,
                                           widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    obstetrico_au = forms.CharField(label="AU", max_length=300,
                                    widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    obstetrico_maniobre_leopold = forms.CharField(label="Maniobre de Leopold", max_length=300,
                                                  widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    # genitourinario
    genitourinario_percucion_lumbar = forms.CharField(label="Lumbar", max_length=300,
                                                      widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    genitourinario_percucion_derecha = forms.CharField(label="Derecha", max_length=300,
                                                       widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    genitourinario_percucion_izquierda = forms.CharField(label="Izquierda", max_length=300, widget=forms.TextInput(
        attrs={'class': 'form-control consulta'}))
    genitourinario_tacto_vaginal = forms.CharField(label="Tacto Vaginal", max_length=300,
                                                   widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    genitourinario_vulva = forms.CharField(label="Vulva", max_length=300,
                                           widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    genitourinario_flujo = forms.CharField(label="Flujo", max_length=300,
                                           widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    genitourinario_cuello_uterino = forms.CharField(label="Cuello Uterino", max_length=300,
                                                    widget=forms.TextInput(attrs={'class': 'form-control consulta'}))

    # Sistema Nervioso
    nervioso_estado = forms.CharField(label="Estado de Conciencia", max_length=300,
                                      widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    nervioso_glasgow_ocular = forms.CharField(label="Ocular", max_length=300,
                                              widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    nervioso_glasgow_motor = forms.CharField(label="Motor", max_length=300,
                                             widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    nervioso_glasgow_verbal = forms.CharField(label="Verbal", max_length=300,
                                              widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    nervioso_conducta = forms.CharField(label="Conducta", max_length=300,
                                        widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    nervioso_lenguaje = forms.CharField(label="Lenguaje", max_length=300,
                                        widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    nervioso_paredes_craneales = forms.CharField(label="Paredes Craneales", max_length=300,
                                                 widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    nervioso_reflejos_fotomotor = forms.CharField(label="Fotomotor", max_length=300,
                                                  widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    nervioso_reflejos_acomodacion = forms.CharField(label="Acomodación", max_length=300,
                                                    widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    nervioso_reflejos_osteotendinosos = forms.CharField(label="Reflejos Osteotendinosos", max_length=300,
                                                        widget=forms.TextInput(
                                                            attrs={'class': 'form-control consulta'}))
    nervioso_motricidad = forms.CharField(label="Motricidad", max_length=300,
                                          widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    nervioso_babinski = forms.CharField(label="Babinski", max_length=300,
                                        widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    nervioso_sensibilidad = forms.CharField(label="Sensibilidad", max_length=300,
                                            widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    nervioso_temblor = forms.CharField(label="Temblor", max_length=300,
                                       widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    nervioso_romberg = forms.CharField(label="Romberg", max_length=300,
                                       widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    nervioso_taxia = forms.CharField(label="Taxia", max_length=300,
                                     widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    nervioso_dismetria = forms.CharField(label="Dismetría", max_length=300,
                                         widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    nervioso_rigidez = forms.CharField(label="Rigidez de nuca", max_length=300,
                                       widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    nervioso_fondo_ojo = forms.CharField(label="Fondo de ojo", max_length=300,
                                         widget=forms.TextInput(attrs={'class': 'form-control consulta'}))

    # osteomioarticular
    osteomioarticular_columna_vertebral = forms.CharField(label="Columna Vertebral", max_length=300,
                                                          widget=forms.TextInput(
                                                              attrs={'class': 'form-control consulta'}))
    osteomioarticular_ejes_oseos = forms.CharField(label="Ejes Óseos", max_length=300,
                                                   widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    osteomioarticular_articulaciones = forms.CharField(label="Articulaciones", max_length=300,
                                                       widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    osteomioarticular_miembros = forms.CharField(label="Miembros", max_length=300,
                                                 widget=forms.TextInput(attrs={'class': 'form-control consulta'}))
    osteomioarticular_trofismo_muscular = forms.CharField(label="Trofismo Muscular", max_length=300,
                                                          widget=forms.TextInput(
                                                              attrs={'class': 'form-control consulta'}))
    # Complementarios
    complementarios_entregados = forms.CharField(label="Complementarios Entregados", required=False,
                                                 max_length=1500,
                                                 widget=forms.Textarea(
                                                     attrs={'class': 'form-control', 'rows': '6',
                                                            'style': "height:100%;"}))
    complementarios_indicados = forms.CharField(label="Complementarios Indicados", required=False,
                                                 max_length=1500,
                                                 widget=forms.Textarea(
                                                     attrs={'class': 'form-control', 'rows': '6',
                                                            'style': "height:100%;"}))
    # Diagnostico
    diagnostico_presuntivo = forms.CharField(label="Diagnostico Presuntivo", required=True,
                                                 max_length=1500,
                                                 widget=forms.Textarea(
                                                     attrs={'class': 'form-control', 'rows': '6',
                                                            'style': "height:100%;"}))
    plan_terapeutico = forms.CharField(label="Plan Terapeutico", required=True,
                                                 max_length=1500,
                                                 widget=forms.Textarea(
                                                     attrs={'class': 'form-control', 'rows': '6',
                                                            'style': "height:100%;"}))

class ComplementarioForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=300,
                             widget=forms.TextInput(attrs={'class': 'form-control historia'}))
    nota = forms.CharField(label="Nota", required=False, max_length=300,
                                              widget=forms.Textarea(
                                                  attrs={'class': 'form-control', 'rows': '6',
                                                         'style': "height:100%;"}))
    files_complementarios = forms.FileField(label="Archivos Complementarios")