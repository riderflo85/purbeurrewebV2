window.onload = function() {
    main()
};

function main() {

    var btn = document.getElementsByClassName('btn-save-food');
    var userSession = document.getElementById('user_session').textContent;
    var titleModalBox = document.getElementById('titleBox');
    var bodyModalBox = document.getElementById('bodyBox');

    if (userSession === 'True') {

        for (let i = 0; i < btn.length; i++) {

            btn[i].addEventListener('click', function (event) {
                var nameFood = btn[i].parentNode.childNodes[1].textContent;
                // alert('bouton ' + i + ' cliquer\nid du produit est ' + btn[i].childNodes[0].textContent +'\nSon nom est ' + nameFood);
                titleModalBox.textContent = 'Sauvegarde...';
                bodyModalBox.textContent = 'Le produit ' + nameFood + ' a bien été ajouter à vos favoris';
                $('#modalBox').modal();
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