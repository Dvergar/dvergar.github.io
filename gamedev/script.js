$(document).ready( function () {
    
    // Close mobile & tablet menu on item click
    $('.navbar-item').each(function(e) {
        $(this).click(function(){
        if($('#navbar-burger').hasClass('is-active')){
            $('#navbar-burger').removeClass('is-active');
            $('#navbar-menu').removeClass('is-active');
        }
        });
    });

    // BULMA HAMBURGER
    var burger = document.querySelector('.burger');
    var nav = document.querySelector('#'+burger.dataset.target);
    
    burger.addEventListener('click', function(){
        burger.classList.toggle('is-active');
        nav.classList.toggle('is-active');
    });

});