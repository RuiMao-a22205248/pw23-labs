const nightModeButton = document.getElementById('night-mode');
const body = document.body;
const container1 = document.querySelector(".container1");

var video = document.getElementById("background-video");
var changeVideoBtn = document.getElementById("change-video-btn");



nightModeButton.addEventListener('click', function () {
  if (body.classList.contains('night-mode')) {
    body.classList.remove('night-mode');
    nightModeButton.innerHTML = '<i class="fa-solid fa-lightbulb"></i></i>';
    video.src = "img/bg2.mp4";
    body.style.color = '#ffffffda';;

  } else {
    body.classList.add('night-mode');
    nightModeButton.innerHTML = '<i class="fa-regular fa-lightbulb"></i>';
    video.src = "img/bg_b.mp4";
    body.style.color = '#a7a7a7da';
  }
});

const menuClickArea = document.querySelector('.menu-click-area');
const main = document.querySelector('main');
const footer = document.querySelector('.footer-basic');
menuClickArea.addEventListener('click', () => {
  if (main.style.display == 'none') {
    main.style.display = 'flex';
    footer.style.display = 'flex';
  } else {
    main.style.display = 'none';
    footer.style.display = 'none';
  }

});


document.addEventListener("DOMContentLoaded", function () {
  const menuItems = document.querySelectorAll(".menu-item");

  function setActiveMenuItem(entries, observer) {
    entries.forEach(entry => {
      const menuItem = document.querySelector(`a[href="#${entry.target.id}"]`);
      if (entry.isIntersecting) {
        menuItem.classList.add("active");
      } else {
        menuItem.classList.remove("active");
      }
    });
  }

  const options = {
    root: null,
    rootMargin: '0px',
    threshold: 0.5
  };

  const observer = new IntersectionObserver(setActiveMenuItem, options);

  menuItems.forEach(item => {
    const sectionId = item.getAttribute("href");
    const section = document.querySelector(sectionId);
    observer.observe(section);
  });


  menuItems.forEach(item => {
    item.addEventListener("click", (e) => {
      e.preventDefault();
      const target = document.querySelector(item.getAttribute("href"));
      target.scrollIntoView({ behavior: "smooth" });
    });
  });
});










