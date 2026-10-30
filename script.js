
const toggle = document.querySelector('.menu-toggle');

const links = document.querySelector('.nav-links');

// Mobile navigation
toggle.addEventListener('click', () => {

    const open = links.classList.toggle('open');

    toggle.setAttribute('aria-expanded', open);

    toggle.innerHTML = open
        ? '<i class="fa-solid fa-xmark"></i>'
        : '<i class="fa-solid fa-bars"></i>';

});

// Close menu after clicking a link
document.querySelectorAll('.nav-links a').forEach(link => {

    link.addEventListener('click', () => {

        links.classList.remove('open');

        toggle.setAttribute('aria-expanded', 'false');

        toggle.innerHTML =
            '<i class="fa-solid fa-bars"></i>';

    });

});

// Automatic copyright year
document.getElementById('year').textContent =
    new Date().getFullYear();
