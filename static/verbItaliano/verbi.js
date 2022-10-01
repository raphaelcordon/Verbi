/* :: 1.0 Import All Verb JSs */
function include(file) {
  var script  = document.createElement('script');
  script.src  = file;
  script.type = 'text/javascript';
  script.defer = true;

  document.getElementsByTagName('head').item(0).appendChild(script);

}

/* Include JS Verbs ControlaTutti */
include('/static/verbItaliano/js/controllaTutti.js');

/* Include JS Verbs INDICATIVO */
include('/static/verbItaliano/js/indicativo/presente.js');
include('/static/verbItaliano/js/indicativo/passatoProssimo.js');
include('/static/verbItaliano/js/indicativo/imperfetto.js');
include('/static/verbItaliano/js/indicativo/trapassatoProssimo.js');
include('/static/verbItaliano/js/indicativo/passatoRemoto.js');
include('/static/verbItaliano/js/indicativo/trapassatoRemoto.js');
include('/static/verbItaliano/js/indicativo/futuroSemplice.js');
include('/static/verbItaliano/js/indicativo/futuroAnteriore.js');

/* Include JS Verbs CONGIUNTIVO */
include('/static/verbItaliano/js/congiuntivo/presente.js');
include('/static/verbItaliano/js/congiuntivo/passato.js');
include('/static/verbItaliano/js/congiuntivo/imperfetto.js');
include('/static/verbItaliano/js/congiuntivo/trapassato.js');

/* Include JS Verbs CONDIZIONALE */
include('/static/verbItaliano/js/condizionale/presente.js');
include('/static/verbItaliano/js/condizionale/passato.js');

/* Include JS Verbs IMPERATIVO */
include('/static/verbItaliano/js/imperativo/presente.js');

/* Include JS Verbs INFINITIVO */
include('/static/verbItaliano/js/infinitivo/presente.js');
include('/static/verbItaliano/js/infinitivo/passato.js');

/* Include JS Verbs PARTICIPIO */
include('/static/verbItaliano/js/participio/presente.js');
include('/static/verbItaliano/js/participio/passato.js');

/* Include JS Verbs GERUNDIO */
include('/static/verbItaliano/js/gerundio/presente.js');
include('/static/verbItaliano/js/gerundio/passato.js');