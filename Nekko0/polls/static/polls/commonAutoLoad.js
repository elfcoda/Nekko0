function aplayerAutoSet() {
  //var apSetFolder = document.getElementById("aplayer").firstElementChild.firstElementChild.nextElementSibling.lastElementChild.lastElementChild.lastElementChild;
}

var os = function() {
     var ua = navigator.userAgent,
     isWindowsPhone = /(?:Windows Phone)/.test(ua),
     isSymbian = /(?:SymbianOS)/.test(ua) || isWindowsPhone,
     isAndroid = /(?:Android)/.test(ua),
     isFireFox = /(?:Firefox)/.test(ua),
     isChrome = /(?:Chrome|CriOS)/.test(ua),
     isTablet = /(?:iPad|PlayBook)/.test(ua) || (isAndroid && !/(?:Mobile)/.test(ua)) || (isFireFox && /(?:Tablet)/.test(ua)),
     isPhone = /(?:iPhone)/.test(ua) && !isTablet,
     isPc = !isPhone && !isAndroid && !isSymbian;
     return {
          isTablet: isTablet,
          isPhone: isPhone,
          isAndroid : isAndroid,
          isPc : isPc
     };
}();

function stopVisit() {
    if (os.isPhone || os.isAndroid)
    {
	    var v = document.getElementById("stop-visit");
            v.innerHTML = "please visit the page on PC browser.";
	    alert("为了更好的访问体验，请使用PC端浏览器哦~");
	    if (window.stop)
	        window.stop();
	    else
	        document.execCommand("Stop");
    }
}
