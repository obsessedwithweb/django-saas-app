let cards = document.querySelectorAll(".card");
let stackArea = document.querySelector(".stack-area");

function rotateCards() {
  let angle = 0;
  cards.forEach((card, index) => {
    if (card.classList.contains("away")) {
      card.style.transform = `translateY(-120vh) rotate(-48deg)`;
    } else {
      card.style.transform = `rotate(${angle}deg)`;
      angle -= 7;
      card.style.zIndex = cards.length - index;
    }
  });
}
rotateCards();
window.addEventListener("scroll", () => {
  let distance = window.innerHeight / 2;
  let topVal = stackArea.getBoundingClientRect().top;
  let index = -1 * (topVal / distance + 1);
  index = Math.floor(index);
  for (let i = cards.length; i >= 0; i--) {
    if (i <= index) {
      cards[index].classList.add("away");
    }
    else {
      cards[index].classList.remove("away");
    }
  }
  rotateCards();
})

