let Table;
$(document).ready(function () {
    Table = $('#Table').DataTable({
        "ajax": "/historias/hoja-cargo-ajax/",
        "dom": 'Blfrtip',
        "serverSide": true,
        "paging": true,
        "processing": true,
        buttons: [
            { extend: 'pdfHtml5', className: 'btn btn-primary btn-icon fa fa-file-pdf-o', text:" Exportar PDF" },
        ],
        "columns": [
            {"data": "count"},
            {"data": "id"},
            {"data": "nombre"},
            {"data": "sexo"},
            {"data": "telefono"},
            {"data": "motivo_consulta"},
            {"data": "date_of_creation"},
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

    var start = moment();
    var end = moment().add(1, 'days');

    function cb(start, end) {
        $("#col7_filter").val(start.format('YYYY-MM-DD') + "|" + end.format('YYYY-MM-DD'))
        $('#reportrange span').html(start.format('MMMM D, YYYY') + ' - ' + end.format('MMMM D, YYYY'));
        filterColumn(7);
    }

    $('#reportrange').daterangepicker({
        startDate: start,
        endDate: end,
        ranges: {
            'Hoy': [moment(), moment().add(1, 'days')],
            'Ayer': [moment().subtract(1, 'days'), moment()],
            'Últimos 7 Dias': [moment().subtract(6, 'days'), moment().add(1, 'days')],
            'Últimos 30 Dias': [moment().subtract(29, 'days'), moment().add(1, 'days')],
            'Este Mes': [moment().startOf('month'), moment().endOf('month')],
            'Ultimo Mes': [moment().subtract(1, 'month').startOf('month'), moment().subtract(1, 'month').endOf('month')]
        }
    }, cb);
    cb(start, end);


});

function formatAcciones(data) {
    return `<a href="/historias/print_consulta/${data.id}">
                <button class="btn btn-danger btn-xs btn-icon " title="PDF"><i class="fa fa-file-pdf-o icon-lg"></i></button>
            </a>
            <a href="/historias/upload-complementario/${data.id}">
                <button class="btn btn-info btn-xs btn-icon " title="Complementarios"><i class="fa fa-file icon-lg"></i></button>
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


$('input.column_filter').on('keyup click ', function () {
    filterColumn($(this).parents('div').attr('data-column'));
});

function filterColumn(i) {
    $('#Table').DataTable().column(i).search(
        $('#col' + i + '_filter').val(),
        $('#col' + i + '_smart').prop('checked')).draw();
}

$('.hide_column').on('click', function (e) {
    e.preventDefault();

    // Get the column API object
    var column = Table.column($(this).attr('data-column'));

    // Toggle the visibility
    column.visible(!column.visible());
});