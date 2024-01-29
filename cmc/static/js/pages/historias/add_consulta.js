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

        var FormObstetrico = $("#FormObstetrico").serializeArray();
        var Obstetrico = new Object();
        $.each(FormObstetrico, function (i, field) {
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
            'ListaProcederes': ListaProcederes,
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

$('#add_proceder').on('click', function () {
    let valid = true;
    if ($("#id_proceder").val() == "") {
        $("#inp_proceder").addClass('has-error');
        valid = false;
    }
    if ($("#id_cant_proceder").val() == "") {
        $("#inp_cant_proceder").addClass('has-error');
        valid = false;
    }
    if (valid) {
        let proceder = {
            proceder: $("#id_proceder").val(),
            cant: $("#id_cant_proceder").val(),
        }
        ListaProcederes.push(proceder);
        proceder['id'] = ListaProcederes.length;
        var item = `<div class="panel panel-dark" id="item-${ListaProcederes.length}">
                    <div class="panel-heading">
                        <div class="panel-control">
                            <button class="btn btn-danger" type="button" onclick="removeItemProceder(${ListaProcederes.length})"><i
                                    class="icon demo-pli-trash"></i></button>
                        </div>
                        <h3 class="panel-title">${$("#id_cant_proceder").val()} -${$("#id_proceder option:selected").text()}</h3>
                    </div>
                </div>`;
        $("#div_proceder").append(item);
        $("#id_proceder").val("");
        $("#id_cant_proceder").val("");
    }
});

function removeItemProceder(i) {
    ListaProcederes = ListaProcederes.filter(function (obj) {
        if (obj['id'] === i) {
            return obj['id'] !== i;
        } else {
            return true;
        }
    });
    $('#item-' + i).remove();
}


$('#id_peso_actual').on( "keyup", function() {
    // Obtener los valores de altura y peso
    var altura = parseFloat($("#id_talla").val());
    var peso = parseFloat($("#id_peso_actual").val());
    // console.log("entro");

    // Verificar si los valores son numéricos
    if (!isNaN(altura) && !isNaN(peso)) {

        // Calcular el índice de masa corporal (IMC)
        var imc = peso / ((altura / 100) * (altura / 100));

        // Mostrar el resultado
        $("#id_imc").val(imc.toFixed(2));
    }

});

$('#id_talla').on( "keyup", function() {
    // Obtener los valores de altura y peso
    var altura = parseFloat($("#id_talla").val());
    var peso = parseFloat($("#id_peso_actual").val());
    // console.log("entro");

    // Verificar si los valores son numéricos
    if (!isNaN(altura) && !isNaN(peso)) {

        // Calcular el índice de masa corporal (IMC)
        var imc = peso / ((altura / 100) * (altura / 100));

        // Mostrar el resultado
        $("#id_imc").val(imc.toFixed(2));
    }

});
