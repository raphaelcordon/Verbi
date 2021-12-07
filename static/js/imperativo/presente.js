$(document).on('click', "#answerimperativoPresente", function () {
    runimperativoPresente();
});
function runimperativoPresente() {

    var eximperativoPresenteTu = document.getElementById('eximperativoPresenteTu').value;
    var eximperativoPresenteLui = document.getElementById('eximperativoPresenteLui').value;
    var eximperativoPresenteNoi = document.getElementById('eximperativoPresenteNoi').value;
    var eximperativoPresenteVoi = document.getElementById('eximperativoPresenteVoi').value;
    var eximperativoPresenteLoro = document.getElementById('eximperativoPresenteLoro').value;

    //tu
    var answerimperativoPresenteTu = document.getElementById('answerimperativoPresenteTu').value;
    if (eximperativoPresenteTu == answerimperativoPresenteTu){
        $('.CSSverbsAnswerimperativoPresenteTu').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerimperativoPresenteTu').attr('style', 'display: initial; color: red;');
    };

    //lui
    var answerimperativoPresenteLui = document.getElementById('answerimperativoPresenteLui').value;
    if (eximperativoPresenteLui == answerimperativoPresenteLui){
        $('.CSSverbsAnswerimperativoPresenteLui').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerimperativoPresenteLui').attr('style', 'display: initial; color: red;');
    };

    //noi
    var answerimperativoPresenteNoi = document.getElementById('answerimperativoPresenteNoi').value;
    if (eximperativoPresenteNoi == answerimperativoPresenteNoi){
        $('.CSSverbsAnswerimperativoPresenteNoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerimperativoPresenteNoi').attr('style', 'display: initial; color: red;');
    };

    //voi
    var answerimperativoPresenteVoi = document.getElementById('answerimperativoPresenteVoi').value;
    if (eximperativoPresenteVoi == answerimperativoPresenteVoi){
        $('.CSSverbsAnswerimperativoPresenteVoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerimperativoPresenteVoi').attr('style', 'display: initial; color: red;');
    };

    //loro
    var answerimperativoPresenteLoro = document.getElementById('answerimperativoPresenteLoro').value;
    if (eximperativoPresenteLoro == answerimperativoPresenteLoro){
        $('.CSSverbsAnswerimperativoPresenteLoro').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerimperativoPresenteLoro').attr('style', 'display: initial; color: red;');
    };
  };

// Cleaning the form
$(document).on('click', "#ricominciaimperativoPresente", function () {
    cleanimperativoPresente();
});
function cleanimperativoPresente() {
    $('.CSSverbsAnswerimperativoPresenteTu').attr('style', 'display: none;');
    $('.CSSverbsAnswerimperativoPresenteLui').attr('style', 'display: none;');
    $('.CSSverbsAnswerimperativoPresenteNoi').attr('style', 'display: none;');
    $('.CSSverbsAnswerimperativoPresenteVoi').attr('style', 'display: none;');
    $('.CSSverbsAnswerimperativoPresenteLoro').attr('style', 'display: none;');

    document.getElementById('formimperativoPresente').reset();
};
