<script>
    const audio = document.getElementById('backgroundAudio');

    function playMusic(filename) {
      audio.src = filename;
      audio.play();
    }
    muteButton.addEventListener('click', () => {
      if (audio.paused) {
        audio.play();
        isMuted = false;
        muteButton.firstElementChild.src = 'images/mute.png';
      } else {
        audio.pause();
        isMuted = true;
        muteButton.firstElementChild.src = 'images/unmute.png';
      }
    });
    const hamburgerButton = document.getElementById('hamburgerButton');
    const navButtons = document.querySelectorAll('nav svg');

    hamburgerButton.addEventListener('click', () => {
      // Cambia la visibilidad de los botones de navegación
      navButtons.forEach(button => {
        button.style.display = 'block';
      });

      const mainNav = document.getElementById('mainNav');
      mainNav.classList.toggle('open');
      hamburgerButton.classList.toggle('open');
      const isOpen = mainNav.classList.contains('open');

      anime({
        targets: 'textPath',
        startOffset: (d, i) => {
          if (isOpen) {
            return i % 2 === 0 ? '60%' : '40%';
          }
          return i % 2 === 0 ? '0%' : '100%';
        },
        duration: 2500,
        delay: isOpen ? 200 + anime.stagger(50) : anime.stagger(50),
        begin: () => {
          if (mainNav.classList.contains('open')) {
            mainNav.style.visibility = 'visible';
          }
        },
        complete: () => {
          if (!mainNav.classList.contains('open')) {
            mainNav.style.visibility = 'hidden';
          }
        },
      });
    });
  </script>