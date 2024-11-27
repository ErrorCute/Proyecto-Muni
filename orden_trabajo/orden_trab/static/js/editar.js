document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("editarEmpleadoForm");

    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Evita el envío del formulario por defecto

        const formData = new FormData(form);
        const empleadoId = form.dataset.empleadoId; // Obtener el ID del empleado desde el atributo data

        fetch(`/orden_trab/editar/${empleadoId}/`, {
            method: "POST",
            body: formData,
            headers: {
                "X-Requested-With": "XMLHttpRequest", // Indica que es una solicitud AJAX
                "X-CSRFToken": formData.get("csrfmiddlewaretoken"), // Obtener el token CSRF
            },
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert("Empleado actualizado correctamente");
                    window.location.href = "/orden_trab/empleados/"; // Redirige a la lista de empleados
                } else {
                    alert("Error al actualizar el empleado");
                    console.log(data.errors);
                }
            })
            .catch(error => {
                console.error("Error en la solicitud:", error);
            });
    });
});
