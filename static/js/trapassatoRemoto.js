$(document).on('click', "#answertrapassatoRemoto", function () {
    runtrapassatoRemoto();
});
function runtrapassatoRemoto() {

    var extrapassatoRemotoIo = document.getElementById('extrapassatoRemotoIo').value;
    var extrapassatoRemotoTu = document.getElementById('extrapassatoRemotoTu').value;
    var extrapassatoRemotoLui = document.getElementById('extrapassatoRemotoLui').value;
    var extrapassatoRemotoNoi = document.getElementById('extrapassatoRemotoNoi').value;
    var extrapassatoRemotoVoi = document.getElementById('extrapassatoRemotoVoi').value;
    var extrapassatoRemotoLoro = document.getElementById('extrapassatoRemotoLoro').value;

    //io
    var answertrapassatoRemotoIo = document.getElementById('answertrapassatoRemotoIo').value;
    if (extrapassatoRemotoIo == answertrapassatoRemotoIo){
        $('.CSSverbsAnswertrapassatoRemotoIo').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswertrapassatoRemotoIo').attr('style', 'display: initial; color: red;');
    };

    //tu
    var answertrapassatoRemotoTu = document.getElementById('answertrapassatoRemotoTu').value;
    if (extrapassatoRemotoTu == answertrapassatoRemotoTu){
        $('.CSSverbsAnswertrapassatoRemotoTu').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswertrapassatoRemotoTu').attr('style', 'display: initial; color: red;');
    };

    //lui
    var answertrapassatoRemotoLui = document.getElementById('answertrapassatoRemotoLui').value;
    if (extrapassatoRemotoLui == answertrapassatoRemotoLui){
        $('.CSSverbsAnswertrapassatoRemotoLui').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswertrapassatoRemotoLui').attr('style', 'display: initial; color: red;');
    };

    //noi
    var answertrapassatoRemotoNoi = document.getElementById('answertrapassatoRemotoNoi').value;
    if (extrapassatoRemotoNoi == answertrapassatoRemotoNoi){
        $('.CSSverbsAnswertrapassatoRemotoNoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswertrapassatoRemotoNoi').attr('style', 'display: initial; color: red;');
    };

    //voi
    var answertrapassatoRemotoVoi = document.getElementById('answertrapassatoRemotoVoi').value;
    if (extrapassatoRemotoVoi == answertrapassatoRemotoVoi){
        $('.CSSverbsAnswertrapassatoRemotoVoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswertrapassatoRemotoVoi').attr('style', 'display: initial; color: red;');
    };

    //loro
    var answertrapassatoRemotoLoro = document.getElementById('answertrapassatoRemotoLoro').value;
    if (extrapassatoRemotoLoro == answertrapassatoRemotoLoro){
        $('.CSSverbsAnswertrapassatoRemotoLoro').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswertrapassatoRemotoLoro').attr('style', 'display: initial; color: red;');
    };
  };

// Cleaning the form
$(document).on('click', "#ricominciatrapassatoRemoto", function () {
    cleantrapassatoRemoto();
});
function cleantrapassatoRemoto() {
    $('.CSSverbsAnswertrapassatoRemotoIo').attr('style', 'display: none;');
    $('.CSSverbsAnswertrapassatoRemotoTu').attr('style', 'display: none;');
    $('.CSSverbsAnswertrapassatoRemotoLui').attr('style', 'display: none;');
    $('.CSSverbsAnswertrapassatoRemotoNoi').attr('style', 'display: none;');
    $('.CSSverbsAnswertrapassatoRemotoVoi').attr('style', 'display: none;');
    $('.CSSverbsAnswertrapassatoRemotoLoro').attr('style', 'display: none;');

    document.getElementById('formtrapassatoRemoto').reset();
};