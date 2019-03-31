$(function(){
    function footerPosition(){
        //设置文档正文宽度
        var contentWidth = document.body.scrollWidth + "px";
        document.getElementById("footer-outer").style.width = contentWidth;
        document.getElementById("ft-style").style.width = contentWidth;
        //移动端判断
	      var u = navigator.userAgent, app = navigator.appVersion;
	      var mobile = !!u.match(/AppleWebKit.*Mobile.*/)||!!u.match(/AppleWebKit/)&&u.indexOf('QIHU')&&u.indexOf('Chrome')<0;
	      var iPad = u.indexOf('iPad') > -1;

        $("#footer-outer").removeClass("fixed-bottom");
        var contentHeight = document.body.scrollHeight,//网页正文全文高度
            winHeight = window.innerHeight;//可视窗口高度，不包括浏览器顶部工具栏
        if(!(contentHeight > winHeight)){
            //当网页正文高度小于可视窗口高度时，为footer添加类fixed-bottom
            $("#footer-outer").addClass("fixed-bottom");
            if(mobile&&!iPad)
            {
              document.getElementById("footer-outer").style.width = "100%";
              document.getElementById("ft-style").style.width = "100%";
            }
        }

    }
    footerPosition();
    //移动端不处理resize,包括iPad
    if (!mobile)
    {
      $(window).resize(footerPosition);
    }
});
