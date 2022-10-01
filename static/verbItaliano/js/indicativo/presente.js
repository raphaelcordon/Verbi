$(document).on('click', "#answerindicativoPresente", function () {
    runindicativoPresente();
});
function runindicativoPresente() {

    var exindicativoPresenteIo = document.getElementById('exindicativoPresenteIo').value;
    var exindicativoPresenteTu = document.getElementById('exindicativoPresenteTu').value;
    var exindicativoPresenteLui = document.getElementById('exindicativoPresenteLui').value;
    var exindicativoPresenteNoi = document.getElementById('exindicativoPresenteNoi').value;
    var exindicativoPresenteVoi = document.getElementById('exindicativoPresenteVoi').value;
    var exindicativoPresenteLoro = document.getElementById('exindicativoPresenteLoro').value;

    //io
    var answerindicativoPresenteIo = document.getElementById('answerindicativoPresenteIo').value;
    if (exindicativoPresenteIo == answerindicativoPresenteIo){
        $('.CSSverbsAnswerindicativoPresenteIo').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoPresenteIo').attr('style', 'display: initial; color: red;');
    };

    //tu
    var answerindicativoPresenteTu = document.getElementById('answerindicativoPresenteTu').value;
    if (exindicativoPresenteTu == answerindicativoPresenteTu){
        $('.CSSverbsAnswerindicativoPresenteTu').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoPresenteTu').attr('style', 'display: initial; color: red;');
    };

    //lui
    var answerindicativoPresenteLui = document.getElementById('answerindicativoPresenteLui').value;
    if (exindicativoPresenteLui == answerindicativoPresenteLui){
        $('.CSSverbsAnswerindicativoPresenteLui').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoPresenteLui').attr('style', 'display: initial; color: red;');
    };

    //noi
    var answerindicativoPresenteNoi = document.getElementById('answerindicativoPresenteNoi').value;
    if (exindicativoPresenteNoi == answerindicativoPresenteNoi){
        $('.CSSverbsAnswerindicativoPresenteNoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoPresenteNoi').attr('style', 'display: initial; color: red;');
    };

    //voi
    var answerindicativoPresenteVoi = document.getElementById('answerindicativoPresenteVoi').value;
    if (exindicativoPresenteVoi == answerindicativoPresenteVoi){
        $('.CSSverbsAnswerindicativoPresenteVoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoPresenteVoi').attr('style', 'display: initial; color: red;');
    };

    //loro
    var answerindicativoPresenteLoro = document.getElementById('answerindicativoPresenteLoro').value;
    if (exindicativoPresenteLoro == answerindicativoPresenteLoro){
        $('.CSSverbsAnswerindicativoPresenteLoro').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerindicativoPresenteLoro').attr('style', 'display: initial; color: red;');
    };
  };

// Cleaning the form
$(document).on('click', "#ricominciaindicativoPresente", function () {
    cleanindicativoPresente();
});
function cleanindicativoPresente() {
    $('.CSSverbsAnswerindicativoPresenteIo').attr('style', 'display: none;');
    $('.CSSverbsAnswerindicativoPresenteTu').attr('style', 'display: none;');
    $('.CSSverbsAnswerindicativoPresenteLui').attr('style', 'display: none;');
    $('.CSSverbsAnswerindicativoPresenteNoi').attr('style', 'display: none;');
    $('.CSSverbsAnswerindicativoPresenteVoi').attr('style', 'display: none;');
    $('.CSSverbsAnswerindicativoPresenteLoro').attr('style', 'display: none;');

    document.getElementById('formindicativoPresente').reset();
};
