
$(document).ready(function(){
	$('#watch_course').on('submit', function(event){
	    event.preventDefault();
	    add_fav();
	});

	$(document.getElementById('fav_course')).submit(function(event){
	    event.preventDefault();
	    submit_review();
	});
});


function add_fav() {
	let getUrl = window.location;
	let baseUrl = getUrl .protocol + "//" + getUrl.host;
	$.ajax({
		url : baseUrl + "/watch_course/",
		type : "POST",
		data : {
			course : window.location.pathname.replace("/course/", ""),
			username : $('#user_id_to_js').val(),
		},

		success : function(json) {
			$('#results').html("You are now watching this course.");
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