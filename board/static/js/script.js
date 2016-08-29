(function ($) {
  $(document).ready(function(){

    // hide .navbar first
    $(".navbar-fixed-top").hide();

    // fade in .navbar
    $(function () {
        $(window).scroll(function () {

                 // set distance user needs to scroll before we start fadeIn
            if ($(this).scrollTop() > 50) {
                $('.navbar-fixed-top').fadeIn();
            } else {
                $('.navbar-fixed-top').fadeOut();
            }
        });
    });

});
  }(jQuery));



