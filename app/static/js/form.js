$(function () {
	var questionIndex = 0;
	var prevQuestion = 0;
	var numQuestions = $(".form-group").size();

	provider_objects = $.parseJSON(providers);
	$('.form-group').hide();
	$('.button-holder').hide();
	$('#warning').hide();
	$(".form-group:eq("+questionIndex+")").show();

	$('.next-btn').on('click', function(e) {
		e.preventDefault();
		var $this = $(this);

		prevQuestion = questionIndex;
		if (performChecks() == false) {
			$('#warning').fadeIn();
			return;
		}

		if ($this.data("executing")) return;
		$this.data("executing", true);
		$('.button-holder').hide();
		$(".form-group:eq("+prevQuestion+")").animate({
			opacity: 0,
		}, 300, function() {
			$(".form-group").hide();
			$(".form-group:eq("+prevQuestion+")").hide();
			$('#warning').fadeOut();
			questionIndex++;
			$(".form-group:eq("+questionIndex+")").fadeIn();
			$this.data("executing", false);
		});

		if (questionIndex == numQuestions - 2) {
			$('.next-btn').hide();
			$('.button-holder').show();
		}
	});

	function performChecks() {
		if (questionIndex == 3) {
			if ($('#id_questionChildren_2').is(':checked')) {
				questionIndex += 2;
				return true;
			} else if ($('#id_questionChildren_1').is(':checked')) {
				return true;
			} else {
				return false;
			}
		}
		return true;
	}

	var provider;
	var provider_latlng;
	var provider_lat, provider_lng;
	var distance;
	for (var i = 0; i < provider_objects.length; i++) {
		provider_latlng = provider_objects[i].fields.latlng.split(",");
		provider_lat = parseFloat(provider_latlng[0]);
		provider_lng = parseFloat(provider_latlng[1]);

		distance = getDistanceFromLatLonInKm(provider_lat, provider_lng, ref_loc_lat, ref_loc_lng);

		$('#provider-distance')[i].textContent = "test";
	}

	function getDistanceFromLatLonInKm(lat1,lon1,lat2,lon2) {
		var R = 6371; // Radius of the earth in km
		var dLat = deg2rad(lat2-lat1);  // deg2rad below
		var dLon = deg2rad(lon2-lon1); 
		var a = 
	    	Math.sin(dLat/2) * Math.sin(dLat/2) +
	    	Math.cos(deg2rad(lat1)) * Math.cos(deg2rad(lat2)) * 
	    	Math.sin(dLon/2) * Math.sin(dLon/2); 
		var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a)); 
		var d = R * c; // Distance in km
		return d;
	}

	function deg2rad(deg) {
  		return deg * (Math.PI/180)
	}

	window.addEventListener("map:init", function (e) {
		var lat, lng;
        var detail = e.detail;
        var s;
        var current_provider;

        for (var i = 0; i < provider_objects.length; i++) {

        	current_provider = provider_objects[i].fields;
	        s = current_provider.latlng.split(",");
	        lat = parseFloat(s[0]); 
	        lng = parseFloat(s[1]);
	        var content = 
	        '<b class="provider-name-popup">'+current_provider.provider_name+'</b>'+
	        '<ul class="provider-details provider-details-popup">'+
	        	'<li><span aria-label="Address" class="glyphicon glyphicon-search"></span>'+ " " + 
	        		current_provider.address1 + " " + current_provider.address2 + " " + current_provider.city + " " + current_provider.state + ", USA</li>" +
	        	'<li><span aria-label="Website" class="glyphicon glyphicon-globe"></span>'+" "+current_provider.website+"</li>"+
	        	'<li><span aria-label="Phone" class="glyphicon glyphicon-earphone"></span>'+" "+current_provider.phone+"</li>"+
	        "</ul>";

	        L.marker([lat, lng], 
	        	{title: current_provider.provider_name,
	        	opacity: 1.0}).addTo(detail.map)
	        .bindPopup(L.popup().setContent(content));
        }
	    }, false);
});

