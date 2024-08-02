 // JavaScript para mostrar o loader ao carregar a página e ao navegar para outra URL
 document.addEventListener('DOMContentLoaded', function () {
  var loader = document.getElementById('loader');
  
  // Mostrar o loader ao carregar a página
  loader.style.display = 'flex';
  
  // Ocultar o loader após o carregamento da página
  window.addEventListener('load', function () {
      loader.style.display = 'none';
  });
  
  // Mostrar o loader ao navegar para outra URL
  document.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function (event) {
          // Não mostrar o loader para links de ancoragem na mesma página
          if (link.getAttribute('href').charAt(0) === '#') {
              return;
          }

          // Mostrar o loader e permitir que o link continue com a navegação
          loader.style.display = 'flex';
      });
  });
});