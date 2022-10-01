$(document).on('click', "#answercondizionalePassato", function () {
    runcondizionalePassato();
});
function runcondizionalePassato() {

    var excondizionalePassatoIo = document.getElementById('excondizionalePassatoIo').value;
    var excondizionalePassatoTu = document.getElementById('excondizionalePassatoTu').value;
    var excondizionalePassatoLui = document.getElementById('excondizionalePassatoLui').value;
    var excondizionalePassatoNoi = document.getElementById('excondizionalePassatoNoi').value;
    var excondizionalePassatoVoi = document.getElementById('excondizionalePassatoVoi').value;
    var excondizionalePassatoLoro = document.getElementById('excondizionalePassatoLoro').value;

    //io
    var answercondizionalePassatoIo = document.getElementById('answercondizionalePassatoIo').value;
    if (excondizionalePassatoIo == answercondizionalePassatoIo){
        $('.CSSverbsAnswercondizionalePassatoIo').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswercondizionalePassatoIo').attr('style', 'display: initial; color: red;');
    };

    //tu
    var answercondizionalePassatoTu = document.getElementById('answercondizionalePassatoTu').value;
    if (excondizionalePassatoTu == answercondizionalePassatoTu){
        $('.CSSverbsAnswercondizionalePassatoTu').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswercondizionalePassatoTu').attr('style', 'display: initial; color: red;');
    };

    //lui
    var answercondizionalePassatoLui = document.getElementById('answercondizionalePassatoLui').value;
    if (excondizionalePassatoLui == answercondizionalePassatoLui){
        $('.CSSverbsAnswercondizionalePassatoLui').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswercondizionalePassatoLui').attr('style', 'display: initial; color: red;');
    };

    //noi
    var answercondizionalePassatoNoi = document.getElementById('answercondizionalePassatoNoi').value;
    if (excondizionalePassatoNoi == answercondizionalePassatoNoi){
        $('.CSSverbsAnswercondizionalePassatoNoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswercondizionalePassatoNoi').attr('style', 'display: initial; color: red;');
    };

    //voi
    var answercondizionalePassatoVoi = document.getElementById('answercondizionalePassatoVoi').value;
    if (excondizionalePassatoVoi == answercondizionalePassatoVoi){
        $('.CSSverbsAnswercondizionalePassatoVoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswercondizionalePassatoVoi').attr('style', 'display: initial; color: red;');
    };

    //loro
    var answercondizionalePassatoLoro = document.getElementById('answercondizionalePassatoLoro').value;
    if (excondizionalePassatoLoro == answercondizionalePassatoLoro){
        $('.CSSverbsAnswercondizionalePassatoLoro').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswercondizionalePassatoLoro').attr('style', 'display: initial; color: red;');
    };
  };

// Cleaning the form
$(document).on('click', "#ricominciacondizionalePassato", function () {
    cleancondizionalePassato();
});
function cleancondizionalePassato() {
    $('.CSSverbsAnswercondizionalePassatoIo').attr('style', 'display: none;');
    $('.CSSverbsAnswercondizionalePassatoTu').attr('style', 'display: none;');
    $('.CSSverbsAnswercondizionalePassatoLui').attr('style', 'display: none;');
    $('.CSSverbsAnswercondizionalePassatoNoi').attr('style', 'display: none;');
    $('.CSSverbsAnswercondizionalePassatoVoi').attr('style', 'display: none;');
    $('.CSSverbsAnswercondizionalePassatoLoro').attr('style', 'display: none;');

    document.getElementById('formcondizionalePassato').reset();
};