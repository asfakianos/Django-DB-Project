		
$(document).ready(function(){
	$(document.getElementById('review_form')).submit(function(event){
		    event.preventDefault();
		    
		    submit_review();
		});
});



function submit_review() {
	$('#results').removeClass();
	let getUrl = window.location;
	let baseUrl = getUrl .protocol + "//" + getUrl.host;
	$.ajax({
		url : baseUrl + "/submit_review/",
		type : "POST",
		data : { 
				review : $('#review_text').val(),
				course : window.location.pathname.replace("/course/", ""),
				},

		success : function(json) {
			$('#review_text').val('');
			$('#results').html("Success! Form submitted.");
			$('#results').addClass("alert alert-success");
			$('#results').show();
		},

        error : function(xhr,errmsg,err) {
            $('#results').html("Something went wrong!");
            $('#results').addClass("alert alert-danger");
            $('#results').show();
            console.log(xhr.status + ": " + xhr.responseText);
		}
	});
};