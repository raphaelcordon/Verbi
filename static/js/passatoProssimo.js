$(document).on('click', "#answerpassatoProssimo", function () {

    var expassatoProssimoIo = document.getElementById('expassatoProssimoIo').value;
    var expassatoProssimoTu = document.getElementById('expassatoProssimoTu').value;
    var expassatoProssimoLui = document.getElementById('expassatoProssimoLui').value;
    var expassatoProssimoNoi = document.getElementById('expassatoProssimoNoi').value;
    var expassatoProssimoVoi = document.getElementById('expassatoProssimoVoi').value;
    var expassatoProssimoLoro = document.getElementById('expassatoProssimoLoro').value;

    //io
    var answerpassatoProssimoIo = document.getElementById('answerpassatoProssimoIo').value;
    if (expassatoProssimoIo == answerpassatoProssimoIo){
        $('.CSSverbsAnswerpassatoProssimoIo').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerpassatoProssimoIo').attr('style', 'display: initial; color: red;');
    };

    //tu
    var answerpassatoProssimoTu = document.getElementById('answerpassatoProssimoTu').value;
    if (expassatoProssimoTu == answerpassatoProssimoTu){
        $('.CSSverbsAnswerpassatoProssimoTu').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerpassatoProssimoTu').attr('style', 'display: initial; color: red;');
    };

    //lui
    var answerpassatoProssimoLui = document.getElementById('answerpassatoProssimoLui').value;
    if (expassatoProssimoLui == answerpassatoProssimoLui){
        $('.CSSverbsAnswerpassatoProssimoLui').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerpassatoProssimoLui').attr('style', 'display: initial; color: red;');
    };

    //noi
    var answerpassatoProssimoNoi = document.getElementById('answerpassatoProssimoNoi').value;
    if (expassatoProssimoNoi == answerpassatoProssimoNoi){
        $('.CSSverbsAnswerpassatoProssimoNoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerpassatoProssimoNoi').attr('style', 'display: initial; color: red;');
    };

    //voi
    var answerpassatoProssimoVoi = document.getElementById('answerpassatoProssimoVoi').value;
    if (expassatoProssimoVoi == answerpassatoProssimoVoi){
        $('.CSSverbsAnswerpassatoProssimoVoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerpassatoProssimoVoi').attr('style', 'display: initial; color: red;');
    };

    //loro
    var answerpassatoProssimoLoro = document.getElementById('answerpassatoProssimoLoro').value;
    if (expassatoProssimoLoro == answerpassatoProssimoLoro){
        $('.CSSverbsAnswerpassatoProssimoLoro').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerpassatoProssimoLoro').attr('style', 'display: initial; color: red;');
    };
  });