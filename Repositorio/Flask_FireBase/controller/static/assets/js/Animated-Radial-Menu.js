let toggle = document.querySelector('.toggle')
let menu = document.querySelector('.menu')

toggle.onclick = ()=>{
    menu.classList.toggle('active')
}

function cambiarImagen(nuevaImagen) {
    document.getElementById('imagenCambiante').src = nuevaImagen;

    var radioButtons = document.getElementsByName('tipo');
    var radioSeleccionado;

    for (var i = 0; i < radioButtons.length; i++) {
        if (radioButtons[i].checked) {
            radioSeleccionado = radioButtons[i];
            break;
        }
    }

    var tipoCapitalizado = radioSeleccionado.value.charAt(0).toUpperCase() + radioSeleccionado.value.slice(1);

    // Actualiza el texto del label con el value del radio button seleccionado
    var labelTipo = document.querySelector('label[for="nivel"]');
    labelTipo.textContent = "Tipo: " + tipoCapitalizado;
  }

  function validarYEnviar() {
    if (validarFormulario()) {
        document.getElementById('env').disabled = true; // Deshabilita el botón para evitar clics adicionales
        document.getElementById('dynamicForm').submit(); // Envía el formulario programáticamente
    }
}

function validarFormulario() {
    var nombre = document.getElementById('nombre').value;
    var descripcion = document.getElementById('descripcion').value;
    var nivel = document.getElementById('nivel').value;
    var experiencia = document.getElementById('experiencia').value;
    var fuerza = document.getElementById('fuerza').value;
    var magia = document.getElementById('magias').value;
    var maxpg = document.getElementById('maxpg').value;
    var maxpm = document.getElementById('maxpm').value;
    var coste = document.getElementById('coste').value;
    var radioButtons = document.getElementsByName('tipo');
    var radio="";
        // Itera a través de los radio buttons
    for (var i = 0; i < radioButtons.length; i++) {
        // Comprueba si el radio button actual está marcado
        if (radioButtons[i].checked) {
            // Al menos uno está marcado, puedes continuar o realizar acciones necesarias
            radio="hay_uno";
        }
    }

    // Puedes agregar más campos según sea necesario

    if (
        nombre === "" ||
        descripcion === "" ||
        nivel === "" ||
        experiencia === "" ||
        fuerza === "" ||
        magia === "" ||
        maxpg === "" ||
        maxpm === "" ||
        coste === "" || radio===""
    ) {
        alert("Por favor, completa todos los campos antes de enviar el formulario.");
        return false; // Evita que se envíe el formulario
    }

    return true; // Permite que se envíe el formulario
}