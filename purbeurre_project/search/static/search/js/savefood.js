window.onload = function() {
    main()
};

function main() {

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var btn = document.getElementsByClassName('btn-save-food');
    var userSession = document.getElementById('user_session').textContent;
    var titleModalBox = document.getElementById('titleBox');
    var bodyModalBox = document.getElementById('bodyBox');

    if (userSession === 'True') {

        for (let i = 0; i < btn.length; i++) {

            btn[i].addEventListener('click', function (event) {
                var nameFood = btn[i].parentNode.childNodes[1].textContent;
                // alert('bouton ' + i + ' cliquer\nid du produit est ' + btn[i].childNodes[0].textContent +'\nSon nom est ' + nameFood);
                $.ajax({
                    url: '/save_food',
                    type: 'POST',
                    dataType: 'json',
                    data: {'idFood': btn[i].childNodes[0].textContent},
                    success: function (data) {
                        console.log(data);
                        titleModalBox.textContent = 'Sauvegarde...';
                        bodyModalBox.textContent = 'Le produit ' + nameFood + ' a bien été ajouter à vos favoris';
                        $('#modalBox').modal();
                    },
                    error: function (error) {
                        console.log(error);
                        titleModalBox.textContent = 'Erreur';
                        bodyModalBox.textContent = 'Le produit ' + nameFood + " n'a pas été ajouter à vos favoris.\nUne erreur c'est produite.";
                        $('#modalBox').modal();
                    }
                })
            });
        }
    }else {

        for (let i = 0; i < btn.length; i++) {

            btn[i].addEventListener('click', function (event) {
                // alert("Vous devez vous connectez pour sauvegarder l'aliment");
                titleModalBox.textContent = 'Notification';
                bodyModalBox.classList.add('text-danger');
                bodyModalBox.textContent = "Vous devez vous connectez pour sauvegarder l'aliment";
                $('#modalBox').modal();
            });
        }
    }
}