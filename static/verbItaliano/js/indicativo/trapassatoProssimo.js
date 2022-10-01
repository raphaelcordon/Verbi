$(document).on('click', "#answerindicativoTrapassatoProssimo", function () {
    runindicativoTrapassatoProssimo();
});
function runindicativoTrapassatoProssimo() {

    var exindicativoTrapassatoProssimoIo = document.getElementById('exindicativoTrapassatoProssimoIo').value;
    var exindicativoTrapassatoProssimoTu = document.getElementById('exindicativoTrapassatoProssimoTu').value;
    var exindicativoTrapassatoProssimoLui = document.getElementById('exindicativoTrapassatoProssimoLui').value;
    var exindicativoTrapassatoProssimoNoi = document.getElementById('exindicativoTrapassatoProssimoNoi').value;
    var exindicativoTrapassatoProssimoVoi = document.getElementById('exindicativoTrapassatoProssimoVoi').value;
    var exindicativoTrapassatoProssimoLoro = document.getElementById('exindicativoTrapassatoProssimoLoro').value;

    //io
    var answerindicativoTrapassatoProssimoIo = document.getElementById('answerindicativoTrapassatoProssimoIo').value;
    if (exindicativoTrapassatoProssimoIo == answerindicativoTrapassatoProssimoIo){
        $('.CSSverbsAnswerindicativoTrapassatoProssimoIo').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoTrapassatoProssimoIo').attr('style', 'display: initial; color: red;');
    };

    //tu
    var answerindicativoTrapassatoProssimoTu = document.getElementById('answerindicativoTrapassatoProssimoTu').value;
    if (exindicativoTrapassatoProssimoTu == answerindicativoTrapassatoProssimoTu){
        $('.CSSverbsAnswerindicativoTrapassatoProssimoTu').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoTrapassatoProssimoTu').attr('style', 'display: initial; color: red;');
    };

    //lui
    var answerindicativoTrapassatoProssimoLui = document.getElementById('answerindicativoTrapassatoProssimoLui').value;
    if (exindicativoTrapassatoProssimoLui == answerindicativoTrapassatoProssimoLui){
        $('.CSSverbsAnswerindicativoTrapassatoProssimoLui').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoTrapassatoProssimoLui').attr('style', 'display: initial; color: red;');
    };

    //noi
    var answerindicativoTrapassatoProssimoNoi = document.getElementById('answerindicativoTrapassatoProssimoNoi').value;
    if (exindicativoTrapassatoProssimoNoi == answerindicativoTrapassatoProssimoNoi){
        $('.CSSverbsAnswerindicativoTrapassatoProssimoNoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoTrapassatoProssimoNoi').attr('style', 'display: initial; color: red;');
    };

    //voi
    var answerindicativoTrapassatoProssimoVoi = document.getElementById('answerindicativoTrapassatoProssimoVoi').value;
    if (exindicativoTrapassatoProssimoVoi == answerindicativoTrapassatoProssimoVoi){
        $('.CSSverbsAnswerindicativoTrapassatoProssimoVoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoTrapassatoProssimoVoi').attr('style', 'display: initial; color: red;');
    };

    //loro
    var answerindicativoTrapassatoProssimoLoro = document.getElementById('answerindicativoTrapassatoProssimoLoro').value;
    if (exindicativoTrapassatoProssimoLoro == answerindicativoTrapassatoProssimoLoro){
        $('.CSSverbsAnswerindicativoTrapassatoProssimoLoro').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoTrapassatoProssimoLoro').attr('style', 'display: initial; color: red;');
    };
  };

// Cleaning the form
$(document).on('click', "#ricominciaindicativoTrapassatoProssimo", function () {
    cleanindicativoTrapassatoProssimo();
});
function cleanindicativoTrapassatoProssimo() {
    $('.CSSverbsAnswerindicativoTrapassatoProssimoIo').attr('style', 'display: none;');
    $('.CSSverbsAnswerindicativoTrapassatoProssimoTu').attr('style', 'display: none;');
    $('.CSSverbsAnswerindicativoTrapassatoProssimoLui').attr('style', 'display: none;');
    $('.CSSverbsAnswerindicativoTrapassatoProssimoNoi').attr('style', 'display: none;');
    $('.CSSverbsAnswerindicativoTrapassatoProssimoVoi').attr('style', 'display: none;');
    $('.CSSverbsAnswerindicativoTrapassatoProssimoLoro').attr('style', 'display: none;');

    document.getElementById('formindicativoTrapassatoProssimo').reset();
};