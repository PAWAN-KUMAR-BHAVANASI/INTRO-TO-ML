window.addEventListener('scroll', function() {
    const logo = document.querySelector('.logo');
    const scrollPosition = window.scrollY;

    if (scrollPosition > 100) { // Adjust the scroll value as needed
        logo.classList.add('scrolled');
    } else {
        logo.classList.remove('scrolled');
    }
});
