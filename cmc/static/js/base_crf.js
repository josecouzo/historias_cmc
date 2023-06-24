function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

window.setTimeout(function () {
        $(".alert-dismissible").fadeTo(500, 0).slideUp(500, function () {
            $(this).remove();
        });

    },
    2000
);

// const csrftoken = getCookie('csrftoken');
const head = new Headers();
head.append("Content-Type", "application/json");
head.append("X-CSRFToken", csrftoken);

