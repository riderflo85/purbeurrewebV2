function notMatch() {

    var match = document.getElementById('match');

    if (match !== null) {
        var titleBox = document.getElementById('titleBox');
        var bodyBox = document.getElementById('bodyBox');
        var buttonClose = document.getElementById('btnClose');
        var buttonRedirect = document.getElementById('btnRedirect');

        buttonClose.classList.add('d-none');
        buttonRedirect.classList.remove('d-none');
        titleBox.textContent = 'Erreur...';
        bodyBox.textContent = "Aucun produit n'a été trouver pour votre recherche";
        $('#modalBox').modal();
    }else{
        // pass
    }
}