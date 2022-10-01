$(document).on('click', "#answercongiuntivoPassato", function () {
    runcongiuntivoPassato();
});
function runcongiuntivoPassato() {

    var excongiuntivoPassatoIo = document.getElementById('excongiuntivoPassatoIo').value;
    var excongiuntivoPassatoTu = document.getElementById('excongiuntivoPassatoTu').value;
    var excongiuntivoPassatoLui = document.getElementById('excongiuntivoPassatoLui').value;
    var excongiuntivoPassatoNoi = document.getElementById('excongiuntivoPassatoNoi').value;
    var excongiuntivoPassatoVoi = document.getElementById('excongiuntivoPassatoVoi').value;
    var excongiuntivoPassatoLoro = document.getElementById('excongiuntivoPassatoLoro').value;

    //io
    var answercongiuntivoPassatoIo = document.getElementById('answercongiuntivoPassatoIo').value;
    if (excongiuntivoPassatoIo == answercongiuntivoPassatoIo){
        $('.CSSverbsAnswercongiuntivoPassatoIo').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswercongiuntivoPassatoIo').attr('style', 'display: initial; color: red;');
    };

    //tu
    var answercongiuntivoPassatoTu = document.getElementById('answercongiuntivoPassatoTu').value;
    if (excongiuntivoPassatoTu == answercongiuntivoPassatoTu){
        $('.CSSverbsAnswercongiuntivoPassatoTu').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswercongiuntivoPassatoTu').attr('style', 'display: initial; color: red;');
    };

    //lui
    var answercongiuntivoPassatoLui = document.getElementById('answercongiuntivoPassatoLui').value;
    if (excongiuntivoPassatoLui == answercongiuntivoPassatoLui){
        $('.CSSverbsAnswercongiuntivoPassatoLui').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswercongiuntivoPassatoLui').attr('style', 'display: initial; color: red;');
    };

    //noi
    var answercongiuntivoPassatoNoi = document.getElementById('answercongiuntivoPassatoNoi').value;
    if (excongiuntivoPassatoNoi == answercongiuntivoPassatoNoi){
        $('.CSSverbsAnswercongiuntivoPassatoNoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswercongiuntivoPassatoNoi').attr('style', 'display: initial; color: red;');
    };

    //voi
    var answercongiuntivoPassatoVoi = document.getElementById('answercongiuntivoPassatoVoi').value;
    if (excongiuntivoPassatoVoi == answercongiuntivoPassatoVoi){
        $('.CSSverbsAnswercongiuntivoPassatoVoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswercongiuntivoPassatoVoi').attr('style', 'display: initial; color: red;');
    };

    //loro
    var answercongiuntivoPassatoLoro = document.getElementById('answercongiuntivoPassatoLoro').value;
    if (excongiuntivoPassatoLoro == answercongiuntivoPassatoLoro){
        $('.CSSverbsAnswercongiuntivoPassatoLoro').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswercongiuntivoPassatoLoro').attr('style', 'display: initial; color: red;');
    };
  };

// Cleaning the form
$(document).on('click', "#ricominciacongiuntivoPassato", function () {
    cleancongiuntivoPassato();
});
function cleancongiuntivoPassato() {
    $('.CSSverbsAnswercongiuntivoPassatoIo').attr('style', 'display: none;');
    $('.CSSverbsAnswercongiuntivoPassatoTu').attr('style', 'display: none;');
    $('.CSSverbsAnswercongiuntivoPassatoLui').attr('style', 'display: none;');
    $('.CSSverbsAnswercongiuntivoPassatoNoi').attr('style', 'display: none;');
    $('.CSSverbsAnswercongiuntivoPassatoVoi').attr('style', 'display: none;');
    $('.CSSverbsAnswercongiuntivoPassatoLoro').attr('style', 'display: none;');

    document.getElementById('formcongiuntivoPassato').reset();
};