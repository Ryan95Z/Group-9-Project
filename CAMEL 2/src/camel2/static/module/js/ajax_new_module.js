$(document).ready( function(){
	$("#form_submit").click( function(){
		event.preventDefault();
		new_module_request();

	});
});

function new_module_request(){
	$.ajax({
        url : "/module/NewModule/", //endpoint
        type : "POST", // http method
        data : { 
        	module_code : $('#id_code option:selected').text(),
        	module_year : $('#id_year option:selected').text(),
        	module_title : $('#id_title').val(),
        }, // data sent with the post request
        
        //get the csrf_token
        beforeSend: function(xhr, settings) {
        	//console.log("Before Send");
        	$.ajaxSettings.beforeSend(xhr, settings);
    	},

        // handle a successful response
        success : function(json) {
        	module_title : $('#id_title').val(""),
            console.log(json); // log the returned json to the console
            // console.log("success");
            if(json.key_exists){
                alert(json.key_exists + " is already a module");
            }else{
            	show_new_module(json);
            }

        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log(xhr);
        }
    });
}

function show_new_module(json){
	// adding module to table
	$('#module_table').append(
		"<tr>" + 
			"<th>" + json.module_code + "</th>" + 
			"<th>" + json.module_year + "</th>" + 
			"<th>" + json.module_title + "</th>" + 
		"</tr>"
		);
}