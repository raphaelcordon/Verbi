$(document).on('click', "#answerImperfetto", function () {
    runImperfetto();
});
function runImperfetto() {

    var exImperfettoIo = document.getElementById('exImperfettoIo').value;
    var exImperfettoTu = document.getElementById('exImperfettoTu').value;
    var exImperfettoLui = document.getElementById('exImperfettoLui').value;
    var exImperfettoNoi = document.getElementById('exImperfettoNoi').value;
    var exImperfettoVoi = document.getElementById('exImperfettoVoi').value;
    var exImperfettoLoro = document.getElementById('exImperfettoLoro').value;

    //io
    var answerImperfettoIo = document.getElementById('answerImperfettoIo').value;
    if (exImperfettoIo == answerImperfettoIo){
        $('.CSSverbsAnswerImperfettoIo').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerImperfettoIo').attr('style', 'display: initial; color: red;');
    };

    //tu
    var answerImperfettoTu = document.getElementById('answerImperfettoTu').value;
    if (exImperfettoTu == answerImperfettoTu){
        $('.CSSverbsAnswerImperfettoTu').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerImperfettoTu').attr('style', 'display: initial; color: red;');
    };

    //lui
    var answerImperfettoLui = document.getElementById('answerImperfettoLui').value;
    if (exImperfettoLui == answerImperfettoLui){
        $('.CSSverbsAnswerImperfettoLui').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerImperfettoLui').attr('style', 'display: initial; color: red;');
    };

    //noi
    var answerImperfettoNoi = document.getElementById('answerImperfettoNoi').value;
    if (exImperfettoNoi == answerImperfettoNoi){
        $('.CSSverbsAnswerImperfettoNoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerImperfettoNoi').attr('style', 'display: initial; color: red;');
    };

    //voi
    var answerImperfettoVoi = document.getElementById('answerImperfettoVoi').value;
    if (exImperfettoVoi == answerImperfettoVoi){
        $('.CSSverbsAnswerImperfettoVoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerImperfettoVoi').attr('style', 'display: initial; color: red;');
    };

    //loro
    var answerImperfettoLoro = document.getElementById('answerImperfettoLoro').value;
    if (exImperfettoLoro == answerImperfettoLoro){
        $('.CSSverbsAnswerImperfettoLoro').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerImperfettoLoro').attr('style', 'display: initial; color: red;');
    };
  };

// Cleaning the form
$(document).on('click', "#ricominciaImperfetto", function () {
    $('.CSSverbsAnswerImperfettoIo').attr('style', 'display: none;');
    $('.CSSverbsAnswerImperfettoTu').attr('style', 'display: none;');
    $('.CSSverbsAnswerImperfettoLui').attr('style', 'display: none;');
    $('.CSSverbsAnswerImperfettoNoi').attr('style', 'display: none;');
    $('.CSSverbsAnswerImperfettoVoi').attr('style', 'display: none;');
    $('.CSSverbsAnswerImperfettoLoro').attr('style', 'display: none;');

    document.getElementById('formImperfetto').reset();
});
