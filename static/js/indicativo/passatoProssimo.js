$(document).on('click', "#answerindicativoPassatoProssimo", function () {
    runindicativoPassatoProssimo();
});
function runindicativoPassatoProssimo() {

    var exindicativoPassatoProssimoIo = document.getElementById('exindicativoPassatoProssimoIo').value;
    var exindicativoPassatoProssimoTu = document.getElementById('exindicativoPassatoProssimoTu').value;
    var exindicativoPassatoProssimoLui = document.getElementById('exindicativoPassatoProssimoLui').value;
    var exindicativoPassatoProssimoNoi = document.getElementById('exindicativoPassatoProssimoNoi').value;
    var exindicativoPassatoProssimoVoi = document.getElementById('exindicativoPassatoProssimoVoi').value;
    var exindicativoPassatoProssimoLoro = document.getElementById('exindicativoPassatoProssimoLoro').value;

    //io
    var answerindicativoPassatoProssimoIo = document.getElementById('answerindicativoPassatoProssimoIo').value;
    if (exindicativoPassatoProssimoIo == answerindicativoPassatoProssimoIo){
        $('.CSSverbsAnswerindicativoPassatoProssimoIo').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoPassatoProssimoIo').attr('style', 'display: initial; color: red;');
    };

    //tu
    var answerindicativoPassatoProssimoTu = document.getElementById('answerindicativoPassatoProssimoTu').value;
    if (exindicativoPassatoProssimoTu == answerindicativoPassatoProssimoTu){
        $('.CSSverbsAnswerindicativoPassatoProssimoTu').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoPassatoProssimoTu').attr('style', 'display: initial; color: red;');
    };

    //lui
    var answerindicativoPassatoProssimoLui = document.getElementById('answerindicativoPassatoProssimoLui').value;
    if (exindicativoPassatoProssimoLui == answerindicativoPassatoProssimoLui){
        $('.CSSverbsAnswerindicativoPassatoProssimoLui').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoPassatoProssimoLui').attr('style', 'display: initial; color: red;');
    };

    //noi
    var answerindicativoPassatoProssimoNoi = document.getElementById('answerindicativoPassatoProssimoNoi').value;
    if (exindicativoPassatoProssimoNoi == answerindicativoPassatoProssimoNoi){
        $('.CSSverbsAnswerindicativoPassatoProssimoNoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoPassatoProssimoNoi').attr('style', 'display: initial; color: red;');
    };

    //voi
    var answerindicativoPassatoProssimoVoi = document.getElementById('answerindicativoPassatoProssimoVoi').value;
    if (exindicativoPassatoProssimoVoi == answerindicativoPassatoProssimoVoi){
        $('.CSSverbsAnswerindicativoPassatoProssimoVoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoPassatoProssimoVoi').attr('style', 'display: initial; color: red;');
    };

    //loro
    var answerindicativoPassatoProssimoLoro = document.getElementById('answerindicativoPassatoProssimoLoro').value;
    if (exindicativoPassatoProssimoLoro == answerindicativoPassatoProssimoLoro){
        $('.CSSverbsAnswerindicativoPassatoProssimoLoro').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoPassatoProssimoLoro').attr('style', 'display: initial; color: red;');
    };
  };

// Cleaning the form
$(document).on('click', "#ricominciaindicativoPassatoProssimo", function () {
    cleanindicativoPassatoProssimo();
});
function cleanindicativoPassatoProssimo() {
    $('.CSSverbsAnswerindicativoPassatoProssimoIo').attr('style', 'display: none;');
    $('.CSSverbsAnswerindicativoPassatoProssimoTu').attr('style', 'display: none;');
    $('.CSSverbsAnswerindicativoPassatoProssimoLui').attr('style', 'display: none;');
    $('.CSSverbsAnswerindicativoPassatoProssimoNoi').attr('style', 'display: none;');
    $('.CSSverbsAnswerindicativoPassatoProssimoVoi').attr('style', 'display: none;');
    $('.CSSverbsAnswerindicativoPassatoProssimoLoro').attr('style', 'display: none;');

    document.getElementById('formindicativoPassatoProssimo').reset();
};