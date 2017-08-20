$(function(){
	$('ul.nav-tabs~article').hide();
	$('#Welcome').show();
	$("[data-toggle='tooltip']").tooltip();
});
$('ul.nav-tabs li').click(function(){
	$('ul.nav-tabs li').removeClass("active");
	$(this).addClass("active");
	$('ul.nav-tabs li a').css("color","gray");
	$('ul.nav-tabs li.active a').css("color","black");
	$('ul.nav-tabs~article').hide();
	var ID = '#' + $(this).attr("name");
	$(ID).show();
});
