$(document).on('click', "#answerPresente", function () {
    runPresent();
});
function runPresent() {

    var exPresentIo = document.getElementById('exPresentIo').value;
    var exPresentTu = document.getElementById('exPresentTu').value;
    var exPresentLui = document.getElementById('exPresentLui').value;
    var exPresentNoi = document.getElementById('exPresentNoi').value;
    var exPresentVoi = document.getElementById('exPresentVoi').value;
    var exPresentLoro = document.getElementById('exPresentLoro').value;

    //io
    var answerPresenteIo = document.getElementById('answerPresenteIo').value;
    if (exPresentIo == answerPresenteIo){
        $('.CSSverbsAnswerPresentIo').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerPresentIo').attr('style', 'display: initial; color: red;');
    };

    //tu
    var answerPresenteTu = document.getElementById('answerPresenteTu').value;
    if (exPresentTu == answerPresenteTu){
        $('.CSSverbsAnswerPresentTu').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerPresentTu').attr('style', 'display: initial; color: red;');
    };

    //lui
    var answerPresenteLui = document.getElementById('answerPresenteLui').value;
    if (exPresentLui == answerPresenteLui){
        $('.CSSverbsAnswerPresentLui').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerPresentLui').attr('style', 'display: initial; color: red;');
    };

    //noi
    var answerPresenteNoi = document.getElementById('answerPresenteNoi').value;
    if (exPresentNoi == answerPresenteNoi){
        $('.CSSverbsAnswerPresentNoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerPresentNoi').attr('style', 'display: initial; color: red;');
    };

    //voi
    var answerPresenteVoi = document.getElementById('answerPresenteVoi').value;
    if (exPresentVoi == answerPresenteVoi){
        $('.CSSverbsAnswerPresentVoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerPresentVoi').attr('style', 'display: initial; color: red;');
    };

    //loro
    var answerPresenteLoro = document.getElementById('answerPresenteLoro').value;
    if (exPresentLoro == answerPresenteLoro){
        $('.CSSverbsAnswerPresentLoro').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerPresentLoro').attr('style', 'display: initial; color: red;');
    };
  };

// Cleaning the form
$(document).on('click', "#ricominciaPresente", function () {
    $('.CSSverbsAnswerPresentIo').attr('style', 'display: none;');
    $('.CSSverbsAnswerPresentTu').attr('style', 'display: none;');
    $('.CSSverbsAnswerPresentLui').attr('style', 'display: none;');
    $('.CSSverbsAnswerPresentNoi').attr('style', 'display: none;');
    $('.CSSverbsAnswerPresentVoi').attr('style', 'display: none;');
    $('.CSSverbsAnswerPresentLoro').attr('style', 'display: none;');

    document.getElementById('formPresente').reset();
});
