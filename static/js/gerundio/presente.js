$(document).on('click', "#answergerundioPresente", function () {
    rungerundioPresente();
});
function rungerundioPresente() {

    var exgerundioPresente = document.getElementById('exgerundioPresente').value;


    //Gerundio Presente
    var answergerundioPresente = document.getElementById('answergerundioPresenteIo').value;
    if (exgerundioPresente == answergerundioPresente){
        $('.CSSverbsAnswergerundioPresente').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswergerundioPresente').attr('style', 'display: initial; color: red;');
    };
  };

// Cleaning the form
$(document).on('click', "#ricominciagerundioPresente", function () {
    cleangerundioPresente();
});
function cleangerundioPresente() {
    $('.CSSverbsAnswergerundioPresente').attr('style', 'display: none;');
    document.getElementById('formgerundioPresente').reset();
};
