$(document).on('click', "#answerindicativoFuturoSemplice", function () {
    runindicativoFuturoSemplice();
});
function runindicativoFuturoSemplice() {

    var exindicativoFuturoSempliceIo = document.getElementById('exindicativoFuturoSempliceIo').value;
    var exindicativoFuturoSempliceTu = document.getElementById('exindicativoFuturoSempliceTu').value;
    var exindicativoFuturoSempliceLui = document.getElementById('exindicativoFuturoSempliceLui').value;
    var exindicativoFuturoSempliceNoi = document.getElementById('exindicativoFuturoSempliceNoi').value;
    var exindicativoFuturoSempliceVoi = document.getElementById('exindicativoFuturoSempliceVoi').value;
    var exindicativoFuturoSempliceLoro = document.getElementById('exindicativoFuturoSempliceLoro').value;

    //io
    var answerindicativoFuturoSempliceIo = document.getElementById('answerindicativoFuturoSempliceIo').value;
    if (exindicativoFuturoSempliceIo == answerindicativoFuturoSempliceIo){
        $('.CSSverbsAnswerindicativoFuturoSempliceIo').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoFuturoSempliceIo').attr('style', 'display: initial; color: red;');
    };

    //tu
    var answerindicativoFuturoSempliceTu = document.getElementById('answerindicativoFuturoSempliceTu').value;
    if (exindicativoFuturoSempliceTu == answerindicativoFuturoSempliceTu){
        $('.CSSverbsAnswerindicativoFuturoSempliceTu').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoFuturoSempliceTu').attr('style', 'display: initial; color: red;');
    };

    //lui
    var answerindicativoFuturoSempliceLui = document.getElementById('answerindicativoFuturoSempliceLui').value;
    if (exindicativoFuturoSempliceLui == answerindicativoFuturoSempliceLui){
        $('.CSSverbsAnswerindicativoFuturoSempliceLui').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoFuturoSempliceLui').attr('style', 'display: initial; color: red;');
    };

    //noi
    var answerindicativoFuturoSempliceNoi = document.getElementById('answerindicativoFuturoSempliceNoi').value;
    if (exindicativoFuturoSempliceNoi == answerindicativoFuturoSempliceNoi){
        $('.CSSverbsAnswerindicativoFuturoSempliceNoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoFuturoSempliceNoi').attr('style', 'display: initial; color: red;');
    };

    //voi
    var answerindicativoFuturoSempliceVoi = document.getElementById('answerindicativoFuturoSempliceVoi').value;
    if (exindicativoFuturoSempliceVoi == answerindicativoFuturoSempliceVoi){
        $('.CSSverbsAnswerindicativoFuturoSempliceVoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoFuturoSempliceVoi').attr('style', 'display: initial; color: red;');
    };

    //loro
    var answerindicativoFuturoSempliceLoro = document.getElementById('answerindicativoFuturoSempliceLoro').value;
    if (exindicativoFuturoSempliceLoro == answerindicativoFuturoSempliceLoro){
        $('.CSSverbsAnswerindicativoFuturoSempliceLoro').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoFuturoSempliceLoro').attr('style', 'display: initial; color: red;');
    };
  };

// Cleaning the form
$(document).on('click', "#ricominciaindicativoFuturoSemplice", function () {
    cleanindicativoFuturoSemplice();
});
function cleanindicativoFuturoSemplice() {
    $('.CSSverbsAnswerindicativoFuturoSempliceIo').attr('style', 'display: none;');
    $('.CSSverbsAnswerindicativoFuturoSempliceTu').attr('style', 'display: none;');
    $('.CSSverbsAnswerindicativoFuturoSempliceLui').attr('style', 'display: none;');
    $('.CSSverbsAnswerindicativoFuturoSempliceNoi').attr('style', 'display: none;');
    $('.CSSverbsAnswerindicativoFuturoSempliceVoi').attr('style', 'display: none;');
    $('.CSSverbsAnswerindicativoFuturoSempliceLoro').attr('style', 'display: none;');

    document.getElementById('formindicativoFuturoSemplice').reset();
};