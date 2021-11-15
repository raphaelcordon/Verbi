$(document).on('click', "#answerfuturoSemplice", function () {
    runfuturoSemplice();
});
function runfuturoSemplice() {

    var exfuturoSempliceIo = document.getElementById('exfuturoSempliceIo').value;
    var exfuturoSempliceTu = document.getElementById('exfuturoSempliceTu').value;
    var exfuturoSempliceLui = document.getElementById('exfuturoSempliceLui').value;
    var exfuturoSempliceNoi = document.getElementById('exfuturoSempliceNoi').value;
    var exfuturoSempliceVoi = document.getElementById('exfuturoSempliceVoi').value;
    var exfuturoSempliceLoro = document.getElementById('exfuturoSempliceLoro').value;

    //io
    var answerfuturoSempliceIo = document.getElementById('answerfuturoSempliceIo').value;
    if (exfuturoSempliceIo == answerfuturoSempliceIo){
        $('.CSSverbsAnswerfuturoSempliceIo').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerfuturoSempliceIo').attr('style', 'display: initial; color: red;');
    };

    //tu
    var answerfuturoSempliceTu = document.getElementById('answerfuturoSempliceTu').value;
    if (exfuturoSempliceTu == answerfuturoSempliceTu){
        $('.CSSverbsAnswerfuturoSempliceTu').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerfuturoSempliceTu').attr('style', 'display: initial; color: red;');
    };

    //lui
    var answerfuturoSempliceLui = document.getElementById('answerfuturoSempliceLui').value;
    if (exfuturoSempliceLui == answerfuturoSempliceLui){
        $('.CSSverbsAnswerfuturoSempliceLui').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerfuturoSempliceLui').attr('style', 'display: initial; color: red;');
    };

    //noi
    var answerfuturoSempliceNoi = document.getElementById('answerfuturoSempliceNoi').value;
    if (exfuturoSempliceNoi == answerfuturoSempliceNoi){
        $('.CSSverbsAnswerfuturoSempliceNoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerfuturoSempliceNoi').attr('style', 'display: initial; color: red;');
    };

    //voi
    var answerfuturoSempliceVoi = document.getElementById('answerfuturoSempliceVoi').value;
    if (exfuturoSempliceVoi == answerfuturoSempliceVoi){
        $('.CSSverbsAnswerfuturoSempliceVoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerfuturoSempliceVoi').attr('style', 'display: initial; color: red;');
    };

    //loro
    var answerfuturoSempliceLoro = document.getElementById('answerfuturoSempliceLoro').value;
    if (exfuturoSempliceLoro == answerfuturoSempliceLoro){
        $('.CSSverbsAnswerfuturoSempliceLoro').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerfuturoSempliceLoro').attr('style', 'display: initial; color: red;');
    };
  };

// Cleaning the form
$(document).on('click', "#ricominciafuturoSemplice", function () {
    cleanfuturoSemplice();
});
function cleanfuturoSemplice() {
    $('.CSSverbsAnswerfuturoSempliceIo').attr('style', 'display: none;');
    $('.CSSverbsAnswerfuturoSempliceTu').attr('style', 'display: none;');
    $('.CSSverbsAnswerfuturoSempliceLui').attr('style', 'display: none;');
    $('.CSSverbsAnswerfuturoSempliceNoi').attr('style', 'display: none;');
    $('.CSSverbsAnswerfuturoSempliceVoi').attr('style', 'display: none;');
    $('.CSSverbsAnswerfuturoSempliceLoro').attr('style', 'display: none;');

    document.getElementById('formfuturoSemplice').reset();
};