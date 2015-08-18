$(function () {

	$('.hello').text("");
	$('#center-circle').on('click', explode);

	function explode() {
		$('.circle#1').show();
		$('.circle#2').show();
		$('.circle#3').show();
		$('.circle#4').show();
		$('.circle#1').animate({height:"25%", width:"13%", left:"33%"}, 500);
		$('.circle#2').animate({height:"25%", width:"13%", top:"25%"}, 500);
		$('.circle#3').animate({height:"25%", width:"13%", left:"67%"}, 500);
		$('.circle#4').animate({height:"25%", width:"13%", top:"75%"}, 500);
		$('#center-circle').hide(500);
	}
});