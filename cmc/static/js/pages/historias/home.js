let Table;
$(document).ready(function () {
    Table = $('#Table').DataTable({
        "ajax": "/historias/hoja-cargo-ajax/",
        "dom": 'lfrtip',
        "serverSide": true,
        "paging": true,
        "processing": true,
        "columns": [
            {"data": "count"},
            {"data": "id"},
            {
                "data": function (data, type, row) {
                    return formatClient(data);
                }
            },
            {"data": "sexo"},
            {"data": "telefono"},
            {"data": "motivo_consulta"},
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