document.addEventListener("DOMContentLoaded", function () {
    var editForms = document.querySelectorAll("[id^='editForm']");

    editForms.forEach(function (form) {
        form.addEventListener("submit", function (event) {
            event.preventDefault();
            // Puedes agregar aquí cualquier lógica adicional antes de enviar el formulario

            // Envía el formulario
            form.submit();
        });
    });
});
