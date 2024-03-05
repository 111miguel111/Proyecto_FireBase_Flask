// Obtener el elemento de audio de fondo
const audio = document.getElementById('backgroundAudio');

// Función para reproducir música
function playMusic(filename) {
  // Establecer la fuente del audio y reproducirlo
  audio.src = filename;
  audio.play();
}

// Agregar un evento de clic al botón de silencio
muteButton.addEventListener('click', () => {
  // Verificar si el audio está en pausa (silenciado)
  if (audio.paused) {
    // Si está en pausa, reproducir audio y cambiar la imagen del botón a no silenciado
    audio.play();
    isMuted = false;
    muteButton.firstElementChild.src = 'images/mute.png';
  } else {
    // Si está reproduciendo, pausar el audio y cambiar la imagen del botón a silenciado
    audio.pause();
    isMuted = true;
    muteButton.firstElementChild.src = 'images/unmute.png';
  }
});

// Obtener el botón de hamburguesa y los botones de navegación
const hamburgerButton = document.getElementById('hamburgerButton');
const navButtons = document.querySelectorAll('nav svg');

// Agregar un evento de clic al botón de hamburguesa
hamburgerButton.addEventListener('click', () => {
  // Cambiar la visibilidad de los botones de navegación
  navButtons.forEach(button => {
    button.style.display = 'block';
  });

  // Alternar la clase 'open' en el menú de navegación y el botón de hamburguesa
  const mainNav = document.getElementById('mainNav');
  mainNav.classList.toggle('open');
  hamburgerButton.classList.toggle('open');

  // Verificar si el menú está abierto
  const isOpen = mainNav.classList.contains('open');

  // Animación para los botones de texto
  anime({
    targets: 'textPath',
    startOffset: (d, i) => {
      // Determinar el desplazamiento inicial para la animación de los botones de texto
      if (isOpen) {
        return i % 2 === 0 ? '60%' : '40%';
      }
      return i % 2 === 0 ? '0%' : '100%';
    },
    duration: 2500,
    delay: isOpen ? 200 + anime.stagger(50) : anime.stagger(50),
    begin: () => {
      // Mostrar el menú de navegación cuando comienza la animación
      if (mainNav.classList.contains('open')) {
        mainNav.style.visibility = 'visible';
      }
    },
    complete: () => {
      // Ocultar el menú de navegación cuando la animación está completa
      if (!mainNav.classList.contains('open')) {
        mainNav.style.visibility = 'hidden';
      }
    },
  });
});
