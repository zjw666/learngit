$(function(){
	tabs_init();            //首页标签初始化
	init();                  //杂项初始化
	button_change();          //初始化头像按钮大小
	$data=$("#list").clone();  //克隆头像列表，为头像分类动画做准备
	person_object = {
		zjw:"本科毕业于西南石油大学，现硕士研究生在读。爱好乒乓球和羽毛球，喜欢和朋友一起愉快地玩耍。处于人生十字口中一只迷茫的小白，最近由于毕业问题，心里充满了烦恼和忧虑，希望能早点做完项目，顺利发表文章毕业，最终能找到一份自己喜爱的工作。邮箱：591342608@qq.com",
		wmh:"暂无简介",
		gsm:"暂无简介",
		hwa:"暂无简介",
		lxx:"暂无简介",
		zs:"暂无简介",
		wxx:"暂无简介",
		zd:"暂无简介",
		wyl:"暂无简介",
		zht:"暂无简介"
	}
	news_change();           //使新闻导航栏的高度与内容栏相同
	news_check();            //检查是否翻到最后一篇新闻或第一篇新闻
	words_num_check();        //设置新闻翻页提示的标题长度
	news_type_check();        //添加新闻导航栏的当前激活功能
	input_add_class();        //为用户登录的输入框添加样式
	pic_width_height();       //控制用户头像长宽比
	bind_emojionArea();       //绑定表情输入框，提示用户评论需登录
	emoji_change();          //将unicode字符转化为图片
	placeholder();           //解决低版本的IE下没有placeholder属性问题
});

function init(){   //杂项初始化
	$("[data-toggle='tooltip']").tooltip();  //激活提示工具
	$("ul.nav-pills.nav-stacked.affix").width($("#scroll").width());  //使affix导航栏宽度动态变化
	$('#img-container button').hide();  //隐藏头像中的访问主页按钮
}

function tabs_init(){   //首页标签初始化
	$('ul.nav-tabs~article').hide();    //隐藏全部标签内容
	$('#Welcome').show();               //使标签首页内容显示
}

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
	news_change();
	pic_width_height();
});

$('#img-container').hover(     //头像按钮淡入淡出以及遮罩透明度变化
	function(){
	var button = $('#img-container button');
	$(button).stop(true);
	$('#mask').css("opacity","0.5");
	$(button).fadeIn("500");},
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


$('#classification button').click(function(){    //头像分类动画
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

$("#list a").click(function(event){  //为各个人物头像捆绑点击事件
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
	
$("#location div img").click(function(){  //连接地图头像与人物介绍界面
	var name=this.alt;
	var url= this.src;
	$("#personal").stop(stopAll=false,goToEnd=true);
	$("#personal").css("opacity","0");
	$("#personal h2").text(name);
	$("#personal img").attr("src",url);
	$("#personal p").text(person_object[name]);
	$("#personal").animate({
		opacity:'1'
	},1000);
});	

function news_change(){        //使新闻导航栏的高度与内容栏相同
	var news_contents=$('#article-content').height();
	$('#border').height(news_contents);
}

$('#pages li:contains(a)').click(function(){  //分页按钮的active类添加
	$(this).siblings().removeClass('active');
	$(this).addClass('active');
});


function news_type_check(){    //添加新闻导航栏的当前激活功能
	var type = window.location.pathname;
	if (type.lastIndexOf('life') != -1){
		var li = $('#type-news li')[0];
	}else if (type.lastIndexOf('academic') != -1){
		var li = $('#type-news li')[1];
	}else if (type.lastIndexOf('happy') != -1){
		var li = $('#type-news li')[2];
	}
	$(li).siblings().removeClass('active');
	$(li).addClass('current-news');
}

$('#pages-content button').click(function(){  //添加新闻详情页的翻页功能
	var text = window.location.href.split('/');
	text.pop();
	text.pop();
	if ($(this).attr('id')=='left'){
		text.push($('#left-text').attr('index'));
	}else{
		text.push($('#right-text').attr('index'));	
	}
	var url = text.join('/');
	window.open(url,'_self');
});

function news_check(){    //检查是否翻到最后一篇新闻或第一篇新闻
	var left = $('#left'),
		right = $('#right');
	if ($('#left-text').attr('index') == '-1'){
		$(left).attr('disabled',true);
		$(left).addClass('disabled');
	}else{
		$(left).attr('disabled',false);
		$(left).removeClass('disabled');
	}
	if ($('#right-text').attr('index') == '-1'){
		$(right).attr('disabled',true);
		$(right).addClass('disabled');
	}else{
		$(right).attr('disabled',false);
		$(right).removeClass('disabled');
	}
}

function words_num_check(){    //设置新闻翻页提示的标题长度
	var span1=$($('.news-text')[0]).text();
	var span2=$($('.news-text')[1]).text();
	if (span1.length > 15){
		var news_title=span1.slice(0,15)+'...';
		$($('.news-text')[0]).text(news_title);
	}
	if (span2.length > 15){
		var news_title=span2.slice(0,15)+'...';
		$($('.news-text')[1]).text(news_title);
	}
}

function input_add_class(){    //为用户登录的输入框添加样式
	$("form.user_form input").addClass("form-control");  
	$("#id_password").attr({"placeholder":"请输入密码",
							"oninvalid":"setCustomValidity('请输入密码');",
							"oninput":"setCustomValidity('');"})
	$("form.user_form #id_username").attr({"placeholder":"请输入用户名或邮箱",
							"oninvalid":"setCustomValidity('请输入用户名或邮箱');",
							"oninput":"setCustomValidity('');"})
	$("form.user_form #id_email").attr({"placeholder":"请输入邮箱地址",
							"oninvalid":"setCustomValidity('请输入正确的邮箱地址');",
							"oninput":"setCustomValidity('');"})
	$("#id_captcha_1").attr({"placeholder":"请输入验证码",
							"class":"form-control",
							"required":"required",
							"oninvalid":"setCustomValidity('请输入验证码');",
							"oninput":"setCustomValidity('');"})
	$("#id_new_password1,#id_new_password2").attr({"placeholder":"请输入重置的密码",
							"oninvalid":"setCustomValidity('请输入重置的密码');",
							"oninput":"setCustomValidity('');"})
}

function pic_width_height(){  //控制用户头像长宽比
	var pic_width = $("#person_pic").width();
	$("#person_pic").height(pic_width);
}

$(document).on("change","input[type=file]",function(){	//上传头像图片预览，未来元素绑定法
	var fileobj = $(this)[0];
	if (fileobj && fileobj.files){   //是否能获取file对象
		var headimage = fileobj.files[0]
		if (headimage.type.split('/')[0] == 'image'){
			if(headimage.size/1024/1024 <= 1 ){
					$('#pic_name').text(headimage.name);
					if (typeof FileReader != 'undefined'){
						var reader = new FileReader();
						reader.readAsDataURL(headimage);
						reader.onload = function(){
							var dataURL = reader.result;
							$("#person_pic").attr("src",dataURL);
						};
					}else{
						var URL = window.URL || window.webkitURL;
						var imageURL = URL.createObjectURL(headimage);
						$("#person_pic").attr("src",imageURL);
					} 
			}else{
				alert("图片大小必须小于1M")
				fileobj.value = '';
				$('#pic_name').text("上传图片失败");
			}
		}else{
			alert("上传文件必须为图片格式");
			fileobj.value = '';
			$('#pic_name').text("上传图片失败");
		}
	}else{    //不能获取file对象，一般都是低版本的IE
		try{
			fileobj.select();
			fileobj.blur();
			var path = document.selection.createRange().text;    
			var fso = new ActiveXObject("Scripting.FileSystemObject");
			var fileSize = fso.GetFile(path).size;
			if (fileSize/1024/1024 >= 1){        //检查图片大小
				var file_clone = fileobj.cloneNode(false);
				fileobj.parentNode.replaceChild(file_clone,fileobj);    //由于低版本IE无法修改input file的值，直接克隆一个替换原来的实现清空操作
				$('#pic_name').text("上传图片失败");
				alert("图片大小必须小于1M");
			}else{                                //预览图片
				var text_list = $("input[type=file]").val().split("\\");
				var pic_name = text_list[text_list.length-1];
				$('#pic_name').text(pic_name);
				var pic = document.getElementById("person_pic");
				pic.style.filter = "progid:DXImageTransform.Microsoft.AlphaImageLoader(sizingMethod='scale',src=\"" + path + "\")";    //滤镜预览图片
				pic.src = 'data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==';                 //设置img的src为base64编码的透明图片，要不会显示红xx
			}
		}catch(e){
			alert(e+"\n"+"如果错误为：Error:Automation 服务器不能创建对象；"+"\n"+"请按以下方法配置浏览器："+"\n"+"请打开【Internet选项-安全-Internet-自定义级别-ActiveX控件和插件-对未标记为可安全执行脚本的ActiveX控件初始化并执行脚本（不安全）-点击启用-确定】");
		}
		
	}
});

$("img.captcha").click(function(){   //更新验证码图片ajax
	$.getJSON("/captcha/refresh",function(data){
		$("img.captcha").attr("src",data.image_url);
		$("#id_captcha_0").attr("value",data.key);
		$("#id_captcha_1").keyup();
	});
});

$("#id_captcha_1").keyup(function(){    //验证码输入验证ajax
	var response=$('#id_captcha_1').val();
	var hashkey=$('#id_captcha_0').val();
	var json_data={
		'response':response,
		'hashkey':hashkey
	}
	$.getJSON("/ajax_captcha",json_data,function(data){
		$("span.captcha_status").remove();
		if (data.status){
			$("#id_captcha_1").after('<span class="captcha_status glyphicon glyphicon-ok-sign"></span>');
		}else{
			$("#id_captcha_1").after('<span class="captcha_status glyphicon glyphicon-remove-sign"></span>');
		}
	});
});

/*
$("#contact_form textarea,.reply_form textarea").focus(function(){  //提示用户评论前需登录
	if ($("input[name=author]").val() == "None"){
		$("#Modal").modal({backdrop:'static'});
		$(this).blur();
	}
});
*/

$("#contact_form").submit(function(e){                    //用户登陆后才能提交评论表单
	var author = $("input[name=author]").val();
	var content = $("#contact_form textarea").val();
	if (author == "None"){
		e.preventDefault();
		$("#Modal").modal({backdrop:'static'});
	}else if (!content.trim()){
		e.preventDefault();
		$("#contentModal").modal({backdrop:'static'});
	}
});

$("#contact_form button").click(function(){             //评论内容不能为空
	var content = $("#contact_form textarea").val();
	if (!content.trim()){
		$("#contentModal").modal({backdrop:'static'});
	}	
});

$("#email_actived_button").click(function(){   //为邮箱激活模态框登录按钮绑定事件
	window.open("/active/",'_blank');
	$("#email_modal .close").click();
});

$("#id_important").change(function(){    //提示用户启用邮箱服务前需激活邮箱ajax
	if (this.checked){
		var author = $("input[name=author]").val();
		if (author != "None"){
			var json_data = {'author':author};
			$.getJSON("/email_actived_check/",json_data,function(data){
				if (data.status){
					$("#email_modal").modal({backdrop:'static'});
					$("#id_important").attr("checked",false);
				}
			});
		}
	}
});

$("#modal-login").click(function(){   //为登录验证模态框登录按钮绑定事件
	window.open("/login/?next=/comment/",'_self');
});

$(document).on("click",".form_button",function(){   //ajax提交回复表单,这里的提交按钮要采用未来元素绑定事件法
	var textarea_content=$($($(this).prev()).find('textarea')),
		content=$(textarea_content).val(),
		author=$("input[name=author]").val(),
		reply_to=$(this).attr("person"),
		comment=$(this).attr("comment");
	if (author != "None"){
		if (content.trim()){
			var button = this;
			var json_data={
				'content':content,
				'author':author,
				'reply_to':reply_to,
				'comment':comment
			}
			$(textarea_content).val("");        //清空回复框内容
			$($(textarea_content).next().children()[0]).html(''); //清空关联的表情框内容
			$($(button).parent().parent().siblings("a")).click();   //关闭回复框
			$.ajax({
				url:'/reply_ajax/',
				type:'POST',
				dataType:'json',
				data:json_data,
				success:function(result){
					if (result.reply_status){   //生成新的回复，并插入到对应评论的回复列表中
						var reply_list=$(button).parents("li.media").find("div.media"),
							date = new Date(result.time),
							div_media=$('<div></div>').attr("class","media"),
							a_media=$('<a></a>').attr({
								"href":"/personal/?name="+result.author_name,
								"class":"media-left"
							}),
							img=$('<img>').attr({
								"src":result.url,
								"class":"media-object img-circle",
								"alt":"photo"
							}),
							div_body=$('<div></div>').attr("class","media-body"),
							h4=$('<h4></h4>').attr("class","media-heading"),
							span_h4=$('<span></span>').attr("class","glyphicon glyphicon-share-alt"),
							p=$('<p></p>').text(content),
							a_media_body=$('<a></a>').attr({
								"href":"#reply_"+result.reply_id,
								"class":"reply_button",
								"reply":result.author_name,
								"data-toggle":"collapse"
							}).text("回复"),
							span=$('<span></span>').attr("class","pull-right").text(date.getFullYear()+'年'+(date.getMonth()+1)+'月'+date.getDate()+'日'),
							div_form=$('<div></div>').attr({
								"class":"collapse well reply_form",
								"id":"reply_"+result.reply_id
							}),
							form=$('<form></form>').attr({
								"role":"form",
								"method":"post",
								"action":"#"
							}),
							div_form_group=$('<div></div>').attr("class","form-group"),
							textarea=$('<textarea></textarea>').attr({
								"class":"form-control",
								"name":"content",
								"placeholder":"请输入回复的内容",
								"oninvalid":"setCustomValidity('请输入你要回复的内容');",
								"title":"请输入回复的内容",
								"required":"required"
							}),
							form_button=$('<button></button>').attr({
								"type":"button",
								"class":"btn btn-default pull-right form_button",
								"person":result.author_name,
								"comment":comment
							}).text("提交");
							$(div_form_group).append(textarea);
							$(form).append(div_form_group,form_button);
							$(div_form).append(form);
							$(h4).append(result.author_name,' ',span_h4,' ',reply_to);
							$(div_body).append(h4,p,a_media_body,span,div_form);
							$(a_media).append(img);
							$(div_media).append(a_media,div_body);
							if (reply_list.length != 0){
								$(reply_list[reply_list.length-1]).after(div_media);
							}else{
								$("#comment_"+comment).after(div_media);
							}
							$(div_media).before('<hr class="comment_line" />');
							$(textarea).emojioneArea({                        //绑定表情输入框，提示用户评论需登录
											events:{
												focus:function(editor){
													if ($("input[name=author]").val() == "None"){
													$("#Modal").modal({backdrop:'static'});
													$(editor).blur();	
													}
												}	
											}
										});
							var value = $(p).text();                             //将unicode表情字符转化为图片
							var code = $("<div></div>").text(value).html();    //防止跨站脚本攻击
							$(p).html(emojione.toImage(code));
					}else{
						alert("回复失败，请刷新页面重试，如有问题，请联系网站管理人员");
					}
				}
			});
		}else{
			$("#contentModal").modal({backdrop:'static'});
		}
	}else{
		$("#Modal").modal({backdrop:'static'});
	}
});

$("#email_active button").click(function(){  //邮箱激活按钮
	window.open('/active/','_blank');
	$(this).attr("disabled","disabled");
	span_text = $("#active_text"); 
	$(span_text).removeClass("unactived");
	var time = 60;
	var Interval = window.setInterval(function(){
		$(span_text).text(time);
		time -= 1;
		if (time < 0 ){
			clearInterval(Interval);
			$("#email_active button").attr("disabled",false);
			$(span_text).text("再次发送邮件");
		}
	},1000);
});

function bind_emojionArea(){     //绑定表情输入框，提示用户评论需登录
	var textarea = $(".contact_article textarea");
	if (textarea.length){
		$(textarea).emojioneArea({
			events:{
				focus:function(editor){
					if ($("input[name=author]").val() == "None"){
					$("#Modal").modal({backdrop:'static'});
					$(editor).blur();	
					}
				}	
			}
		});
	}
}

function emoji_change(){   //将unicode表情字符转化为图片
	$(".media-body p").each(function(){
		var value = $(this).text();
		var code = $("<div></div>").text(value).html();    //防止跨站脚本攻击
		$(this).html(emojione.toImage(code));
	});
}

function placeholder(){       //解决低版本的IE下没有placeholder属性问题
	if (! ('placeholder' in document.createElement('input'))){     //判断是否支持placeholder属性
		$("input[placeholder]").each(function(){
			$(this).parent().append("<span class='placeholder'>" + $(this).attr("placeholder") + "</span>");
			if ($(this).val() != ""){
				$(this).parent().find('span.placeholder').hide();
			}
		});
		$("input[placeholder]").focus(function(){
			$(this).parent().find('span.placeholder').hide();
		});
		$("input[placeholder]").blur(function(){
			if ($(this).val()== ""){
				$(this).parent().find('span.placeholder').show();
			}
		});
		$("span.placeholder").click(function(){    //当点击span元素时，输入框获得焦点
			$(this).parent().find('input').focus();
		}).css({
			"color":"gray",
			"position":"absolute",
			"bottom":"10%",
			"left":"10px",
			"zIndex":"10"
		});
		$("span.placeholder").parent().css("position","relative");
		$("ul.errorlist").css({
			"position":"absolute",
		});
		$("ul.errorlist").parent().after("<div style='height:20px'></div>");
	}
}
