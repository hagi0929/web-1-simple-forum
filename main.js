function check_pw(pe) {
    var pwd = prompt("비번:")
    var form = document.getElementById(pe);
    document.getElementById("hidden_pw1").setAttribute('value', pwd)
    document.getElementById("hidden_pw2").setAttribute('value', pwd)
    form.submit();
}
