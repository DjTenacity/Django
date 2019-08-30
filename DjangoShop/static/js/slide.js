$(function(){
	let $li = $('.slide_pics li');
	let $prev = $('.prev');
	let $next = $('.next');
	let $points = $('.points');

	let len = $li.length;
	console.log(len); 

	//将要运动过来的li
	var nowli = 0 ;
	//当前要离开的li
	var preli = 0 ;

	var timer =null;

	$li.not('.frist').css({ 	left:  760 	});

	$li.each(function(index, el) {
		// 创建li ,去掉 <> 才是选择li
		var $sli = $('<li>');

		if(index ==0){
			$sli.addClass('active');
		}
		 $sli.appendTo('.points')
	});

	$points=$('.points li');

	$points.click(function(event) {
		 nowli = $(this).index();
		 if(nowli==preli){
			return;
		 }
		 move();
		 $(this).addClass('active').siblings().removeClass('active');
	});

	$prev.click(function(event) {
		nowli--;
		move();
		$points.eq(nowli).addClass('active').siblings().removeClass('active');
	});

	$next.click(function(event) {
		nowli++
		move();
		$points.eq(nowli).addClass('active').siblings().removeClass('active');
	});
	$('.slide').mouseenter(function(event) {
		 clearInterval(timer);
	});
	$('.slide').mouseleave(function(event) {
		timer = setInterval(autoplay,4000);
	});

	timer = setInterval(autoplay,4000);

	function autoplay(){
		nowli++
		move();
		$points.eq(nowli).addClass('active').siblings().removeClass('active');
	}

	function move(){
		if(nowli<0){
			nowli = len-1;
			preli=0;
			$li.eq(nowli).css({ left:  -760  });
			$li.eq(preli).stop().animate({ left: 760});
			$li.eq(nowli).stop().animate({ left: 0});
			preli =nowli;
			return;
		}
		if(nowli>len-1){
			nowli = 0;
			preli=len-1;
			$li.eq(nowli).css({ left:   760  });
			$li.eq(preli).stop().animate({ left: -760});
			$li.eq(nowli).stop().animate({ left: 0});
			preli =nowli;
			return;
		}

		if(nowli> preli){
			$li.eq(nowli).css({ left:  760  });
			$li.eq(preli).stop().animate({ left: -760});
			$li.eq(nowli).stop().animate({ left: 0});
		}else{
			$li.eq(nowli).css({ left:  -760  });
			$li.eq(preli).stop().animate({ left: 760});
			$li.eq(nowli).stop().animate({ left: 0});
		}
		preli =nowli;
	}
})