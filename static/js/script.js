function disableButton(optbtn,femail,otp,reset)
{
    var email_val = document.getElementById(femail.id).value;
    if (email_val.length > 10){
        optbtn.disabled = true;
        document.getElementById(femail.id).disabled = true;
        document.getElementById(otp.id).disabled = false;
        document.getElementById(reset.id).disabled = false;
    }
}


