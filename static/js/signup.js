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


function check_pass() {
    let newp = $("#newpwd").val();
    let cp = $("#cpwd").val();
    if (newp == cp) {
        $("#newpwd").css("border", "1px solid green");
        $("#cpwd").css("border", "1px solid green");
        $('#sbbtn').removeAttr("disabled");

    } else {
        $("#newpwd").css("border", "1px solid red");
        $("#cpwd").css("border", "1px solid red");
        $('#sbbtn').attr("disabled", "disabled");

    }
}