$(document).on('click', "#answercongiuntivoImperfetto", function () {
    runcongiuntivoImperfetto();
});
function runcongiuntivoImperfetto() {

    var excongiuntivoImperfettoIo = document.getElementById('excongiuntivoImperfettoIo').value;
    var excongiuntivoImperfettoTu = document.getElementById('excongiuntivoImperfettoTu').value;
    var excongiuntivoImperfettoLui = document.getElementById('excongiuntivoImperfettoLui').value;
    var excongiuntivoImperfettoNoi = document.getElementById('excongiuntivoImperfettoNoi').value;
    var excongiuntivoImperfettoVoi = document.getElementById('excongiuntivoImperfettoVoi').value;
    var excongiuntivoImperfettoLoro = document.getElementById('excongiuntivoImperfettoLoro').value;

    //io
    var answercongiuntivoImperfettoIo = document.getElementById('answercongiuntivoImperfettoIo').value;
    if (excongiuntivoImperfettoIo == answercongiuntivoImperfettoIo){
        $('.CSSverbsAnswercongiuntivoImperfettoIo').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswercongiuntivoImperfettoIo').attr('style', 'display: initial; color: red;');
    };

    //tu
    var answercongiuntivoImperfettoTu = document.getElementById('answercongiuntivoImperfettoTu').value;
    if (excongiuntivoImperfettoTu == answercongiuntivoImperfettoTu){
        $('.CSSverbsAnswercongiuntivoImperfettoTu').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswercongiuntivoImperfettoTu').attr('style', 'display: initial; color: red;');
    };

    //lui
    var answercongiuntivoImperfettoLui = document.getElementById('answercongiuntivoImperfettoLui').value;
    if (excongiuntivoImperfettoLui == answercongiuntivoImperfettoLui){
        $('.CSSverbsAnswercongiuntivoImperfettoLui').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswercongiuntivoImperfettoLui').attr('style', 'display: initial; color: red;');
    };

    //noi
    var answercongiuntivoImperfettoNoi = document.getElementById('answercongiuntivoImperfettoNoi').value;
    if (excongiuntivoImperfettoNoi == answercongiuntivoImperfettoNoi){
        $('.CSSverbsAnswercongiuntivoImperfettoNoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswercongiuntivoImperfettoNoi').attr('style', 'display: initial; color: red;');
    };

    //voi
    var answercongiuntivoImperfettoVoi = document.getElementById('answercongiuntivoImperfettoVoi').value;
    if (excongiuntivoImperfettoVoi == answercongiuntivoImperfettoVoi){
        $('.CSSverbsAnswercongiuntivoImperfettoVoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswercongiuntivoImperfettoVoi').attr('style', 'display: initial; color: red;');
    };

    //loro
    var answercongiuntivoImperfettoLoro = document.getElementById('answercongiuntivoImperfettoLoro').value;
    if (excongiuntivoImperfettoLoro == answercongiuntivoImperfettoLoro){
        $('.CSSverbsAnswercongiuntivoImperfettoLoro').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswercongiuntivoImperfettoLoro').attr('style', 'display: initial; color: red;');
    };
  };

// Cleaning the form
$(document).on('click', "#ricominciacongiuntivoImperfetto", function () {
    cleancongiuntivoImperfetto();
});
function cleancongiuntivoImperfetto() {
    $('.CSSverbsAnswercongiuntivoImperfettoIo').attr('style', 'display: none;');
    $('.CSSverbsAnswercongiuntivoImperfettoTu').attr('style', 'display: none;');
    $('.CSSverbsAnswercongiuntivoImperfettoLui').attr('style', 'display: none;');
    $('.CSSverbsAnswercongiuntivoImperfettoNoi').attr('style', 'display: none;');
    $('.CSSverbsAnswercongiuntivoImperfettoVoi').attr('style', 'display: none;');
    $('.CSSverbsAnswercongiuntivoImperfettoLoro').attr('style', 'display: none;');

    document.getElementById('formcongiuntivoImperfetto').reset();
};
