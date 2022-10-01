$(document).on('click', "#answerindicativoImperfetto", function () {
    runindicativoImperfetto();
});
function runindicativoImperfetto() {

    var exindicativoImperfettoIo = document.getElementById('exindicativoImperfettoIo').value;
    var exindicativoImperfettoTu = document.getElementById('exindicativoImperfettoTu').value;
    var exindicativoImperfettoLui = document.getElementById('exindicativoImperfettoLui').value;
    var exindicativoImperfettoNoi = document.getElementById('exindicativoImperfettoNoi').value;
    var exindicativoImperfettoVoi = document.getElementById('exindicativoImperfettoVoi').value;
    var exindicativoImperfettoLoro = document.getElementById('exindicativoImperfettoLoro').value;

    //io
    var answerindicativoImperfettoIo = document.getElementById('answerindicativoImperfettoIo').value;
    if (exindicativoImperfettoIo == answerindicativoImperfettoIo){
        $('.CSSverbsAnswerindicativoImperfettoIo').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoImperfettoIo').attr('style', 'display: initial; color: red;');
    };

    //tu
    var answerindicativoImperfettoTu = document.getElementById('answerindicativoImperfettoTu').value;
    if (exindicativoImperfettoTu == answerindicativoImperfettoTu){
        $('.CSSverbsAnswerindicativoImperfettoTu').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoImperfettoTu').attr('style', 'display: initial; color: red;');
    };

    //lui
    var answerindicativoImperfettoLui = document.getElementById('answerindicativoImperfettoLui').value;
    if (exindicativoImperfettoLui == answerindicativoImperfettoLui){
        $('.CSSverbsAnswerindicativoImperfettoLui').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoImperfettoLui').attr('style', 'display: initial; color: red;');
    };

    //noi
    var answerindicativoImperfettoNoi = document.getElementById('answerindicativoImperfettoNoi').value;
    if (exindicativoImperfettoNoi == answerindicativoImperfettoNoi){
        $('.CSSverbsAnswerindicativoImperfettoNoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoImperfettoNoi').attr('style', 'display: initial; color: red;');
    };

    //voi
    var answerindicativoImperfettoVoi = document.getElementById('answerindicativoImperfettoVoi').value;
    if (exindicativoImperfettoVoi == answerindicativoImperfettoVoi){
        $('.CSSverbsAnswerindicativoImperfettoVoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoImperfettoVoi').attr('style', 'display: initial; color: red;');
    };

    //loro
    var answerindicativoImperfettoLoro = document.getElementById('answerindicativoImperfettoLoro').value;
    if (exindicativoImperfettoLoro == answerindicativoImperfettoLoro){
        $('.CSSverbsAnswerindicativoImperfettoLoro').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoImperfettoLoro').attr('style', 'display: initial; color: red;');
    };
  };

// Cleaning the form
$(document).on('click', "#ricominciaindicativoImperfetto", function () {
    cleanindicativoImperfetto();
});
function cleanindicativoImperfetto() {
    $('.CSSverbsAnswerindicativoImperfettoIo').attr('style', 'display: none;');
    $('.CSSverbsAnswerindicativoImperfettoTu').attr('style', 'display: none;');
    $('.CSSverbsAnswerindicativoImperfettoLui').attr('style', 'display: none;');
    $('.CSSverbsAnswerindicativoImperfettoNoi').attr('style', 'display: none;');
    $('.CSSverbsAnswerindicativoImperfettoVoi').attr('style', 'display: none;');
    $('.CSSverbsAnswerindicativoImperfettoLoro').attr('style', 'display: none;');

    document.getElementById('formindicativoImperfetto').reset();
};
