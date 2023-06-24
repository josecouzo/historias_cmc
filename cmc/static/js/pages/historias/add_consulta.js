let ListaOperaciones = [];

function insertar() {
    let valid = true;
    var formInterrogatorio = $('#formInterrogatorio');
    formInterrogatorio.parsley().validate();
    var FormDiagnostico = $('#FormDiagnostico');
    FormDiagnostico.parsley().validate();

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
            'consulta': consulta,
        };
        fetch("/historias/add-consulta-ajax/", {
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

