$(document).on('click', "#answerPresente", function () {
    runPresente();
});
function runPresente() {

    var exPresenteIo = document.getElementById('exPresenteIo').value;
    var exPresenteTu = document.getElementById('exPresenteTu').value;
    var exPresenteLui = document.getElementById('exPresenteLui').value;
    var exPresenteNoi = document.getElementById('exPresenteNoi').value;
    var exPresenteVoi = document.getElementById('exPresenteVoi').value;
    var exPresenteLoro = document.getElementById('exPresenteLoro').value;

    //io
    var answerPresenteIo = document.getElementById('answerPresenteIo').value;
    if (exPresenteIo == answerPresenteIo){
        $('.CSSverbsAnswerPresenteIo').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerPresenteIo').attr('style', 'display: initial; color: red;');
    };

    //tu
    var answerPresenteTu = document.getElementById('answerPresenteTu').value;
    if (exPresenteTu == answerPresenteTu){
        $('.CSSverbsAnswerPresenteTu').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerPresenteTu').attr('style', 'display: initial; color: red;');
    };

    //lui
    var answerPresenteLui = document.getElementById('answerPresenteLui').value;
    if (exPresenteLui == answerPresenteLui){
        $('.CSSverbsAnswerPresenteLui').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerPresenteLui').attr('style', 'display: initial; color: red;');
    };

    //noi
    var answerPresenteNoi = document.getElementById('answerPresenteNoi').value;
    if (exPresenteNoi == answerPresenteNoi){
        $('.CSSverbsAnswerPresenteNoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerPresenteNoi').attr('style', 'display: initial; color: red;');
    };

    //voi
    var answerPresenteVoi = document.getElementById('answerPresenteVoi').value;
    if (exPresenteVoi == answerPresenteVoi){
        $('.CSSverbsAnswerPresenteVoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerPresenteVoi').attr('style', 'display: initial; color: red;');
    };

    //loro
    var answerPresenteLoro = document.getElementById('answerPresenteLoro').value;
    if (exPresenteLoro == answerPresenteLoro){
        $('.CSSverbsAnswerPresenteLoro').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerPresenteLoro').attr('style', 'display: initial; color: red;');
    };
  };

// Cleaning the form
$(document).on('click', "#ricominciaPresente", function () {
    cleanPresente();
});
function cleanPresente() {
    $('.CSSverbsAnswerPresenteIo').attr('style', 'display: none;');
    $('.CSSverbsAnswerPresenteTu').attr('style', 'display: none;');
    $('.CSSverbsAnswerPresenteLui').attr('style', 'display: none;');
    $('.CSSverbsAnswerPresenteNoi').attr('style', 'display: none;');
    $('.CSSverbsAnswerPresenteVoi').attr('style', 'display: none;');
    $('.CSSverbsAnswerPresenteLoro').attr('style', 'display: none;');

    document.getElementById('formPresente').reset();
};
