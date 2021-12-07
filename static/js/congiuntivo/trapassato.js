$(document).on('click', "#answercongiuntivoTrapassato", function () {
    runcongiuntivoTrapassato();
});
function runcongiuntivoTrapassato() {

    var excongiuntivoTrapassatoIo = document.getElementById('excongiuntivoTrapassatoIo').value;
    var excongiuntivoTrapassatoTu = document.getElementById('excongiuntivoTrapassatoTu').value;
    var excongiuntivoTrapassatoLui = document.getElementById('excongiuntivoTrapassatoLui').value;
    var excongiuntivoTrapassatoNoi = document.getElementById('excongiuntivoTrapassatoNoi').value;
    var excongiuntivoTrapassatoVoi = document.getElementById('excongiuntivoTrapassatoVoi').value;
    var excongiuntivoTrapassatoLoro = document.getElementById('excongiuntivoTrapassatoLoro').value;

    //io
    var answercongiuntivoTrapassatoIo = document.getElementById('answercongiuntivoTrapassatoIo').value;
    if (excongiuntivoTrapassatoIo == answercongiuntivoTrapassatoIo){
        $('.CSSverbsAnswercongiuntivoTrapassatoIo').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswercongiuntivoTrapassatoIo').attr('style', 'display: initial; color: red;');
    };

    //tu
    var answercongiuntivoTrapassatoTu = document.getElementById('answercongiuntivoTrapassatoTu').value;
    if (excongiuntivoTrapassatoTu == answercongiuntivoTrapassatoTu){
        $('.CSSverbsAnswercongiuntivoTrapassatoTu').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswercongiuntivoTrapassatoTu').attr('style', 'display: initial; color: red;');
    };

    //lui
    var answercongiuntivoTrapassatoLui = document.getElementById('answercongiuntivoTrapassatoLui').value;
    if (excongiuntivoTrapassatoLui == answercongiuntivoTrapassatoLui){
        $('.CSSverbsAnswercongiuntivoTrapassatoLui').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswercongiuntivoTrapassatoLui').attr('style', 'display: initial; color: red;');
    };

    //noi
    var answercongiuntivoTrapassatoNoi = document.getElementById('answercongiuntivoTrapassatoNoi').value;
    if (excongiuntivoTrapassatoNoi == answercongiuntivoTrapassatoNoi){
        $('.CSSverbsAnswercongiuntivoTrapassatoNoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswercongiuntivoTrapassatoNoi').attr('style', 'display: initial; color: red;');
    };

    //voi
    var answercongiuntivoTrapassatoVoi = document.getElementById('answercongiuntivoTrapassatoVoi').value;
    if (excongiuntivoTrapassatoVoi == answercongiuntivoTrapassatoVoi){
        $('.CSSverbsAnswercongiuntivoTrapassatoVoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswercongiuntivoTrapassatoVoi').attr('style', 'display: initial; color: red;');
    };

    //loro
    var answercongiuntivoTrapassatoLoro = document.getElementById('answercongiuntivoTrapassatoLoro').value;
    if (excongiuntivoTrapassatoLoro == answercongiuntivoTrapassatoLoro){
        $('.CSSverbsAnswercongiuntivoTrapassatoLoro').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswercongiuntivoTrapassatoLoro').attr('style', 'display: initial; color: red;');
    };
  };

// Cleaning the form
$(document).on('click', "#ricominciacongiuntivoTrapassato", function () {
    cleancongiuntivoTrapassato();
});
function cleancongiuntivoTrapassato() {
    $('.CSSverbsAnswercongiuntivoTrapassatoIo').attr('style', 'display: none;');
    $('.CSSverbsAnswercongiuntivoTrapassatoTu').attr('style', 'display: none;');
    $('.CSSverbsAnswercongiuntivoTrapassatoLui').attr('style', 'display: none;');
    $('.CSSverbsAnswercongiuntivoTrapassatoNoi').attr('style', 'display: none;');
    $('.CSSverbsAnswercongiuntivoTrapassatoVoi').attr('style', 'display: none;');
    $('.CSSverbsAnswercongiuntivoTrapassatoLoro').attr('style', 'display: none;');

    document.getElementById('formcongiuntivoTrapassato').reset();
};