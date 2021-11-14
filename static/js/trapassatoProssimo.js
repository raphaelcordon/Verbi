$(document).on('click', "#answertrapassatoProssimo", function () {
    runtrapassatoProssimo();
});
function runtrapassatoProssimo() {

    var extrapassatoProssimoIo = document.getElementById('extrapassatoProssimoIo').value;
    var extrapassatoProssimoTu = document.getElementById('extrapassatoProssimoTu').value;
    var extrapassatoProssimoLui = document.getElementById('extrapassatoProssimoLui').value;
    var extrapassatoProssimoNoi = document.getElementById('extrapassatoProssimoNoi').value;
    var extrapassatoProssimoVoi = document.getElementById('extrapassatoProssimoVoi').value;
    var extrapassatoProssimoLoro = document.getElementById('extrapassatoProssimoLoro').value;

    //io
    var answertrapassatoProssimoIo = document.getElementById('answertrapassatoProssimoIo').value;
    if (extrapassatoProssimoIo == answertrapassatoProssimoIo){
        $('.CSSverbsAnswertrapassatoProssimoIo').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswertrapassatoProssimoIo').attr('style', 'display: initial; color: red;');
    };

    //tu
    var answertrapassatoProssimoTu = document.getElementById('answertrapassatoProssimoTu').value;
    if (extrapassatoProssimoTu == answertrapassatoProssimoTu){
        $('.CSSverbsAnswertrapassatoProssimoTu').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswertrapassatoProssimoTu').attr('style', 'display: initial; color: red;');
    };

    //lui
    var answertrapassatoProssimoLui = document.getElementById('answertrapassatoProssimoLui').value;
    if (extrapassatoProssimoLui == answertrapassatoProssimoLui){
        $('.CSSverbsAnswertrapassatoProssimoLui').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswertrapassatoProssimoLui').attr('style', 'display: initial; color: red;');
    };

    //noi
    var answertrapassatoProssimoNoi = document.getElementById('answertrapassatoProssimoNoi').value;
    if (extrapassatoProssimoNoi == answertrapassatoProssimoNoi){
        $('.CSSverbsAnswertrapassatoProssimoNoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswertrapassatoProssimoNoi').attr('style', 'display: initial; color: red;');
    };

    //voi
    var answertrapassatoProssimoVoi = document.getElementById('answertrapassatoProssimoVoi').value;
    if (extrapassatoProssimoVoi == answertrapassatoProssimoVoi){
        $('.CSSverbsAnswertrapassatoProssimoVoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswertrapassatoProssimoVoi').attr('style', 'display: initial; color: red;');
    };

    //loro
    var answertrapassatoProssimoLoro = document.getElementById('answertrapassatoProssimoLoro').value;
    if (extrapassatoProssimoLoro == answertrapassatoProssimoLoro){
        $('.CSSverbsAnswertrapassatoProssimoLoro').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswertrapassatoProssimoLoro').attr('style', 'display: initial; color: red;');
    };
  };

// Cleaning the form
$(document).on('click', "#ricominciatrapassatoProssimo", function () {
    $('.CSSverbsAnswertrapassatoProssimoIo').attr('style', 'display: none;');
    $('.CSSverbsAnswertrapassatoProssimoTu').attr('style', 'display: none;');
    $('.CSSverbsAnswertrapassatoProssimoLui').attr('style', 'display: none;');
    $('.CSSverbsAnswertrapassatoProssimoNoi').attr('style', 'display: none;');
    $('.CSSverbsAnswertrapassatoProssimoVoi').attr('style', 'display: none;');
    $('.CSSverbsAnswertrapassatoProssimoLoro').attr('style', 'display: none;');

    document.getElementById('formtrapassatoProssimo').reset();
});