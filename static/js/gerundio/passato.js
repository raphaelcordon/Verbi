$(document).on('click', "#answergerundioPassato", function () {
    rungerundioPassato();
});
function rungerundioPassato() {

    var exgerundioPassato = document.getElementById('exgerundioPassato').value;


    //Gerundio Passato
    var answergerundioPassato = document.getElementById('answergerundioPassatoIo').value;
    if (exgerundioPassato == answergerundioPassato){
        $('.CSSverbsAnswergerundioPassato').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswergerundioPassato').attr('style', 'display: initial; color: red;');
    };
  };

// Cleaning the form
$(document).on('click', "#ricominciagerundioPassato", function () {
    cleangerundioPassato();
});
function cleangerundioPassato() {
    $('.CSSverbsAnswergerundioPassato').attr('style', 'display: none;');


    document.getElementById('formgerundioPassato').reset();
};