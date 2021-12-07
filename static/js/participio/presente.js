$(document).on('click', "#answerparticipioPresente", function () {
    runparticipioPresente();
});
function runparticipioPresente() {

    var exparticipioPresente = document.getElementById('exparticipioPresente').value;


    //Participio Presente
    var answerparticipioPresente = document.getElementById('answerparticipioPresenteIo').value;
    if (exparticipioPresente == answerparticipioPresente){
        $('.CSSverbsAnswerparticipioPresente').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerparticipioPresente').attr('style', 'display: initial; color: red;');
    };
  };

// Cleaning the form
$(document).on('click', "#ricominciaparticipioPresente", function () {
    cleanparticipioPresente();
});
function cleanparticipioPresente() {
    $('.CSSverbsAnswerparticipioPresente').attr('style', 'display: none;');
    document.getElementById('formparticipioPresente').reset();
};
