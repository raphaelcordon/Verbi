$(document).on('click', "#answerInfinitivoPassato", function () {
    runinfinitivoPassato();
});
function runinfinitivoPassato() {

    var exInfinitivoPassato = document.getElementById('exInfinitivoPassato').value;


    //InfinitivoPassato
    var answerInfinitivoPassato = document.getElementById('answerInfinitivoPassatoIo').value;
    if (exInfinitivoPassato == answerInfinitivoPassato){
        $('.CSSverbsAnswerInfinitivoPassato').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerInfinitivoPassato').attr('style', 'display: initial; color: red;');
    };
  };

// Cleaning the form
$(document).on('click', "#ricominciaInfinitivoPassato", function () {
    cleaninfinitivoPassato();
});
function cleaninfinitivoPassato() {
    $('.CSSverbsAnswerInfinitivoPassato').attr('style', 'display: none;');


    document.getElementById('formInfinitivoPassato').reset();
};