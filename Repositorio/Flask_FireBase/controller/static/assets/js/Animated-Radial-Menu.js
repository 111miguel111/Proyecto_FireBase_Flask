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
