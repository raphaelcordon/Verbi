$(document).on('click', "#answerfuturoAnteriore", function () {
    runfuturoAnteriore();
});
function runfuturoAnteriore() {

    var exfuturoAnterioreIo = document.getElementById('exfuturoAnterioreIo').value;
    var exfuturoAnterioreTu = document.getElementById('exfuturoAnterioreTu').value;
    var exfuturoAnterioreLui = document.getElementById('exfuturoAnterioreLui').value;
    var exfuturoAnterioreNoi = document.getElementById('exfuturoAnterioreNoi').value;
    var exfuturoAnterioreVoi = document.getElementById('exfuturoAnterioreVoi').value;
    var exfuturoAnterioreLoro = document.getElementById('exfuturoAnterioreLoro').value;

    //io
    var answerfuturoAnterioreIo = document.getElementById('answerfuturoAnterioreIo').value;
    if (exfuturoAnterioreIo == answerfuturoAnterioreIo){
        $('.CSSverbsAnswerfuturoAnterioreIo').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerfuturoAnterioreIo').attr('style', 'display: initial; color: red;');
    };

    //tu
    var answerfuturoAnterioreTu = document.getElementById('answerfuturoAnterioreTu').value;
    if (exfuturoAnterioreTu == answerfuturoAnterioreTu){
        $('.CSSverbsAnswerfuturoAnterioreTu').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerfuturoAnterioreTu').attr('style', 'display: initial; color: red;');
    };

    //lui
    var answerfuturoAnterioreLui = document.getElementById('answerfuturoAnterioreLui').value;
    if (exfuturoAnterioreLui == answerfuturoAnterioreLui){
        $('.CSSverbsAnswerfuturoAnterioreLui').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerfuturoAnterioreLui').attr('style', 'display: initial; color: red;');
    };

    //noi
    var answerfuturoAnterioreNoi = document.getElementById('answerfuturoAnterioreNoi').value;
    if (exfuturoAnterioreNoi == answerfuturoAnterioreNoi){
        $('.CSSverbsAnswerfuturoAnterioreNoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerfuturoAnterioreNoi').attr('style', 'display: initial; color: red;');
    };

    //voi
    var answerfuturoAnterioreVoi = document.getElementById('answerfuturoAnterioreVoi').value;
    if (exfuturoAnterioreVoi == answerfuturoAnterioreVoi){
        $('.CSSverbsAnswerfuturoAnterioreVoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerfuturoAnterioreVoi').attr('style', 'display: initial; color: red;');
    };

    //loro
    var answerfuturoAnterioreLoro = document.getElementById('answerfuturoAnterioreLoro').value;
    if (exfuturoAnterioreLoro == answerfuturoAnterioreLoro){
        $('.CSSverbsAnswerfuturoAnterioreLoro').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerfuturoAnterioreLoro').attr('style', 'display: initial; color: red;');
    };
  };

// Cleaning the form
$(document).on('click', "#ricominciafuturoAnteriore", function () {
    $('.CSSverbsAnswerfuturoAnterioreIo').attr('style', 'display: none;');
    $('.CSSverbsAnswerfuturoAnterioreTu').attr('style', 'display: none;');
    $('.CSSverbsAnswerfuturoAnterioreLui').attr('style', 'display: none;');
    $('.CSSverbsAnswerfuturoAnterioreNoi').attr('style', 'display: none;');
    $('.CSSverbsAnswerfuturoAnterioreVoi').attr('style', 'display: none;');
    $('.CSSverbsAnswerfuturoAnterioreLoro').attr('style', 'display: none;');

    document.getElementById('formfuturoAnteriore').reset();
});