let ListaOperaciones = [];

$(document).ready(function () {
    var id_historia = $("#id_historia").val();
    fetch("/historias/get-operacionesByhistoria/" + id_historia, {
        method: 'GET',
        cache: 'default',
        mode: 'same-origin',
    }).then(response => {
        if (!response.ok) {
            throw Error("Error en respuesta AJAX");
        }
        return response.json()
    }).then(json => {
        ListaOperaciones = json.lista
        $.each(ListaOperaciones, function (i, operacion) {
            operacion['id'] = i;
            var item = `<div class="panel panel-dark" id="item-${operacion['id']}">
                    <div class="panel-heading">
                        <div class="panel-control">
                            <button class="btn btn-danger" type="button" onclick="removeItem(${operacion['id']})"><i
                                    class="icon demo-pli-trash"></i></button>
                        </div>
                        <h3 class="panel-title">${operacion['anyo']}</h3>
                    </div>
                    <div class="panel-body">
                        <p>${operacion['tipo']}</p>
                    </div>
                </div>`;
            $("#div_operaciones").append(item);
            $("#id_operacion").val("");
            $("#id_anyo_operacion").val("");
        });

    }).catch(e => {
        console.log(e);
    })
});

$('#add_historia').on('click', function () {
    let valid = true;
    var formHistoria = $('#formHistoria');
    formHistoria.parsley().validate();
    if (formHistoria.parsley().isValid()) {
        var formHitoriaClin = $("#formHistoria").serializeArray();
        var historia = new Object();
        $.each(formHitoriaClin, function (i, field) {
            historia[field.name] = field.value;
        });
        historia['fumar'] = $('#id_fumar').prop('checked');
        historia['alcohol'] = $('#id_alcohol').prop('checked');
        historia['drogas'] = $('#id_drogas').prop('checked');
        historia['transfuciones'] = $('#id_transfuciones').prop('checked');

        var ConsultaGeneral = {
            'historia': historia,
            'listaOperaciones': ListaOperaciones,
        };
        var id_historia = $("#id_historia").val();
        fetch("/historias/ajax-edit-historia/" + id_historia, {
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
            swal('Exito', 'Se ha modificado la Historia Clinica con Exito', 'success');
            setTimeout("location.href='/historias/historias/'", 1500);
            valid = true;
        }).catch(e => {
            console.log(e);
        })
    }
    return valid;
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
            tipo: $("#id_operacion").val(),
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
