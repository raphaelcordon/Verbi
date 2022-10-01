$(document).on('click', "#answerindicativoTrapassatoRemoto", function () {
    runindicativoTrapassatoRemoto();
});
function runindicativoTrapassatoRemoto() {

    var exindicativoTrapassatoRemotoIo = document.getElementById('exindicativoTrapassatoRemotoIo').value;
    var exindicativoTrapassatoRemotoTu = document.getElementById('exindicativoTrapassatoRemotoTu').value;
    var exindicativoTrapassatoRemotoLui = document.getElementById('exindicativoTrapassatoRemotoLui').value;
    var exindicativoTrapassatoRemotoNoi = document.getElementById('exindicativoTrapassatoRemotoNoi').value;
    var exindicativoTrapassatoRemotoVoi = document.getElementById('exindicativoTrapassatoRemotoVoi').value;
    var exindicativoTrapassatoRemotoLoro = document.getElementById('exindicativoTrapassatoRemotoLoro').value;

    //io
    var answerindicativoTrapassatoRemotoIo = document.getElementById('answerindicativoTrapassatoRemotoIo').value;
    if (exindicativoTrapassatoRemotoIo == answerindicativoTrapassatoRemotoIo){
        $('.CSSverbsAnswerindicativoTrapassatoRemotoIo').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoTrapassatoRemotoIo').attr('style', 'display: initial; color: red;');
    };

    //tu
    var answerindicativoTrapassatoRemotoTu = document.getElementById('answerindicativoTrapassatoRemotoTu').value;
    if (exindicativoTrapassatoRemotoTu == answerindicativoTrapassatoRemotoTu){
        $('.CSSverbsAnswerindicativoTrapassatoRemotoTu').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoTrapassatoRemotoTu').attr('style', 'display: initial; color: red;');
    };

    //lui
    var answerindicativoTrapassatoRemotoLui = document.getElementById('answerindicativoTrapassatoRemotoLui').value;
    if (exindicativoTrapassatoRemotoLui == answerindicativoTrapassatoRemotoLui){
        $('.CSSverbsAnswerindicativoTrapassatoRemotoLui').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoTrapassatoRemotoLui').attr('style', 'display: initial; color: red;');
    };

    //noi
    var answerindicativoTrapassatoRemotoNoi = document.getElementById('answerindicativoTrapassatoRemotoNoi').value;
    if (exindicativoTrapassatoRemotoNoi == answerindicativoTrapassatoRemotoNoi){
        $('.CSSverbsAnswerindicativoTrapassatoRemotoNoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoTrapassatoRemotoNoi').attr('style', 'display: initial; color: red;');
    };

    //voi
    var answerindicativoTrapassatoRemotoVoi = document.getElementById('answerindicativoTrapassatoRemotoVoi').value;
    if (exindicativoTrapassatoRemotoVoi == answerindicativoTrapassatoRemotoVoi){
        $('.CSSverbsAnswerindicativoTrapassatoRemotoVoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoTrapassatoRemotoVoi').attr('style', 'display: initial; color: red;');
    };

    //loro
    var answerindicativoTrapassatoRemotoLoro = document.getElementById('answerindicativoTrapassatoRemotoLoro').value;
    if (exindicativoTrapassatoRemotoLoro == answerindicativoTrapassatoRemotoLoro){
        $('.CSSverbsAnswerindicativoTrapassatoRemotoLoro').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoTrapassatoRemotoLoro').attr('style', 'display: initial; color: red;');
    };
  };

// Cleaning the form
$(document).on('click', "#ricominciaindicativoTrapassatoRemoto", function () {
    cleanindicativoTrapassatoRemoto();
});
function cleanindicativoTrapassatoRemoto() {
    $('.CSSverbsAnswerindicativoTrapassatoRemotoIo').attr('style', 'display: none;');
    $('.CSSverbsAnswerindicativoTrapassatoRemotoTu').attr('style', 'display: none;');
    $('.CSSverbsAnswerindicativoTrapassatoRemotoLui').attr('style', 'display: none;');
    $('.CSSverbsAnswerindicativoTrapassatoRemotoNoi').attr('style', 'display: none;');
    $('.CSSverbsAnswerindicativoTrapassatoRemotoVoi').attr('style', 'display: none;');
    $('.CSSverbsAnswerindicativoTrapassatoRemotoLoro').attr('style', 'display: none;');

    document.getElementById('formindicativoTrapassatoRemoto').reset();
};