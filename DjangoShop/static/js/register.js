$(function(){
	var error_name=false;
	var error_pwd=false;
	var error_cpwd=false;
	var error_email=false;
	var error_remember=false;

	// 失去焦点
	$('#username').blur(function(event) {
		check_username();
	});
	$('#username').focus(function(event) {
		 $(this).next.hide();
	});


	function check_username(){

		var val = $('#username').val();
		//5到15位 , i忽略大小写
		var re = /^[a-z0-9_]{5,15}$/i;  // 等同 /^|w{5,15}$/i

		if(val==''){
			$('#username').next().html("用户名不能为空");
			$('#username').next().show();
			error_name =true;
			return;
		}

		if(re.test(val)){//通过条件
			error_name =false;
		}else{
			error_name =true;
			$('#username').next().html("用户名是包含数字,字母,下划线的5-15位字符");
			$('#username').next().show();
		}
	}

	// 失去焦点
	$('#pwd').blur(function(event) {
		check_pwd();
	});
	$('#pwd').focus(function(event) {
		 $(this).next.hide();
	});


	function check_pwd(){
		var re = /^[a-z0-9A-Z][\w\.]*@[\w](\.[\w]{2,3}){2,3}$/;

		var val = $('#pwd').val(); 
		var re = /^[a-zA-Z0-9@\$\*\.\!\?]{6,16}$/;
		if(val==''){
			$('#pwd').next().html("密码不能为空");
			$('#pwd').next().show();
			error_pwd =true;
			return;
		} 
		if(re.test(val)){//通过条件
			error_pwd =false;
		}else{
			error_pwd =true;
			$('#pwd').next().html("密码是包含数字,字母,以及@$*.!?的6-16位字符");
			$('#pwd').next().show();
		}

	}

	//再次输入密码
	function check_cpwd(){
		var pwd_val = $('#pwd').val(); 
		var cpwd_val = $('#cpwd').val(); 
		if(pwd_val ==cpwd_val ){
			error_cpwd=false;
		}else{
			error_cpwd=true;
			$('#cpwd').next().html("两次输入密码不一致");
			$('#cpwd').next().show();
		}
	}

	$('.input_submit').submit(function(event) {
		/* Act on the event */
		check_username();
		check_pwd();
		// check_cpwd();

		if(error_name==false && error_pwd==false){
			//提交
		}else{
			return false;
		}
	});

})