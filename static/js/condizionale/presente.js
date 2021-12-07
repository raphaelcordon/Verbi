$(document).on('click', "#answercondizionalePresente", function () {
    runcondizionalePresente();
});
function runcondizionalePresente() {

    var excondizionalePresenteIo = document.getElementById('excondizionalePresenteIo').value;
    var excondizionalePresenteTu = document.getElementById('excondizionalePresenteTu').value;
    var excondizionalePresenteLui = document.getElementById('excondizionalePresenteLui').value;
    var excondizionalePresenteNoi = document.getElementById('excondizionalePresenteNoi').value;
    var excondizionalePresenteVoi = document.getElementById('excondizionalePresenteVoi').value;
    var excondizionalePresenteLoro = document.getElementById('excondizionalePresenteLoro').value;

    //io
    var answercondizionalePresenteIo = document.getElementById('answercondizionalePresenteIo').value;
    if (excondizionalePresenteIo == answercondizionalePresenteIo){
        $('.CSSverbsAnswercondizionalePresenteIo').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswercondizionalePresenteIo').attr('style', 'display: initial; color: red;');
    };

    //tu
    var answercondizionalePresenteTu = document.getElementById('answercondizionalePresenteTu').value;
    if (excondizionalePresenteTu == answercondizionalePresenteTu){
        $('.CSSverbsAnswercondizionalePresenteTu').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswercondizionalePresenteTu').attr('style', 'display: initial; color: red;');
    };

    //lui
    var answercondizionalePresenteLui = document.getElementById('answercondizionalePresenteLui').value;
    if (excondizionalePresenteLui == answercondizionalePresenteLui){
        $('.CSSverbsAnswercondizionalePresenteLui').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswercondizionalePresenteLui').attr('style', 'display: initial; color: red;');
    };

    //noi
    var answercondizionalePresenteNoi = document.getElementById('answercondizionalePresenteNoi').value;
    if (excondizionalePresenteNoi == answercondizionalePresenteNoi){
        $('.CSSverbsAnswercondizionalePresenteNoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswercondizionalePresenteNoi').attr('style', 'display: initial; color: red;');
    };

    //voi
    var answercondizionalePresenteVoi = document.getElementById('answercondizionalePresenteVoi').value;
    if (excondizionalePresenteVoi == answercondizionalePresenteVoi){
        $('.CSSverbsAnswercondizionalePresenteVoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswercondizionalePresenteVoi').attr('style', 'display: initial; color: red;');
    };

    //loro
    var answercondizionalePresenteLoro = document.getElementById('answercondizionalePresenteLoro').value;
    if (excondizionalePresenteLoro == answercondizionalePresenteLoro){
        $('.CSSverbsAnswercondizionalePresenteLoro').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswercondizionalePresenteLoro').attr('style', 'display: initial; color: red;');
    };
  };

// Cleaning the form
$(document).on('click', "#ricominciacondizionalePresente", function () {
    cleancondizionalePresente();
});
function cleancondizionalePresente() {
    $('.CSSverbsAnswercondizionalePresenteIo').attr('style', 'display: none;');
    $('.CSSverbsAnswercondizionalePresenteTu').attr('style', 'display: none;');
    $('.CSSverbsAnswercondizionalePresenteLui').attr('style', 'display: none;');
    $('.CSSverbsAnswercondizionalePresenteNoi').attr('style', 'display: none;');
    $('.CSSverbsAnswercondizionalePresenteVoi').attr('style', 'display: none;');
    $('.CSSverbsAnswercondizionalePresenteLoro').attr('style', 'display: none;');

    document.getElementById('formcondizionalePresente').reset();
};
