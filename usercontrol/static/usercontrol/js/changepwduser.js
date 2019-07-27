function changePwdUser() {

    // ************* see the secureajax.js file for more details ******************************
    var csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    // ****************************************************************************************

    var btnChangePwd = document.getElementById('btnChangePwd');
    var btnSave = document.getElementById('btnBoxSavePwd');
    var btnCancel = document.getElementById('btnCancelPwd');
    var status = document.getElementById('bodyBoxPwd');

    btnChangePwd.addEventListener('click', function () {
        $('#modalPwdUser').modal();
    });

    btnSave.addEventListener('click', function () {
        var pwdField = document.getElementById('oldPwd');
        var newPwdField = document.getElementById('newPwd');
        var confirmNewPwdField = document.getElementById('confirmNewPwd');

        if (newPwdField.value === confirmNewPwdField.value) {
            if (newPwdField.value.length >= 8) {
                $.ajax({
                    url: 'change_pwd',
                    type: 'POST',
                    dataType: 'json',
                    data: { 'old_pwd': pwdField.value, 'new_pwd': newPwdField.value, 'confirm_pwd': confirmNewPwdField.value },
                    success: function (data) {

                        if (data === 'True') {
                            var allField = document.getElementsByClassName('complete');

                            for (let i = 0; i < allField.length; i++) {
                                allField[i].classList.add('d-none');
                            }
                            btnSave.classList.add('d-none');
                            btnCancel.innerHTML = 'Fermer';
                            status.innerHTML = 'Mot de passe changez avec succes';
                            status.classList.add('text-success');
                        } else {
                            status.innerHTML = "Veuillez indiquer votre mot de passe actuel.";
                            status.classList.add('text-danger');
                            pwdField.classList.add('is-invalid');
                        }
                    },
                    error: function (error) {
                        console.log(error);
                    },
                });
            } else {
                status.innerHTML = "Votre nouveau mot de passe dois faire au moins 8 caractères. Veuillez corriger cela.";
                status.classList.add('text-danger');
                newPwdField.classList.add('is-invalid');
            }

        } else {
            status.innerHTML = "La confirmation de votre mot de passe est différente. Veuillez corriger cela.";
            status.classList.add('text-danger');
            confirmNewPwdField.classList.add('is-invalid');
        }
    });
}