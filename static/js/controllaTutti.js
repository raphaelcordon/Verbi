$(document).on('click', "#ricominciaTutti", function () {

// Cleaning the form
    cleanfuturoAnteriore();
    cleanfuturoSemplice();
    cleanImperfetto();
    cleanpassatoProssimo();
    cleanpassatoRemoto();
    cleanPresente();
    cleantrapassatoProssimo();
    cleantrapassatoRemoto();

});

$(document).on('click', "#controllaTutti", function () {

// Checking the form
    runfuturoAnteriore();
    runfuturoSemplice();
    runImperfetto();
    runpassatoProssimo();
    runpassatoRemoto();
    runPresente();
    runtrapassatoProssimo();
    runtrapassatoRemoto();
});