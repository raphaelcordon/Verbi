$(document).on('click', "#answerparticipioPassato", function () {
    runparticipioPassato();
});
function runparticipioPassato() {

    var exparticipioPassato = document.getElementById('exparticipioPassato').value;


    //Participio Passato
    var answerparticipioPassato = document.getElementById('answerparticipioPassatoIo').value;
    if (exparticipioPassato == answerparticipioPassato){
        $('.CSSverbsAnswerparticipioPassato').attr('style', 'display: initial; color: green;');
    }else{
        $('.CSSverbsAnswerparticipioPassato').attr('style', 'display: initial; color: red;');
    };
  };

// Cleaning the form
$(document).on('click', "#ricominciaparticipioPassato", function () {
    cleanparticipioPassato();
});
function cleanparticipioPassato() {
    $('.CSSverbsAnswerparticipioPassato').attr('style', 'display: none;');


    document.getElementById('formparticipioPassato').reset();
};