$(document).ready(function()
{
	var csrftoken = getCookie('csrftoken');
	$('#search').click(function()
	{
		var data_json = {csrfmiddlewaretoken: csrftoken, s_name: $("#s_name").val(), s_age: $("#s_age").val(),"type": "search"};
		$.ajax(
		{
			url: '/ajax',
			type: 'POST',
			dataType: 'json',
			data: data_json,
			success: function(resp_json)
			{
				$("#tdiv").html(resp_json.t);
			},
			error: function(xhr,errmsg,err)
			{
				$("#tdiv").html(xhr.status + ": " + xhr.responseText);
			}
		});
		return false;
	});
	$('#add').click(function()
	{
		var data_json = {csrfmiddlewaretoken: csrftoken, a_name: $("#a_name").val(), a_age: $("#a_age").val(),type: "add"};
		$.ajax(
		{
			url: '/ajax',
			type: 'POST',
			dataType: 'json',
			data: data_json,
			success: function(resp_json)
			{
				$("#tdiv").html(resp_json.t);
			},
			error: function(xhr,errmsg,err)
			{
				$("#tdiv").html(xhr.status + ": " + xhr.responseText);
			}
		});
		return false;
	});
});

function getCookie(name)
{
	var cookieValue = null;
	if (document.cookie && document.cookie != '')
	{
		var cookies = document.cookie.split(';');
		for (var i = 0; i < cookies.length; i++)
		{
			var cookie = jQuery.trim(cookies[i]);
			// Does this cookie string begin with the name we want?
			if (cookie.substring(0, name.length + 1) == (name + '='))
			{
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}