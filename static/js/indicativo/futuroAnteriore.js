$(document).on('click', "#answerindicativoFuturoAnteriore", function () {
    runindicativoFuturoAnteriore();
});
function runindicativoFuturoAnteriore() {

    var exindicativoFuturoAnterioreIo = document.getElementById('exindicativoFuturoAnterioreIo').value;
    var exindicativoFuturoAnterioreTu = document.getElementById('exindicativoFuturoAnterioreTu').value;
    var exindicativoFuturoAnterioreLui = document.getElementById('exindicativoFuturoAnterioreLui').value;
    var exindicativoFuturoAnterioreNoi = document.getElementById('exindicativoFuturoAnterioreNoi').value;
    var exindicativoFuturoAnterioreVoi = document.getElementById('exindicativoFuturoAnterioreVoi').value;
    var exindicativoFuturoAnterioreLoro = document.getElementById('exindicativoFuturoAnterioreLoro').value;

    //io
    var answerindicativoFuturoAnterioreIo = document.getElementById('answerindicativoFuturoAnterioreIo').value;
    if (exindicativoFuturoAnterioreIo == answerindicativoFuturoAnterioreIo){
        $('.CSSverbsAnswerindicativoFuturoAnterioreIo').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoFuturoAnterioreIo').attr('style', 'display: initial; color: red;');
    };

    //tu
    var answerindicativoFuturoAnterioreTu = document.getElementById('answerindicativoFuturoAnterioreTu').value;
    if (exindicativoFuturoAnterioreTu == answerindicativoFuturoAnterioreTu){
        $('.CSSverbsAnswerindicativoFuturoAnterioreTu').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoFuturoAnterioreTu').attr('style', 'display: initial; color: red;');
    };

    //lui
    var answerindicativoFuturoAnterioreLui = document.getElementById('answerindicativoFuturoAnterioreLui').value;
    if (exindicativoFuturoAnterioreLui == answerindicativoFuturoAnterioreLui){
        $('.CSSverbsAnswerindicativoFuturoAnterioreLui').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoFuturoAnterioreLui').attr('style', 'display: initial; color: red;');
    };

    //noi
    var answerindicativoFuturoAnterioreNoi = document.getElementById('answerindicativoFuturoAnterioreNoi').value;
    if (exindicativoFuturoAnterioreNoi == answerindicativoFuturoAnterioreNoi){
        $('.CSSverbsAnswerindicativoFuturoAnterioreNoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoFuturoAnterioreNoi').attr('style', 'display: initial; color: red;');
    };

    //voi
    var answerindicativoFuturoAnterioreVoi = document.getElementById('answerindicativoFuturoAnterioreVoi').value;
    if (exindicativoFuturoAnterioreVoi == answerindicativoFuturoAnterioreVoi){
        $('.CSSverbsAnswerindicativoFuturoAnterioreVoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoFuturoAnterioreVoi').attr('style', 'display: initial; color: red;');
    };

    //loro
    var answerindicativoFuturoAnterioreLoro = document.getElementById('answerindicativoFuturoAnterioreLoro').value;
    if (exindicativoFuturoAnterioreLoro == answerindicativoFuturoAnterioreLoro){
        $('.CSSverbsAnswerindicativoFuturoAnterioreLoro').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoFuturoAnterioreLoro').attr('style', 'display: initial; color: red;');
    };
  };

// Cleaning the form
$(document).on('click', "#ricominciaindicativoFuturoAnteriore", function () {
    cleanindicativoFuturoAnteriore();
});
function cleanindicativoFuturoAnteriore() {

    $('.CSSverbsAnswerindicativoFuturoAnterioreIo').attr('style', 'display: none;');
    $('.CSSverbsAnswerindicativoFuturoAnterioreTu').attr('style', 'display: none;');
    $('.CSSverbsAnswerindicativoFuturoAnterioreLui').attr('style', 'display: none;');
    $('.CSSverbsAnswerindicativoFuturoAnterioreNoi').attr('style', 'display: none;');
    $('.CSSverbsAnswerindicativoFuturoAnterioreVoi').attr('style', 'display: none;');
    $('.CSSverbsAnswerindicativoFuturoAnterioreLoro').attr('style', 'display: none;');

    document.getElementById('formindicativoFuturoAnteriore').reset();
};