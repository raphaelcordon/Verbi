$(document).on('click', "#ricominciaTutti", function () {

// Cleaning the form I N D I C A T I V O
    cleanindicativoFuturoAnteriore();
    cleanindicativoFuturoSemplice();
    cleanindicativoImperfetto();
    cleanindicativoPassatoProssimo();
    cleanindicativoPassatoRemoto();
    cleanindicativoPresente();
    cleanindicativoTrapassatoProssimo();
    cleanindicativoTrapassatoRemoto();

// Cleaning the form C O N G I U N T I V O
    cleancongiuntivoImperfetto();
    cleancongiuntivoPassato();
    cleancongiuntivoPresente();
    cleancongiuntivoTrapassato();

// Cleaning the form C O N D I Z I O N A L E
    cleancondizionalePassato();
    cleancondizionalePresente();

// Cleaning the form I M P E R A T I V O
    cleanimperativoPresente();

// Cleaning the form I N F I N I T I V O
    cleaninfinitivoPassato();
    cleaninfinitivoPresente();


// Cleaning the P A R T I C I P I O
    cleanparticipioPassato();
    cleanparticipioPresente();

// Cleaning the G E R U N D I O
    cleangerundioPassato();
    cleangerundioPresente();

});

$(document).on('click', "#controllaTutti", function () {

// Checking the I N D I C A T I V O
    runindicativoFuturoAnteriore();
    runindicativoFuturoSemplice();
    runindicativoImperfetto();
    runindicativoPassatoProssimo();
    runindicativoPassatoRemoto();
    runindicativoPresente();
    runindicativoTrapassatoProssimo();
    runindicativoTrapassatoRemoto();

// Checking the form C O N G I U N T I V O
    runcongiuntivoImperfetto();
    runcongiuntivoPassato();
    runcongiuntivoPresente();
    runcongiuntivoTrapassato();

// Checking the form C O N D I Z I O N A L E
    runcondizionalePassato();
    runcondizionalePresente();

// Cleaning the form I M P E R A T I V O
    runimperativoPresente();

// Checking the I N F I N I T I V O
    runinfinitivoPassato();
    runinfinitivoPresente();

// Checking the P A R T I C I P I O
    runparticipioPassato();
    runparticipioPresente();

// Checking the G E R U N D I O
    rungerundioPassato();
    rungerundioPresente();
});