// CUSTOM JS
// Add all custom JavaScript here, in a clearn and hierarchical order. Separate by page, if possible.
// Use StandardJS style guide and lint code before pushing.

// ***** HOME *****

$(window).scroll(function () {
  var scroll = $(window).scrollTop();
  if (scroll >= 50) {
    $(".navbar").addClass("navbar-border-bottom");
  } else {
    $(".navbar").removeClass("navbar-border-bottom");
  }
});
