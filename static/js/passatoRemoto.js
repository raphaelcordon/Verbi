$(document).on('click', "#answerpassatoRemoto", function () {
    runpassatoRemoto();
});
function runpassatoRemoto() {

    var expassatoRemotoIo = document.getElementById('expassatoRemotoIo').value;
    var expassatoRemotoTu = document.getElementById('expassatoRemotoTu').value;
    var expassatoRemotoLui = document.getElementById('expassatoRemotoLui').value;
    var expassatoRemotoNoi = document.getElementById('expassatoRemotoNoi').value;
    var expassatoRemotoVoi = document.getElementById('expassatoRemotoVoi').value;
    var expassatoRemotoLoro = document.getElementById('expassatoRemotoLoro').value;

    //io
    var answerpassatoRemotoIo = document.getElementById('answerpassatoRemotoIo').value;
    if (expassatoRemotoIo == answerpassatoRemotoIo){
        $('.CSSverbsAnswerpassatoRemotoIo').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerpassatoRemotoIo').attr('style', 'display: initial; color: red;');
    };

    //tu
    var answerpassatoRemotoTu = document.getElementById('answerpassatoRemotoTu').value;
    if (expassatoRemotoTu == answerpassatoRemotoTu){
        $('.CSSverbsAnswerpassatoRemotoTu').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerpassatoRemotoTu').attr('style', 'display: initial; color: red;');
    };

    //lui
    var answerpassatoRemotoLui = document.getElementById('answerpassatoRemotoLui').value;
    if (expassatoRemotoLui == answerpassatoRemotoLui){
        $('.CSSverbsAnswerpassatoRemotoLui').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerpassatoRemotoLui').attr('style', 'display: initial; color: red;');
    };

    //noi
    var answerpassatoRemotoNoi = document.getElementById('answerpassatoRemotoNoi').value;
    if (expassatoRemotoNoi == answerpassatoRemotoNoi){
        $('.CSSverbsAnswerpassatoRemotoNoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerpassatoRemotoNoi').attr('style', 'display: initial; color: red;');
    };

    //voi
    var answerpassatoRemotoVoi = document.getElementById('answerpassatoRemotoVoi').value;
    if (expassatoRemotoVoi == answerpassatoRemotoVoi){
        $('.CSSverbsAnswerpassatoRemotoVoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerpassatoRemotoVoi').attr('style', 'display: initial; color: red;');
    };

    //loro
    var answerpassatoRemotoLoro = document.getElementById('answerpassatoRemotoLoro').value;
    if (expassatoRemotoLoro == answerpassatoRemotoLoro){
        $('.CSSverbsAnswerpassatoRemotoLoro').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerpassatoRemotoLoro').attr('style', 'display: initial; color: red;');
    };
  };

// Cleaning the form
$(document).on('click', "#ricominciapassatoRemoto", function () {
    cleanpassatoRemoto();
});
function cleanpassatoRemoto() {
    $('.CSSverbsAnswerpassatoRemotoIo').attr('style', 'display: none;');
    $('.CSSverbsAnswerpassatoRemotoTu').attr('style', 'display: none;');
    $('.CSSverbsAnswerpassatoRemotoLui').attr('style', 'display: none;');
    $('.CSSverbsAnswerpassatoRemotoNoi').attr('style', 'display: none;');
    $('.CSSverbsAnswerpassatoRemotoVoi').attr('style', 'display: none;');
    $('.CSSverbsAnswerpassatoRemotoLoro').attr('style', 'display: none;');

    document.getElementById('formpassatoRemoto').reset();
};