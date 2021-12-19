

function print_my_name() {
	document.getElementById("name").innerHTML = "Idan Herscovich"
}

function next_page() {
	window.location.href = "CV.html";
}

var check_phone = /^[0-9 ]{3,20}$/;
var ck_email = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;

function vaidate_form(form){
	var phone = form.mobile.value
	var email = form.email.value
	var errors = [];

    if (!check_phone.test(phone)) {
        errors[errors.length] = "Name is not valid";
    }
    if (!ck_email.test(email)) {
        errors[errors.length] = "Email not valid";
    }
    if (errors.length > 0) {

        reportErrors(errors);
        return false;
    }
    return true;
}


function reportErrors(errors) {
    var msg = "You have mistakes in the form, please try again, the mistakes are:\n";
    for (var i = 0; i < errors.length; i++) {
        var numError = i + 1;
        msg += "\n" + numError + ". " + errors[i];
    }
    alert(msg);
}



