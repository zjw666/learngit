$(function(){
	$('ul.nav-tabs~article').hide();    //隐藏全部标签内容
	$('#Welcome').show();               //使标签首页内容显示
	$("[data-toggle='tooltip']").tooltip();  //激活提示工具
	$("ul.nav-pills.nav-stacked.affix").width($("#scroll").width());  //使affix导航栏宽度动态变化
	$('#img-container button').hide();  //隐藏头像中的访问主页按钮
	button_change();          //初始化头像按钮大小
	$data=$("#list").clone();  //克隆头像列表，为头像分类动画做准备
	person_object = {
		zjw:"本科毕业于西南石油大学，现硕士研究生在读。爱好乒乓球和羽毛球，喜欢和朋友一起愉快地玩耍。处于人生十字口中一只迷茫的小白，最近由于毕业问题，心里充满了烦恼和忧虑，希望能早点做完项目，顺利发表文章毕业，最终能找到一份自己喜爱的工作。邮箱：591342608@qq.com",
		wmh:"本科毕业于西南石油大学，现硕士研究生在读。爱好乒乓球和羽毛球，喜欢和朋友一起愉快地玩耍。处于人生十字口中一只迷茫的小白，最近由于毕业问题，心里充满了烦恼和忧虑，希望能早点做完项目，顺利发表文章毕业，最终能找到一份自己喜爱的工作。邮箱：2591342608@qq.com",
		gsm:"本科毕业于西南石油大学，现硕士研究生在读。爱好乒乓球和羽毛球，喜欢和朋友一起愉快地玩耍。处于人生十字口中一只迷茫的小白，最近由于毕业问题，心里充满了烦恼和忧虑，希望能早点做完项目，顺利发表文章毕业，最终能找到一份自己喜爱的工作。邮箱：3591342608@qq.com",
		hwa:"本科毕业于西南石油大学，现硕士研究生在读。爱好乒乓球和羽毛球，喜欢和朋友一起愉快地玩耍。处于人生十字口中一只迷茫的小白，最近由于毕业问题，心里充满了烦恼和忧虑，希望能早点做完项目，顺利发表文章毕业，最终能找到一份自己喜爱的工作。邮箱：4591342608@qq.com",
		lxx:"本科毕业于西南石油大学，现硕士研究生在读。爱好乒乓球和羽毛球，喜欢和朋友一起愉快地玩耍。处于人生十字口中一只迷茫的小白，最近由于毕业问题，心里充满了烦恼和忧虑，希望能早点做完项目，顺利发表文章毕业，最终能找到一份自己喜爱的工作。邮箱：5591342608@qq.com",
		zs:"本科毕业于西南石油大学，现硕士研究生在读。爱好乒乓球和羽毛球，喜欢和朋友一起愉快地玩耍。处于人生十字口中一只迷茫的小白，最近由于毕业问题，心里充满了烦恼和忧虑，希望能早点做完项目，顺利发表文章毕业，最终能找到一份自己喜爱的工作。邮箱：6591342608@qq.com",
		wxx:"本科毕业于西南石油大学，现硕士研究生在读。爱好乒乓球和羽毛球，喜欢和朋友一起愉快地玩耍。处于人生十字口中一只迷茫的小白，最近由于毕业问题，心里充满了烦恼和忧虑，希望能早点做完项目，顺利发表文章毕业，最终能找到一份自己喜爱的工作。邮箱：7591342608@qq.com",
		zd:"本科毕业于西南石油大学，现硕士研究生在读。爱好乒乓球和羽毛球，喜欢和朋友一起愉快地玩耍。处于人生十字口中一只迷茫的小白，最近由于毕业问题，心里充满了烦恼和忧虑，希望能早点做完项目，顺利发表文章毕业，最终能找到一份自己喜爱的工作。邮箱：8591342608@qq.com",
		wyl:"本科毕业于西南石油大学，现硕士研究生在读。爱好乒乓球和羽毛球，喜欢和朋友一起愉快地玩耍。处于人生十字口中一只迷茫的小白，最近由于毕业问题，心里充满了烦恼和忧虑，希望能早点做完项目，顺利发表文章毕业，最终能找到一份自己喜爱的工作。邮箱：9591342608@qq.com",
		zht:"本科毕业于西南石油大学，现硕士研究生在读。爱好乒乓球和羽毛球，喜欢和朋友一起愉快地玩耍。处于人生十字口中一只迷茫的小白，最近由于毕业问题，心里充满了烦恼和忧虑，希望能早点做完项目，顺利发表文章毕业，最终能找到一份自己喜爱的工作。邮箱：10591342608@qq.com"
	}
	
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


$('#classification li').click(function(){    //头像分类动画
	$(this).addClass("cur");
	$(this).siblings().removeClass("cur");
	var id=$(this).attr("id");
	if (id=="all") 
	{
		var $destination=$data.find("li");
	}else{
		var $destination=$data.find("li."+id);
	}
	$("#list").quicksand($destination,{
		duration:700
	});
	$("#list a").click(function(event){  //动画完成后需重新捆绑事件
		var img = $(this).children()[0];
		var name = img.alt;
		var url= img.src;
		$("#personal").stop(stopAll=false,goToEnd=true);
		$("#personal").css("opacity","0");
		$("#personal h2").text(name);
		$("#personal img").attr("src",url);
		$("#personal p").text(person_object[name]);
		$("#personal").animate({
			opacity:'1'
		},1000);
		event.preventDefault();
	});
});

$("#list a").click(function(event){  //动画完成后需重新捆绑事件
		var img = $(this).children()[0];
		var name = img.alt;
		var url= img.src;
		$("#personal").stop(stopAll=false,goToEnd=true);
		$("#personal").css("opacity","0");
		$("#personal h2").text(name);
		$("#personal img").attr("src",url);
		$("#personal p").text(person_object[name]);
		$("#personal").animate({
			opacity:'1'
		},1000);
		event.preventDefault();
	});
