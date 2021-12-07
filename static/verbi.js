/* :: 1.0 Import All Verb JSs */
function include(file) {
  var script  = document.createElement('script');
  script.src  = file;
  script.type = 'text/javascript';
  script.defer = true;

  document.getElementsByTagName('head').item(0).appendChild(script);

}
/* Include JS Verbs INDICATIVO */
include('/static/js/indicativo/presente.js');
include('/static/js/indicativo/passatoProssimo.js');
include('/static/js/indicativo/imperfetto.js');
include('/static/js/indicativo/trapassatoProssimo.js');
include('/static/js/indicativo/passatoRemoto.js');
include('/static/js/indicativo/trapassatoRemoto.js');
include('/static/js/indicativo/futuroSemplice.js');
include('/static/js/indicativo/futuroAnteriore.js');

/* Include JS Verbs CONGIUNTIVO */
include('/static/js/congiuntivo/presente.js');
include('/static/js/congiuntivo/passato.js');
include('/static/js/congiuntivo/imperfetto.js');
include('/static/js/congiuntivo/trapassato.js');

/* Include JS Verbs CONDIZIONALE
include('/static/js/condizionale/presente.js');
include('/static/js/condizionale/passato.js');*/

/* Include JS Verbs IMPERATIVO */
include('/static/js/imperativo/presente.js');

/* Include JS Verbs INFINITIVO */
include('/static/js/infinitivo/presente.js');
include('/static/js/infinitivo/passato.js');

/* Include JS Verbs PARTICIPIO */
include('/static/js/participio/presente.js');
include('/static/js/participio/passato.js');

/* Include JS Verbs GERUNDIO */
include('/static/js/gerundio/presente.js');
include('/static/js/gerundio/passato.js');