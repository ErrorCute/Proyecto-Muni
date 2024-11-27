// main.js

document.addEventListener('DOMContentLoaded', function () {
    // Función para resaltar el enlace del menú de navegación activo
    function resaltarEnlaceActivo() {
        const enlaces = document.querySelectorAll('nav ul li a');
        const currentPath = window.location.pathname;

        enlaces.forEach(enlace => {
            if (enlace.getAttribute('href') === currentPath) {
                enlace.classList.add('activo');
            } else {
                enlace.classList.remove('activo');
            }
        });
    }

    // Función para mostrar un mensaje de notificación
    function mostrarNotificacion(mensaje, tipo = 'info') {
        const notificacion = document.createElement('div');
        notificacion.className = `notificacion ${tipo}`;
        notificacion.textContent = mensaje;
        document.body.appendChild(notificacion);

        // Ocultar la notificación después de 3 segundos
        setTimeout(() => {
            notificacion.remove();
        }, 3000);
    }

    // Función para manejar errores de formularios
    function manejarErrorFormulario(mensaje) {
        mostrarNotificacion(mensaje, 'error');
    }

    // Inicializar funciones comunes al cargar la página
    function inicializar() {
        resaltarEnlaceActivo();
    }

    // Llamar a la función de inicialización
    inicializar();

    // Ejemplo de uso de notificación
    // mostrarNotificacion('Bienvenido al sistema', 'success');
});
