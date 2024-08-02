let cards = document.getElementsByClassName('cardExercicio');
let button = document.getElementsByClassName('btn-seta');
cards[0].style.backgroundColor = 'rgba(0, 0, 0, 0.7)';

for (let i = 0; i < button.length; i++) {
  button[i].addEventListener('click', function () {

    cards[i].style.backgroundColor = 'rgba(0, 0, 0, 0.7)';
    for (let j = 0; j < cards.length; j++) {

      if (j == i) {
        continue
      }
      cards[j].style.backgroundColor = 'transparent';
    }
  });
}
