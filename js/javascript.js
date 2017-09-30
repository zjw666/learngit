$(function(){
	$('ul.nav-tabs~article').hide();    //隐藏全部标签内容
	$('#Welcome').show();               //使标签首页内容显示
	$("[data-toggle='tooltip']").tooltip();  //激活提示工具
	$("ul.nav-pills.nav-stacked.affix").width($("#scroll").width());  //使affix导航栏宽度动态变化
	$('#img-container button').hide();  //隐藏头像中的访问主页按钮
	button_change();          //初始化头像按钮大小
});

$('ul.nav-tabs li').click(function(){            //标签页之间内容转换
	$('ul.nav-tabs li').removeClass("active");
	$(this).addClass("active");
	$('ul.nav-tabs li a').css("color","gray");
	$('ul.nav-tabs li.active a').css("color","black");
	var ID = '#' + $(this).attr("name");
	$('ul.nav-tabs~article').hide();
	$(ID).show();
});

$('a').focus(function(){        //去掉所有链接获得焦点时的虚线外边框
	$(this).blur();
});


$(window).scroll(function(){   //使affix导航栏宽度动态变化
	$("ul.nav-pills.nav-stacked.affix").width($("#scroll").width());
});

$(window).resize(function(){   //使遮罩宽度与头像宽度保持一致
	$('#mask').width($('img[alt="photo"]').width());
	button_change();
});

$('#img-container').hover(     //头像按钮淡入淡出以及遮罩透明度变化
	function(){
	$('#mask').css("opacity","0.5");
	$('#img-container button').fadeIn("500");},
	function(){
	$('#img-container button').fadeOut("500");
	$('#mask').css("opacity","0");}
);

function button_change(){    //使头像按钮适应屏幕大小
	var width = $('img[alt="photo"]').width();
	var height = $('img[alt="photo"]').height();
	$('#img-container button').css({
		"width":width*0.55,
		"height":height*0.15,
		"top":height*0.4,
		"left":width*0.2,
		"fontSize":width*0.05,
	});
}

$('#img-container button').click(function(){   //实现老师头像按钮的页面跳转
	var ID=$(this).attr("id");
	if (ID=="li"){
		window.open("http://mypage.zju.edu.cn/cfli");}
	else{
		window.open("http://mypage.zju.edu.cn/0814130");
	}
});



