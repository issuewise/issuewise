// Fade #navbutton in and out of visibility using jQuery.

$(document).ready(function() {
	// var timeoutId = null;
	$('body').mousemove(function() {
		// clearTimeout(timeoutId);
		$("#navbutton").fadeIn("slow");
		// timeoutId = setTimeout('$("#navbutton").fadeOut(2000);', 2000);
	}).mouseleave(function() {
		// clearTimeout(timeoutId);
		$("#navbutton").fadeOut("fast");
	});
});
