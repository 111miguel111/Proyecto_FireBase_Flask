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
    var ataque = document.getElementById('ataque').value;
    var ataquePor = document.getElementById('ataquePor').value;
    var magia = document.getElementById('magia').value;
    var coste = document.getElementById('coste').value;
    var materia = document.getElementById('materia').value;


    // Validar que todos los campos estén completos
    if (
        nombre === "" ||
        descripcion === "" ||
        ataque === "" ||
        ataquePor === "" ||
        magia === "" ||
        coste === "" ||
        materia === "0" || // Asumiendo que 0 es la opción por defecto en el select
        radio === ""
    ) {
        var menuSound = document.getElementById("error-sound");
        menuSound.pause();
        menuSound.currentTime = 0;
        menuSound.play();
        alert("Por favor, completa todos los campos antes de enviar el formulario.");
        return false; // Evita que se envíe el formulario
    }

    var menuSound = document.getElementById("start-sound");

    menuSound.pause();
    menuSound.currentTime = 0;
    menuSound.play();
    
    setTimeout(function() {         
    }, 1000);

    return true; // Permite que se envíe el formulario
}
