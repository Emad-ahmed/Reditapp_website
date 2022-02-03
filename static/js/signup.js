$(".forgot-pass-link").click(function() {
    $(".sign-in-form").removeClass("active");
    $(".forgot-pass-form").addClass("active");
});

$(".go-to-sign-in").click('click', '.alink', function() {
    $(".sign-in-form").addClass("active");
    $(".forgot-pass-form").removeClass("active");
});

$(".sign-up-form-btn").click(function() {
    $(".sign-in-form").removeClass("active");
    $(".sign-up-form").addClass("active");
});

$(".sign-in-form-btn").click(function() {
    $(".sign-in-form").addClass("active");
    $(".sign-up-form").removeClass("active");
});

$(".dark-mode-btn").click(function() {
    $(this).toggleClass("active");
    $("body").toggleClass("dark-mode-on");
});