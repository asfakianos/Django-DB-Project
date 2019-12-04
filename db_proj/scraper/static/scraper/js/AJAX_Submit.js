$(document).ready(function(){
	console.log("READY!");
	console.log(document.getElementById('review_form').className);
});
// Use #fav-form on buttons that are used to add courses to a watch list for Profiles
$('#fav_course').on('submit', function(event){
    event.preventDefault();
    console.log("class watched.");
    add_fav();
});


$('#review_form').on('submit', function(event){
	event.preventDefault();
	console.log("review submitted.");
	$('#results').removeClass();
	$('#results').hide();
	submit_review();
});


function add_fav() {
	console.log("Added a course as a favorite...");
	// console.log($('#review_text').val())
	// https://realpython.com/django-and-ajax-form-submissions/
	// Update main -> Get parent maybe??
	// This will be easier for buttons that are on their unique Couse object page. 
}

function submit_review() {
	console.log("Submitted review")
	$.ajax({
		url : "submit_review/",
		type : "POST",
		data : {review : $('#review_text').val() },

		success : function(json) {
			$('#review_text').val(' ');
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
