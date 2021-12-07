$(document).on('click', "#answerInfinitivo", function () {
    runinfinitivoPresente();
});
function runinfinitivoPresente() {

    var exInfinitivoPresente = document.getElementById('exInfinitivoPresente').value;


    //Infinitivo
    var answerInfinitivoPresente = document.getElementById('answerInfinitivoPresente').value;
    if (exInfinitivoPresente == answerInfinitivoPresente){
        $('.CSSverbsAnswerInfinitivoPresente').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerInfinitivoPresente').attr('style', 'display: initial; color: red;');
    };
  };

// Cleaning the form
$(document).on('click', "#ricominciaInfinitivo", function () {
    cleaninfinitivoPresente();
});
function cleaninfinitivoPresente() {
    $('.CSSverbsAnswerInfinitivoPresente').attr('style', 'display: none;');
    document.getElementById('formInfinitivo').reset();
};
