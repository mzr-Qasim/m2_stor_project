  const offcanvasLinks = document.querySelectorAll('#offcanvasRight .theme-links[href^="#"]');

  offcanvasLinks.forEach(link => {
    link.addEventListener('click', (e) => {
      const target = link.getAttribute('href');

      // only scroll if href starts with #
      if(target.startsWith("#") && target.length > 1){
        e.preventDefault(); // prevent default jump

        // smooth scroll to section
        document.querySelector(target).scrollIntoView({ behavior: 'smooth' });

        // close the offcanvas
        const offcanvasEl = document.getElementById('offcanvasRight');
        const bsOffcanvas = bootstrap.Offcanvas.getInstance(offcanvasEl);
        if(bsOffcanvas){
          bsOffcanvas.hide();
        }
      }
    });
  });



var swiper = new Swiper(".mySwiper", {
    slidesPerView: 1,
    spaceBetween: 10,
    breakpoints: {
        768: {
            slidesPerView: 2,
            spaceBetween: 10,
        },
        1024: {
            slidesPerView: 3,
            spaceBetween: 10,
        },
        1200: {
            slidesPerView: 4,
            spaceBetween: 10,
        },
    },
});


window.addEventListener('load', function() {
    if (window.location.hash === "#contact_us") {
        const contactSection = document.getElementById('contact_us');
        if (contactSection) {
            contactSection.scrollIntoView({ behavior: 'smooth' });
        }
    }
});


window.addEventListener('pageshow', function(event) {
    if (event.persisted) {
        document.querySelectorAll('form').forEach(form => form.reset());
    }
});
