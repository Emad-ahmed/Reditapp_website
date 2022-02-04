$(".dark-mode-btn").click(function() {
    var b =
        $(this).toggleClass("active");
    $("body").toggleClass("dark-mode-on");
});