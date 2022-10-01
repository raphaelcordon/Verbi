/* ---------------------------
|  ---------- Apps -----------|
---------------------------- */

// App Resenhando
$("#buttonResenhando").click(function() {
  $("#dataMusicSchool").hide(20);
  $("#dataMovieAPI").hide(20);
  $("#dataResenhando").toggle(400);
});
  
  // App Music School
$("#buttonMusicSchool").click(function() {
  $("#dataResenhando").hide(20);
  $("#dataMovieAPI").hide(20);
  $("#dataMusicSchool").toggle(400);
});
  
  // App Movie API
$("#buttonMovieAPI").click(function() {
  $("#dataResenhando").hide(20);
  $("#dataMusicSchool").hide(20);
  $("#dataMovieAPI").toggle(400);
});