$(document).on('click', "#ricominciaTutti", function () {

// Cleaning the form

    $('.CSSverbsAnswerfuturoAnterioreIo').attr('style', 'display: none;');
    $('.CSSverbsAnswerfuturoAnterioreTu').attr('style', 'display: none;');
    $('.CSSverbsAnswerfuturoAnterioreLui').attr('style', 'display: none;');
    $('.CSSverbsAnswerfuturoAnterioreNoi').attr('style', 'display: none;');
    $('.CSSverbsAnswerfuturoAnterioreVoi').attr('style', 'display: none;');
    $('.CSSverbsAnswerfuturoAnterioreLoro').attr('style', 'display: none;');

    document.getElementById('formfuturoAnteriore').reset();

    $('.CSSverbsAnswerfuturoSempliceIo').attr('style', 'display: none;');
    $('.CSSverbsAnswerfuturoSempliceTu').attr('style', 'display: none;');
    $('.CSSverbsAnswerfuturoSempliceLui').attr('style', 'display: none;');
    $('.CSSverbsAnswerfuturoSempliceNoi').attr('style', 'display: none;');
    $('.CSSverbsAnswerfuturoSempliceVoi').attr('style', 'display: none;');
    $('.CSSverbsAnswerfuturoSempliceLoro').attr('style', 'display: none;');

    document.getElementById('formfuturoSemplice').reset();

    $('.CSSverbsAnswerImperfettoIo').attr('style', 'display: none;');
    $('.CSSverbsAnswerImperfettoTu').attr('style', 'display: none;');
    $('.CSSverbsAnswerImperfettoLui').attr('style', 'display: none;');
    $('.CSSverbsAnswerImperfettoNoi').attr('style', 'display: none;');
    $('.CSSverbsAnswerImperfettoVoi').attr('style', 'display: none;');
    $('.CSSverbsAnswerImperfettoLoro').attr('style', 'display: none;');

    document.getElementById('formImperfetto').reset();

    $('.CSSverbsAnswerpassatoProssimoIo').attr('style', 'display: none;');
    $('.CSSverbsAnswerpassatoProssimoTu').attr('style', 'display: none;');
    $('.CSSverbsAnswerpassatoProssimoLui').attr('style', 'display: none;');
    $('.CSSverbsAnswerpassatoProssimoNoi').attr('style', 'display: none;');
    $('.CSSverbsAnswerpassatoProssimoVoi').attr('style', 'display: none;');
    $('.CSSverbsAnswerpassatoProssimoLoro').attr('style', 'display: none;');

    document.getElementById('formpassatoProssimo').reset();

    $('.CSSverbsAnswerpassatoRemotoIo').attr('style', 'display: none;');
    $('.CSSverbsAnswerpassatoRemotoTu').attr('style', 'display: none;');
    $('.CSSverbsAnswerpassatoRemotoLui').attr('style', 'display: none;');
    $('.CSSverbsAnswerpassatoRemotoNoi').attr('style', 'display: none;');
    $('.CSSverbsAnswerpassatoRemotoVoi').attr('style', 'display: none;');
    $('.CSSverbsAnswerpassatoRemotoLoro').attr('style', 'display: none;');

    document.getElementById('formpassatoRemoto').reset();

    $('.CSSverbsAnswertrapassatoRemotoIo').attr('style', 'display: none;');
    $('.CSSverbsAnswertrapassatoRemotoTu').attr('style', 'display: none;');
    $('.CSSverbsAnswertrapassatoRemotoLui').attr('style', 'display: none;');
    $('.CSSverbsAnswertrapassatoRemotoNoi').attr('style', 'display: none;');
    $('.CSSverbsAnswertrapassatoRemotoVoi').attr('style', 'display: none;');
    $('.CSSverbsAnswertrapassatoRemotoLoro').attr('style', 'display: none;');

    document.getElementById('formtrapassatoRemoto').reset();

    $('.CSSverbsAnswerPresentIo').attr('style', 'display: none;');
    $('.CSSverbsAnswerPresentTu').attr('style', 'display: none;');
    $('.CSSverbsAnswerPresentLui').attr('style', 'display: none;');
    $('.CSSverbsAnswerPresentNoi').attr('style', 'display: none;');
    $('.CSSverbsAnswerPresentVoi').attr('style', 'display: none;');
    $('.CSSverbsAnswerPresentLoro').attr('style', 'display: none;');

    document.getElementById('formPresente').reset();

    $('.CSSverbsAnswertrapassatoProssimoIo').attr('style', 'display: none;');
    $('.CSSverbsAnswertrapassatoProssimoTu').attr('style', 'display: none;');
    $('.CSSverbsAnswertrapassatoProssimoLui').attr('style', 'display: none;');
    $('.CSSverbsAnswertrapassatoProssimoNoi').attr('style', 'display: none;');
    $('.CSSverbsAnswertrapassatoProssimoVoi').attr('style', 'display: none;');
    $('.CSSverbsAnswertrapassatoProssimoLoro').attr('style', 'display: none;');

    document.getElementById('formtrapassatoProssimo').reset();

    $('.CSSverbsAnswertrapassatoRemotoIo').attr('style', 'display: none;');
    $('.CSSverbsAnswertrapassatoRemotoTu').attr('style', 'display: none;');
    $('.CSSverbsAnswertrapassatoRemotoLui').attr('style', 'display: none;');
    $('.CSSverbsAnswertrapassatoRemotoNoi').attr('style', 'display: none;');
    $('.CSSverbsAnswertrapassatoRemotoVoi').attr('style', 'display: none;');
    $('.CSSverbsAnswertrapassatoRemotoLoro').attr('style', 'display: none;');

    document.getElementById('formtrapassatoRemoto').reset();
});


$(document).on('click', "#controllaTutti", function () {

// Checking the form
    runfuturoAnteriore();
    runfuturoSemplice();
    runImperfetto();
    runpassatoProssimo();
    runpassatoRemoto();
    runPresent();
    runtrapassatoProssimo();
    runtrapassatoRemoto();
});