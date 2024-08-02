document.addEventListener("DOMContentLoaded", function() {
  console.log('Document loaded');  // Adicione isso para verificar se o DOM está carregado
  
  const teste = document.getElementById("teste");
  const selectElement = document.getElementById('opcoes');
  const button = document.getElementById('button_start');
  const cores = ["Pernada", "Raquetada", "Drible"];
  const cores1 = ["Pernada Pernada", "Pernada Raquetada", "Pernada Drible", "Drible Raquetada", "Drible Drible", "Raquetada Raquetada", "Troca de mão"];
  let isRunning = false;
  let intervalId;

  button.addEventListener('click', function() {
      console.log('Button clicked');  // Verifique se o clique está funcionando
      const selectedOption = selectElement.value;

      if (isRunning) {
          clearInterval(intervalId);
          isRunning = false;
          button.textContent = 'Começar';
      } else {
          switch (selectedOption) {
              case 'opcao1':
                  intervalId = startLevel(cores, 2000);
                  break;
              case 'opcao2':
                  intervalId = startLevel(cores1, 3000);
                  break;
              case 'opcao3':
                  console.log("level 3");
                  break;
              default:
                  console.log('Nenhuma opção selecionada');
          }
          isRunning = true;
          button.textContent = 'Parar';
      }
  });

  function geraNumero(max) {
      return Math.floor(Math.random() * max);
  }

  function mostraCor(cores) {
      const num = geraNumero(cores.length);
      teste.textContent = cores[num];
      console.log('Texto para falar: ', teste.textContent);  // Verifique o texto que está sendo gerado
      speakText(teste.textContent);
  }

  function startLevel(cores, interval) {
      mostraCor(cores);
      return setInterval(() => mostraCor(cores), interval);
  }

  function speakText(text) {
      if ('speechSynthesis' in window) {
          const synth = window.speechSynthesis;
          const utterance = new SpeechSynthesisUtterance(text);
          utterance.lang = 'pt-BR';
          synth.speak(utterance);
      } else {
          console.log('Speech synthesis not supported');  // Verifique se a síntese de fala é suportada
      }
  }
});
