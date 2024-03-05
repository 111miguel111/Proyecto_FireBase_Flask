/**
 * Función que se ejecuta cuando se hace clic en el botón de toggle.
 */
let toggle = document.querySelector('.toggle');
let menu = document.querySelector('.menu');

/**
 * Alternar la clase 'active' en el menú cuando se hace clic en el botón de toggle.
 */
toggle.onclick = () => {
    menu.classList.toggle('active');
}

/**
 * Cambiar la imagen y actualizar el texto del label según el radio button seleccionado.
 * @param {string} nuevaImagen - La URL de la nueva imagen.
 */
function cambiarImagen(nuevaImagen) {
    // Cambiar la imagen con la URL proporcionada
    document.getElementById('imagenCambiante').src = nuevaImagen;

    // Obtener el radio button seleccionado
    var radioButtons = document.getElementsByName('tipo');
    var radioSeleccionado;
    for (var i = 0; i < radioButtons.length; i++) {
        if (radioButtons[i].checked) {
            radioSeleccionado = radioButtons[i];
            break;
        }
    }

    // Convertir la primera letra del tipo en mayúscula y actualizar el texto del label
    var tipoCapitalizado = radioSeleccionado.value.charAt(0).toUpperCase() + radioSeleccionado.value.slice(1);
    var labelTipo = document.querySelector('label[for="nivel"]');
    labelTipo.textContent = "Tipo: " + tipoCapitalizado;
}

/**
 * Validar y enviar el formulario.
 */
function validarYEnviar() {
    if (validarFormulario()) {
        // Deshabilitar el botón de envío y enviar el formulario
        document.getElementById('env').disabled = true;
        document.getElementById('dynamicForm').submit();
    }
}

/**
 * Validar los campos del formulario antes de enviarlo.
 * @returns {boolean} - Devuelve true si el formulario es válido, de lo contrario, devuelve false.
 */
function validarFormulario() {
    // Obtener los valores de los campos del formulario
    var nombre = document.getElementById('nombre').value;
    var descripcion = document.getElementById('descripcion').value;
    var nivel = document.getElementById('nivel').value;
    var experiencia = document.getElementById('experiencia').value;
    var fuerza = document.getElementById('fuerza').value;
    var magia = document.getElementById('magias').value;
    var maxpg = document.getElementById('maxpg').value;
    var maxpm = document.getElementById('maxpm').value;
    var coste = document.getElementById('coste').value;

    // Obtener el radio button seleccionado
    var radioButtons = document.getElementsByName('tipo');
    var radio = "";
    for (var i = 0; i < radioButtons.length; i++) {
        if (radioButtons[i].checked) {
            radio = "hay_uno";
        }
    }

    // Comprobar si algún campo está vacío
    if (
        nombre === "" ||
        descripcion === "" ||
        nivel === "" ||
        experiencia === "" ||
        fuerza === "" ||
        magia === "" ||
        maxpg === "" ||
        maxpm === "" ||
        coste === "" || radio === ""
    ) {
        // Reproducir un sonido de error y mostrar una alerta si hay campos vacíos
        var menuSound = document.getElementById("error-sound");
        menuSound.pause();
        menuSound.currentTime = 0;
        menuSound.play();
        alert("Por favor, completa todos los campos antes de enviar el formulario.");
        return false;
    }
    // Reproducir un sonido de inicio si todos los campos están completos y devolver true para enviar el formulario
    var menuSound = document.getElementById("start-sound");
    menuSound.pause();
    menuSound.currentTime = 0;
    menuSound.play();
    return true;
}
