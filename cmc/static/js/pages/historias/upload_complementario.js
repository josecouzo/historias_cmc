$(".delete_btn").click(function () {
    var id_complemnetario = $(this).attr('data-id');
    console.log(id_complemnetario);
    fetch("/historias/delete-complementario-ajax/" + id_complemnetario, {
        method: 'POST',
        cache: 'default',
        mode: 'same-origin',
        headers: head,
    }).then(response => {
        if (!response.ok) {
            swal('Error de Servidor', 'Error en respuesta AJAX', 'error');
            throw Error("Error en respuesta AJAX");
        }
        return response.json()
    }).then(json => {
        swal('Exito', 'Se ha eliminado el complementario', 'success');
        setTimeout(" window.location.reload();", 1500);
        valid = true;
    }).catch(e => {
        console.log(e);
    })
});
