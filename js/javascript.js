$(function(){
	$('ul.nav-tabs~article').hide();    //隐藏全部标签内容
	$('#Welcome').show();               //使标签首页内容显示
	$("[data-toggle='tooltip']").tooltip();  //激活提示工具
	$("ul.nav-pills.nav-stacked.affix").width($("#scroll").width());  //使affix导航栏宽度动态变化
});

$('ul.nav-tabs li').click(function(){            //标签页之间内容转换
	$('ul.nav-tabs li').removeClass("active");
	$(this).addClass("active");
	$('ul.nav-tabs li a').css("color","gray");
	$('ul.nav-tabs li.active a').css("color","black");
	$('ul.nav-tabs~article').hide();
	var ID = '#' + $(this).attr("name");
	$(ID).show();
});

$('a').focus(function(){        //去掉所有链接获得焦点时的虚线外边框
	$(this).blur();
});

$(window).resize(function(){   //使affix导航栏宽度动态变化
	$("ul.nav-pills.nav-stacked.affix").width($("#scroll").width());
});

$(window).scroll(function(){   //使affix导航栏宽度动态变化
	$("ul.nav-pills.nav-stacked.affix").width($("#scroll").width());
});

