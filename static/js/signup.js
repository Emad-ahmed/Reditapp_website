$(".dark-mode-btn").click(function() {
    var b =
        $(this).toggleClass("active");
    $("body").toggleClass("dark-mode-on");
});


function myFunction() {
    var x = document.getElementById("id_password");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}