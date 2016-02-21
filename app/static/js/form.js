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
	        '<div class="provider-result">'+current_provider.provider_name+'</div>';
	        // var content =
	       	//     '<div class="provider-result">
	        //         <b class="provider-name">' + current_provider.provider_name + '</b>
	        //         <ul class="provider-details">
	        //             <li><span aria-label="Address" class="glyphicon glyphicon-search"></span>' +
	        //                 current_provider.address1 + " "
	        //                 current_provider.address2 + " " current_provider.city + " " current_provider.state + ", USA"'</li>
	        //             <li><span aria-label="Website" class="glyphicon glyphicon-globe"></span>' + current_provider.website + '</li>
	        //             <li><span aria-label="Phone" class="glyphicon glyphicon-earphone"></span> <i>' + current_provider.phone + '</i></li>
	        //         </ul>
	        //     </div>';
	        L.marker([lat, lng], 
	        	{title: current_provider.provider_name,
	        	opacity: 1.0}).addTo(detail.map)
	        .bindPopup(L.popup().setContent(content));
        }
	    }, false);
});

