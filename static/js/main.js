"use strict";

/* ======= Header animation ======= */
const header = document.getElementById('header');

window.onload=function()
{
    headerAnimation();

};

window.onresize=function()
{
    headerAnimation();

};

window.onscroll=function()
{
    headerAnimation();

};


function headerAnimation () {

    var scrollTop = window.scrollY;

	if ( scrollTop > -1 ) {
	    header.classList.add('header-scrolled');

	} else {
	    header.classList.remove('header-scrolled');
	}

};


/* ===== Gumshoe SrollSpy ===== */
/* Ref: https://github.com/cferdinandi/gumshoe  */

// Initialize Gumshoe
var spy = new Gumshoe('.main-nav .nav-link', {
	offset: 61
});


/* ==== Vanilla JS Back To Top Widget ====== */
/* Ref: https://github.com/vfeskov/vanilla-back-to-top */
addBackToTop({
  cornerOffset: 15, // px
  id:'back-to-top',
});


/* ====== SimpleLightbox Plugin ======= */
/*  Ref: https://github.com/andreknieriem/simplelightbox */

var lightbox = new SimpleLightbox('.media-wrapper a.mask', {
	//Options
	animationSlide:false
});




// VanillaJS Datepicker
var datepickers = [].slice.call(document.querySelectorAll('.datepicker-input'))
var datepickersList = datepickers.map(function (elem) {
    return new Datepicker(elem, {
        buttonClass: 'btn'
      });
});







