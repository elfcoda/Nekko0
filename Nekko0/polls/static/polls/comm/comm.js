$(function(){
    function footerPosition(){
        $("#footer-outer").removeClass("fixed-bottom");
        var contentHeight = document.body.scrollHeight,//网页正文全文高度
            winHeight = window.innerHeight;//可视窗口高度，不包括浏览器顶部工具栏
        if(!(contentHeight > winHeight)){
            //当网页正文高度小于可视窗口高度时，为footer添加类fixed-bottom
            $("#footer-outer").addClass("fixed-bottom");
        }

        //设置文档正文宽度
        var contentWidth = document.body.scrollWidth + "px";
        document.getElementById("footer-outer").style.width = contentWidth;
        document.getElementById("ft-style").style.width = contentWidth;
    }
    footerPosition();
    $(window).resize(footerPosition);
});
