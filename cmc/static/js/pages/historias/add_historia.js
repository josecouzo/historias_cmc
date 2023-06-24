let ListaOperaciones = [];
$('#demo-dp-txtinput input').datepicker();


function insertar() {
    let valid = true;
    var formHistoria = $('#formHistoria');
    formHistoria.parsley().validate();
    var formInterrogatorio = $('#formInterrogatorio');
    formInterrogatorio.parsley().validate();
    var FormDiagnostico = $('#FormDiagnostico');
    FormDiagnostico.parsley().validate();

    if (!formHistoria.parsley().isValid()) {
        $("#error_historia_label").remove();
        $("#error_historia").append("<span class=\"badge badge-danger\" id='error_historia_label'><i class='fa fa-exclamation-triangle '></i></span>")
        valid = false;
    } else {
        $("#error_historia_label").remove();
    }
    if (!formInterrogatorio.parsley().isValid()) {
        $("#error_interrogatorio_label").remove();
        $("#error_interrogatorio").append("<span class=\"badge badge-danger\" id='error_interrogatorio_label'><i class='fa fa-exclamation-triangle '></i></span>")
        valid = false;
    } else {
        $("#error_interrogatorio_label").remove();
    }
    if (!FormDiagnostico.parsley().isValid()) {
        $("#error_diagnostico_label").remove();
        $("#error_diagnostico").append("<span class=\"badge badge-danger\" id='error_diagnostico_label'><i class='fa fa-exclamation-triangle '></i></span>")
        valid = false;
    } else {
        $("#error_diagnostico_label").remove();
    }
    if (valid) {
        var formHitoriaClin = $("#formHistoria").serializeArray();
        var historia = new Object();
        $.each(formHitoriaClin, function (i, field) {
            historia[field.name] = field.value;
        });
        historia['fumar'] = $('#id_fumar').prop('checked');
        historia['alcohol'] = $('#id_alcohol').prop('checked');
        historia['drogas'] = $('#id_drogas').prop('checked');
        historia['transfuciones'] = $('#id_transfuciones').prop('checked');

        var consulta = new Object();
        var formInterrogatorioS = $("#formInterrogatorio").serializeArray();
        var interrogatorio = new Object();
        $.each(formInterrogatorioS, function (i, field) {
            consulta[field.name] = field.value;
        });

        var formEFGeneraS = $("#formEFGeneral").serializeArray();
        var EFGeneraS = new Object();
        $.each(formEFGeneraS, function (i, field) {
            consulta[field.name] = field.value;
        });

        var formRegionalS = $("#formRegional").serializeArray();
        var Regional = new Object();
        $.each(formRegionalS, function (i, field) {
            consulta[field.name] = field.value;
        });

        var FormRespiratorioS = $("#FormRespiratorio").serializeArray();
        var Respiratorio = new Object();
        $.each(FormRespiratorioS, function (i, field) {
            consulta[field.name] = field.value;
        });

        var FormCardiovascular = $("#FormCardiovascular").serializeArray();
        var Cardiovascular = new Object();
        $.each(FormCardiovascular, function (i, field) {
            consulta[field.name] = field.value;
        });

        var FormAbdomen = $("#FormAbdomen").serializeArray();
        var Abdomen = new Object();
        $.each(FormAbdomen, function (i, field) {
            consulta[field.name] = field.value;
        });

        var FormGenitourinario = $("#FormGenitourinario").serializeArray();
        var Genitourinario = new Object();
        $.each(FormGenitourinario, function (i, field) {
            consulta[field.name] = field.value;
        });

        var FormSistemaNervioso = $("#FormSistemaNervioso").serializeArray();
        var SistemaNervioso = new Object();
        $.each(FormSistemaNervioso, function (i, field) {
            consulta[field.name] = field.value;
        });

        var FormComplementariosS = $("#FormComplementarios").serializeArray();
        var Complementarios = new Object();
        $.each(FormComplementariosS, function (i, field) {
            consulta[field.name] = field.value;
        });

        var FormOsteomioarticular = $("#FormOsteomioarticular").serializeArray();
        var Osteomioarticular = new Object();
        $.each(FormOsteomioarticular, function (i, field) {
            consulta[field.name] = field.value;
        });

        var FormDiagnostico = $("#FormDiagnostico").serializeArray();
        var Osteomioarticular = new Object();
        $.each(FormDiagnostico, function (i, field) {
            consulta[field.name] = field.value;
        });
        var ConsultaGeneral = {
            'historia': historia,
            'listaOperaciones': ListaOperaciones,
            'consulta': consulta,
        };
        fetch("/historias/add-historia-ajax/", {
            method: 'POST',
            cache: 'default',
            mode: 'same-origin',
            headers: head,
            body: JSON.stringify(ConsultaGeneral),
        }).then(response => {
            if (!response.ok) {
                swal('Error de Servidor', 'Error en respuesta AJAX', 'error');
                throw Error("Error en respuesta AJAX");
            }
            return response.json()
        }).then(json => {
             swal('Exito', 'Se ha insertado la Historia Clinica con Exito', 'success');
            setTimeout("location.href='/historias/historias/'", 1500);
            valid = true;
        }).catch(e => {
            console.log(e);
        })
    }
    return valid;
}

$('#add_historia').on('click', function () {
    insertar();
});
$('#add_operacion').on('click', function () {
    let valid = true;
    if ($("#id_operacion").val() == "") {
        $("#inp_operacion").addClass('has-error');
        valid = false;
    }
    if ($("#id_anyo_operacion").val() == "") {
        $("#inp_anyo").addClass('has-error');
        valid = false;
    }
    if (valid) {
        let operacion = {
            operacion: $("#id_operacion").val(),
            anyo: $("#id_anyo_operacion").val(),
        }
        ListaOperaciones.push(operacion);
        operacion['id'] = ListaOperaciones.length;
        var item = `<div class="panel panel-dark" id="item-${ListaOperaciones.length}">
                    <div class="panel-heading">
                        <div class="panel-control">
                            <button class="btn btn-danger" type="button" onclick="removeItem(${ListaOperaciones.length})"><i
                                    class="icon demo-pli-trash"></i></button>
                        </div>
                        <h3 class="panel-title">${$("#id_anyo_operacion").val()}</h3>
                    </div>
                    <div class="panel-body">
                        <p>${$("#id_operacion").val()}</p>
                    </div>
                </div>`;
        $("#div_operaciones").append(item);
        $("#id_operacion").val("");
        $("#id_anyo_operacion").val("");
    }
});

function removeItem(i) {
    ListaOperaciones = ListaOperaciones.filter(function (obj) {
        if (obj['id'] === i) {
            return obj['id'] !== i;
        } else {
            return true;
        }
    });
    $('#item-' + i).remove();
}
