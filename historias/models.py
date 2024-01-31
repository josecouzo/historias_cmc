from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
import boto3
from django import template
# Create your models here.
from django.db.models import ImageField


class HistoriaModel(models.Model):
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
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1, choices=gen)
    telefono = models.CharField(max_length=50, null=True)
    ocupacion = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(null=False)
    estado_civil = models.CharField(max_length=50, null=False, choices=e_civil)
    alergias = models.CharField(max_length=500, null=True)
    antecedentes_familiares = models.CharField(max_length=500, null=True)
    antecedentes_perosnales = models.CharField(max_length=500, null=True)
    fumar = models.BooleanField(default=False)
    alcohol = models.BooleanField(default=False)
    drogas = models.BooleanField(default=False)
    transfuciones = models.BooleanField(default=False)
    grupo_factor = models.CharField(max_length=50)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    date_of_update = models.DateTimeField(auto_now=True)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="myphonemodel", verbose_name="Propietario")
    # admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name="phonemodel", verbose_name="Administrador")

    def __str__(self):
        return f"{self.id} | {self.nombre}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class OperacionesModel(models.Model):
    tipo = models.CharField(max_length=50)
    anyo = models.CharField(max_length=50)
    historia = models.ForeignKey(HistoriaModel, on_delete=models.CASCADE, related_name="operaciones")
    date_of_creation = models.DateTimeField(auto_now_add=True)
    date_of_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.anyo} | {self.tipo}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    @property
    def to_dic(self):
        return {
            "id": self.id,
            "tipo": self.tipo,
            "anyo": self.anyo,
            "historia": self.historia.id,
        }

class ConsultaModel(models.Model):
    habito_const = [
        ("Brevilineo", "Brevilineo"),
        ("Longilineo", "Longilineo"),
        ("Normolineo", "")
    ]
    tejido_celular_sub = [
        ("Infiltrado", "Infiltrado"),
        ("No Infiltrado", "No Infiltrado"),
    ]
    murmullo_ves = [
        ("Rudo", "Rudo"),
        ("Concervado", "Concervado"),
        ("Disminuido", "Disminuido"),
        ("Abolido", "Abolido"),
    ]
    ruidos_card = [
        ("Ritmico, Buen Tono", "Ritmico, Buen Tono"),
        ("Ritmico, Bajo Tono", "Ritmico, Bajo Tono"),
        ("Arritmico, Buen Tono", "Arritmico, Buen Tono"),
        ("Arritmico, Bajo Tono", "Arritmico, Bajo Tono"),
    ]
    motivo_consulta = models.CharField(max_length=150)
    historia_enfermedad_actual = models.CharField(max_length=1500)
    inpresion_general = models.CharField(max_length=500)
    fc = models.CharField(max_length=50, null=True)
    ta = models.CharField(max_length=50, null=True)
    fr = models.CharField(max_length=50, null=True)
    pulso = models.CharField(max_length=50, null=True)
    tAuxiliar = models.CharField(max_length=50, null=True)
    tReactal = models.CharField(max_length=50, null=True)
    peso_habitual = models.CharField(max_length=50, null=True)
    peso_actual = models.CharField(max_length=50, null=True)
    talla = models.CharField(max_length=50, null=True)
    imc = models.CharField(max_length=50, null=True)
    habito_constitucional = models.CharField(max_length=50, null=True, choices=habito_const)
    marcha = models.CharField(max_length=50, null=True)
    lesiones = models.CharField(max_length=50, null=True)
    tejido_celular_subcutaneo = models.CharField(max_length=50, null=True, choices=tejido_celular_sub)
    lugar_infiltrado = models.CharField(max_length=50, null=True)
    craneo_cara = models.CharField(max_length=50, null=True)
    cuero_cabelludo = models.CharField(max_length=50, null=True)
    cuello_inspecion = models.CharField(max_length=50, null=True)
    cuello_palpitacion = models.CharField(max_length=50, null=True)
    cuello_percucion = models.CharField(max_length=50, null=True)
    cuello_auscultacion = models.CharField(max_length=50, null=True)
    torax_piel = models.CharField(max_length=50, null=True)
    torax_forma = models.CharField(max_length=50, null=True)
    mama_forma = models.CharField(max_length=50, null=True)
    mama_tamanyo = models.CharField(max_length=50, null=True)
    mama_simetria = models.CharField(max_length=50, null=True)
    mama_areolas = models.CharField(max_length=50, null=True)
    mama_pezones = models.CharField(max_length=50, null=True)
    murmullo_vesicular = models.CharField(max_length=50, null=True, choices=murmullo_ves)
    tiraje = models.CharField(max_length=50, null=True)
    estertores = models.CharField(max_length=50, null=True)
    ruidos_cardiovascular = models.CharField(max_length=50, null=True, choices=ruidos_card)
    soplos = models.CharField(max_length=50, null=True)
    abdomen_inspecion = models.CharField(max_length=150, null=True)
    abdomen_palpacion = models.CharField(max_length=150, null=True)
    abdomen_percucion = models.CharField(max_length=150, null=True)
    abdomen_region_inginal = models.CharField(max_length=150, null=True)
    abdomen_auscultacion = models.CharField(max_length=150, null=True)
    obstetrico_maniobre_leopold = models.CharField(max_length=50, null=True)
    obstetrico_au = models.CharField(max_length=50, null=True)
    # genitourinario_percucion_lumbar = models.CharField(max_length=50, null=True)
    genitourinario_percucion_derecha = models.CharField(max_length=50, null=True)
    genitourinario_percucion_izquierda = models.CharField(max_length=50, null=True)
    genitourinario_tacto_vaginal = models.CharField(max_length=150, null=True)
    genitourinario_puntos_pielos = models.CharField(max_length=150, null=True)
    genitourinario_testiculo = models.CharField(max_length=150, null=True)
    genitourinario_glande = models.CharField(max_length=150, null=True)
    genitourinario_vulva = models.CharField(max_length=150, null=True)
    genitourinario_flujo = models.CharField(max_length=150, null=True)
    genitourinario_cuello_uterino = models.CharField(max_length=150, null=True)
    nervioso_estado = models.CharField(max_length=150, null=True)
    nervioso_glasgow_ocular = models.CharField(max_length=150, null=True)
    nervioso_glasgow_motor = models.CharField(max_length=150, null=True)
    nervioso_glasgow_verbal = models.CharField(max_length=150, null=True)
    nervioso_conducta = models.CharField(max_length=150, null=True)
    nervioso_lenguaje = models.CharField(max_length=150, null=True)
    nervioso_paredes_craneales = models.CharField(max_length=150, null=True)
    nervioso_reflejos_fotomotor = models.CharField(max_length=150, null=True)
    nervioso_reflejos_acomodacion = models.CharField(max_length=150, null=True)
    nervioso_reflejos_osteotendinosos = models.CharField(max_length=150, null=True)
    nervioso_motricidad = models.CharField(max_length=150, null=True)
    nervioso_babinski = models.CharField(max_length=150, null=True)
    nervioso_sensibilidad = models.CharField(max_length=150, null=True)
    nervioso_temblor = models.CharField(max_length=150, null=True)
    nervioso_romberg = models.CharField(max_length=150, null=True)
    nervioso_taxia = models.CharField(max_length=150, null=True)
    nervioso_dismetria = models.CharField(max_length=150, null=True)
    nervioso_rigidez = models.CharField(max_length=150, null=True)
    nervioso_fondo_ojo = models.CharField(max_length=150, null=True)
    osteomioarticular_columna_vertebral = models.CharField(max_length=150, null=True)
    osteomioarticular_ejes_oseos = models.CharField(max_length=150, null=True)
    osteomioarticular_articulaciones = models.CharField(max_length=150, null=True)
    osteomioarticular_miembros = models.CharField(max_length=150, null=True)
    osteomioarticular_trofismo_muscular = models.CharField(max_length=150, null=True)
    complementarios_entregados = models.CharField(max_length=1500, null=True)
    complementarios_indicados = models.CharField(max_length=1500, null=True)
    diagnostico_presuntivo = models.CharField(max_length=1500, null=True)
    plan_terapeutico = models.CharField(max_length=1500, null=True)
    owner = models.ForeignKey(User,  null=True,on_delete=models.CASCADE, related_name="consultas", verbose_name="propietario")
    historia = models.ForeignKey(HistoriaModel, on_delete=models.CASCADE, related_name="conusltas")
    date_of_creation = models.DateTimeField(auto_now_add=True)
    date_of_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.date_of_creation} | {self.motivo_consulta}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


    @property
    def to_dic(self):
        return {
            "id": self.id,
            "fecha": self.date_of_creation.strftime('%d/%m/%Y %H:%M:%S'),
            "motivo_consulta": self.motivo_consulta,
            "diagnostico_presuntivo": self.diagnostico_presuntivo,
            "complementarios_indicados": self.complementarios_indicados,
            "plan_terapeutico": self.plan_terapeutico,
            "owner": f"{self.owner.first_name} {self.owner.last_name}" if self.owner else "-"
        }

class ComplementariosModel(models.Model):
    nombre = models.CharField(max_length=50)
    nota = models.CharField(max_length=50)
    complementario = models.FileField(upload_to='complementarios/')
    consulta = models.ForeignKey(ConsultaModel, on_delete=models.CASCADE, related_name="complementarios")
    date_of_creation = models.DateTimeField(auto_now_add=True)
    date_of_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class ProcederesModel(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    date_of_creation = models.DateTimeField(auto_now_add=True)
    date_of_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} | {self.precio}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    @property
    def to_dic(self):
        return {
            "id": self.id,
            "proceder": self.nombre,
            "precio": self.precio,
        }


class ProcederesRealizadosModel(models.Model):
    proceder = models.ForeignKey(ProcederesModel, on_delete=models.CASCADE, related_name="proceder")
    consulta = models.ForeignKey(ConsultaModel, on_delete=models.CASCADE, related_name="consulta")
    cantidad = models.IntegerField()
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="procederes",
                              verbose_name="propietario")
    date_of_creation = models.DateTimeField(auto_now_add=True)
    date_of_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.proceder.nombre} | {self.cantidad}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    @property
    def to_dic(self):
        return {
            "id": self.id,
            "proceder": self.proceder.nombre,
            "consulta": self.consulta.id,
            "cantidad": self.cantidad
        }








