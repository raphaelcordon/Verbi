$(document).on('click', "#answerindicativoPassatoRemoto", function () {
    runindicativoPassatoRemoto();
});
function runindicativoPassatoRemoto() {

    var exindicativoPassatoRemotoIo = document.getElementById('exindicativoPassatoRemotoIo').value;
    var exindicativoPassatoRemotoTu = document.getElementById('exindicativoPassatoRemotoTu').value;
    var exindicativoPassatoRemotoLui = document.getElementById('exindicativoPassatoRemotoLui').value;
    var exindicativoPassatoRemotoNoi = document.getElementById('exindicativoPassatoRemotoNoi').value;
    var exindicativoPassatoRemotoVoi = document.getElementById('exindicativoPassatoRemotoVoi').value;
    var exindicativoPassatoRemotoLoro = document.getElementById('exindicativoPassatoRemotoLoro').value;

    //io
    var answerindicativoPassatoRemotoIo = document.getElementById('answerindicativoPassatoRemotoIo').value;
    if (exindicativoPassatoRemotoIo == answerindicativoPassatoRemotoIo){
        $('.CSSverbsAnswerindicativoPassatoRemotoIo').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoPassatoRemotoIo').attr('style', 'display: initial; color: red;');
    };

    //tu
    var answerindicativoPassatoRemotoTu = document.getElementById('answerindicativoPassatoRemotoTu').value;
    if (exindicativoPassatoRemotoTu == answerindicativoPassatoRemotoTu){
        $('.CSSverbsAnswerindicativoPassatoRemotoTu').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoPassatoRemotoTu').attr('style', 'display: initial; color: red;');
    };

    //lui
    var answerindicativoPassatoRemotoLui = document.getElementById('answerindicativoPassatoRemotoLui').value;
    if (exindicativoPassatoRemotoLui == answerindicativoPassatoRemotoLui){
        $('.CSSverbsAnswerindicativoPassatoRemotoLui').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoPassatoRemotoLui').attr('style', 'display: initial; color: red;');
    };

    //noi
    var answerindicativoPassatoRemotoNoi = document.getElementById('answerindicativoPassatoRemotoNoi').value;
    if (exindicativoPassatoRemotoNoi == answerindicativoPassatoRemotoNoi){
        $('.CSSverbsAnswerindicativoPassatoRemotoNoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoPassatoRemotoNoi').attr('style', 'display: initial; color: red;');
    };

    //voi
    var answerindicativoPassatoRemotoVoi = document.getElementById('answerindicativoPassatoRemotoVoi').value;
    if (exindicativoPassatoRemotoVoi == answerindicativoPassatoRemotoVoi){
        $('.CSSverbsAnswerindicativoPassatoRemotoVoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoPassatoRemotoVoi').attr('style', 'display: initial; color: red;');
    };

    //loro
    var answerindicativoPassatoRemotoLoro = document.getElementById('answerindicativoPassatoRemotoLoro').value;
    if (exindicativoPassatoRemotoLoro == answerindicativoPassatoRemotoLoro){
        $('.CSSverbsAnswerindicativoPassatoRemotoLoro').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoPassatoRemotoLoro').attr('style', 'display: initial; color: red;');
    };
  };

// Cleaning the form
$(document).on('click', "#ricominciaindicativoPassatoRemoto", function () {
    cleanindicativoPassatoRemoto();
});
function cleanindicativoPassatoRemoto() {
    $('.CSSverbsAnswerindicativoPassatoRemotoIo').attr('style', 'display: none;');
    $('.CSSverbsAnswerindicativoPassatoRemotoTu').attr('style', 'display: none;');
    $('.CSSverbsAnswerindicativoPassatoRemotoLui').attr('style', 'display: none;');
    $('.CSSverbsAnswerindicativoPassatoRemotoNoi').attr('style', 'display: none;');
    $('.CSSverbsAnswerindicativoPassatoRemotoVoi').attr('style', 'display: none;');
    $('.CSSverbsAnswerindicativoPassatoRemotoLoro').attr('style', 'display: none;');

    document.getElementById('formindicativoPassatoRemoto').reset();
};