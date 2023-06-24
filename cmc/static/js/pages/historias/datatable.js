let Table;
$(document).ready(function () {
    Table = $('#Table').DataTable({
        "ajax": "/historias/historias-ajax/",
        "dom": 'lfrtip',
        "serverSide": true,
        "paging": true,
        "processing": true,
        "columns": [
            {
                "data": null,
                "className": "details-control",
                "orderable": false,
                "searchable": false,
                "defaultContent": buttonPassengers,
            },
            {"data": "id"},
            {
                "data": function (data, type, row) {
                    return formatClient(data);
                }
            },
            {"data": "sexo"},
            {"data": "telefono"},
            {"data": "edad"},
            {
                "data": function (data, type, row) {
                    return formatAcciones(data);
                }
            },
        ],
        "order": [[1, "desc"]],
        "aLengthMenu": [[10, 20, 30, 50, 100], [10, 20, 30, 50, 100]],
        pagingType: $(window).width() < 768 ? "full" : "full_numbers",
        "language": {
            "url": "//cdn.datatables.net/plug-ins/1.11.5/i18n/es-ES.json"
        }
    });

    $("#Table tbody").on('click', 'td.details-control', function () {
        let tr = (this).closest('tr');
        let row = Table.row(tr);
        let data = row.data();

        if (row.child.isShown()) {
            row.child.hide();
        } else {
            row.child(formatPassengers(data)).show();
        }
    });


});
const formatClient = (data) => {
    return `<div>${data.nombre}</div>`;
};


function formatAcciones(data) {
    return `<a href="/historias/add-consulta/${data.id}">
                <button class="btn btn-success  btn-xs btn-icon " title="Insertar Consultas"><i class="fa fa-file-pdf-o icon-lg"></i></button>
            </a>
            <a href="/historias/edit-historia/${data.id}">
                <button class="btn btn-primary btn-xs btn-icon " title="Esditar Historia"><i class="fa fa-pencil icon-lg"></i></button>
            </a>
            <a href="/historias/print_receipt/${data.id}">
                <button class="btn btn-danger btn-xs btn-icon " title="PDF"><i class="fa fa-file-pdf-o icon-lg"></i></button>
            </a>`;
}

function formatPassengers(data) {
    let html = '';
    for (let p of data.consultas) {
        html += `
            <tr>
                <td>${p.fecha}</td>
                <td>${p.owner}</td>
                <td>${p.motivo_consulta}</td>
                <td>${p.diagnostico_presuntivo}</td>
                <td>${p.complementarios_indicados}</td>
                <td>${p.plan_terapeutico}</td>
                <td>
                    <a href="/historias/print_consulta/${p.id}">
                    <button class="btn btn-danger btn-xs btn-icon " title="PDF"><i class="fa fa-file-pdf-o icon-lg"></i></button>
                    </a>
                    <a href="/historias/upload-complementario/${p.id}">
                    <button class="btn btn-info btn-xs btn-icon " title="Complementarios"><i class="fa fa-file icon-lg"></i></button>
                    </a>
                </td>
            </tr>
        `
    }
    return `
    <div class="row">
        <table class="table table-responsive-sm table-borderless border-top" id="Passengers" width="100%" cellspacing="0">
            <tbody>
                <tr>
                    <th class="font-weight-bold text-info text-center" colspan="5" style="font-size: large">Consultas</th>
                </tr>
                <tr>
                    <th>Fecha</th>
                    <th>Doctor</th>
                    <th>Motivo de la Consulta</th>
                    <th>Diagnostico Presuntivo</th>
                    <th>Complementarios Indicados</th>
                    <th>Plan Terapeutico</th>
                    <th>Aciones</th>
                </tr>
                ${html}
            </tbody>
        </table>   
    </div>
    `
}

const buttonPassengers = `
<button class="btn btn-info" data-toggle="collapse" style="background-color: transparent; border-color: transparent" 
title="Mostrar Consultas">
    <i class="fa fa-book text-info"></i>
    <span class="label label-info pull-right">1 </span>
</button>

`;


$("#activarFiltros").on('change', function () {
    let activarFiltros = document.getElementById("activarFiltros");
    if (activarFiltros.checked) {
        activarFiltros.checked = true;
        $(".filtros").show();
        $("#switchText").text("Ocultar Filtros");
    } else {
        activarFiltros.checked = false;
        $(".filtros").hide();
        $("#switchText").text("Mostrar Filtros");
    }
});


$('input.column_filter').on('keyup click  ', function () {
    filterColumn($(this).parents('div').attr('data-column'));
});

function filterColumn(i) {
    $('#Table').DataTable().column(i).search(
        $('#col' + i + '_filter').val(),
        $('#col' + i + '_smart').prop('checked')).draw();
}

