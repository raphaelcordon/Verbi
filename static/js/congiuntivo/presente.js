$(document).on('click', "#answercongiuntivoPresente", function () {
    runcongiuntivoPresente();
});
function runcongiuntivoPresente() {

    var excongiuntivoPresenteIo = document.getElementById('excongiuntivoPresenteIo').value;
    var excongiuntivoPresenteTu = document.getElementById('excongiuntivoPresenteTu').value;
    var excongiuntivoPresenteLui = document.getElementById('excongiuntivoPresenteLui').value;
    var excongiuntivoPresenteNoi = document.getElementById('excongiuntivoPresenteNoi').value;
    var excongiuntivoPresenteVoi = document.getElementById('excongiuntivoPresenteVoi').value;
    var excongiuntivoPresenteLoro = document.getElementById('excongiuntivoPresenteLoro').value;

    //io
    var answercongiuntivoPresenteIo = document.getElementById('answercongiuntivoPresenteIo').value;
    if (excongiuntivoPresenteIo == answercongiuntivoPresenteIo){
        $('.CSSverbsAnswercongiuntivoPresenteIo').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswercongiuntivoPresenteIo').attr('style', 'display: initial; color: red;');
    };

    //tu
    var answercongiuntivoPresenteTu = document.getElementById('answercongiuntivoPresenteTu').value;
    if (excongiuntivoPresenteTu == answercongiuntivoPresenteTu){
        $('.CSSverbsAnswercongiuntivoPresenteTu').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswercongiuntivoPresenteTu').attr('style', 'display: initial; color: red;');
    };

    //lui
    var answercongiuntivoPresenteLui = document.getElementById('answercongiuntivoPresenteLui').value;
    if (excongiuntivoPresenteLui == answercongiuntivoPresenteLui){
        $('.CSSverbsAnswercongiuntivoPresenteLui').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswercongiuntivoPresenteLui').attr('style', 'display: initial; color: red;');
    };

    //noi
    var answercongiuntivoPresenteNoi = document.getElementById('answercongiuntivoPresenteNoi').value;
    if (excongiuntivoPresenteNoi == answercongiuntivoPresenteNoi){
        $('.CSSverbsAnswercongiuntivoPresenteNoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswercongiuntivoPresenteNoi').attr('style', 'display: initial; color: red;');
    };

    //voi
    var answercongiuntivoPresenteVoi = document.getElementById('answercongiuntivoPresenteVoi').value;
    if (excongiuntivoPresenteVoi == answercongiuntivoPresenteVoi){
        $('.CSSverbsAnswercongiuntivoPresenteVoi').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswercongiuntivoPresenteVoi').attr('style', 'display: initial; color: red;');
    };

    //loro
    var answercongiuntivoPresenteLoro = document.getElementById('answercongiuntivoPresenteLoro').value;
    if (excongiuntivoPresenteLoro == answercongiuntivoPresenteLoro){
        $('.CSSverbsAnswercongiuntivoPresenteLoro').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswercongiuntivoPresenteLoro').attr('style', 'display: initial; color: red;');
    };
  };

// Cleaning the form
$(document).on('click', "#ricominciacongiuntivoPresente", function () {
    cleancongiuntivoPresente();
});
function cleancongiuntivoPresente() {
    $('.CSSverbsAnswercongiuntivoPresenteIo').attr('style', 'display: none;');
    $('.CSSverbsAnswercongiuntivoPresenteTu').attr('style', 'display: none;');
    $('.CSSverbsAnswercongiuntivoPresenteLui').attr('style', 'display: none;');
    $('.CSSverbsAnswercongiuntivoPresenteNoi').attr('style', 'display: none;');
    $('.CSSverbsAnswercongiuntivoPresenteVoi').attr('style', 'display: none;');
    $('.CSSverbsAnswercongiuntivoPresenteLoro').attr('style', 'display: none;');

    document.getElementById('formcongiuntivoPresente').reset();
};
