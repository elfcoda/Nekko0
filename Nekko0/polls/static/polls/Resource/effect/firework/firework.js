var fgm = {
    on: function (element, type, handler) {
        return element.addEventListener ? element.addEventListener(type, handler, false) : element.attachEvent("on" + type, handler)
    },
    un: function (element, type, handler) {
        return element.removeEventListener ? element.removeEventListener(type, handler, false) : element.detachEvent("on" + type, handler)
    },
    bind: function (object, handler) {
        return function () {
            return handler.apply(object, arguments)
        }
    },
    randomRange: function (lower, upper) {//������Χ��lower~upper�������
        return Math.floor(Math.random() * (upper - lower + 1) + lower)
    },
    getRanColor: function () {//������ʮ��������ɫ
        var str = this.randomRange(0, 0xFFFFFF).toString(16);
        while (str.length < 6) str = "0" + str;
        return "#" + str
    }
};
//��ʼ������
function FireWorks() {
    this.type = 0;
    this.timer = null;
    this.fnManual = fgm.bind(this, this.manual)
}
FireWorks.prototype = {
    initialize: function () {
        clearTimeout(this.timer);
        fgm.un(document, "click", this.fnManual);
        switch (this.type) {
            case 1:
                fgm.on(document, "click", this.fnManual);
                break;
        }
        ;
    },
    manual: function (event) {
        event = event || window.event;
        this.__create__({
            x: event.clientX,
            y: event.clientY
        });
    },
    __create__: function (param) {
        //param��������㣨���̻���ը�㣩
        var that = this;
        var oChip = null;
        var aChip = [];
        var timer = null;
        var oFrag = document.createDocumentFragment();
        (function () {
            //��50-100֮�����������Ƭ
            //����IE���������Ч�ʵ�, �����Χ��С��20-30
            //�Զ����̻�ʱ, �����Χ��С��20-30
            var len = (/msie/i.test(navigator.userAgent) || that.type == 2) ? fgm.randomRange(9, 9) : fgm.randomRange(9, 9)
            //���������̻���ը����ʵ��
            for (i = 0; i < len; i++) {
                //�̻�������̬ʵ��
                oChip = document.createElement("div");
                with (oChip.style) {
                    position = "fixed";
                    top = param.y + document.body.scrollTop + "px";
                    left = param.x + "px";
                    width = "4px";
                    height = "4px";
                    overflow = "hidden";
                    borderRadius = "4px";
                    background = fgm.getRanColor();
                }
                ;
                var speedRangeX = 2.5;
                var speedRangeY = 4.5;
                oChip.speedX = fgm.randomRange(-speedRangeX, speedRangeX);
                oChip.speedY = fgm.randomRange(-speedRangeY, speedRangeY);
                oFrag.appendChild(oChip);
                aChip[i] = oChip
            }
            ;
            document.body.appendChild(oFrag);
            timer = setInterval(function () {
                for (i = 0; i < aChip.length; i++) {
                    var obj = aChip[i];
                    with (obj.style) {
                        // top = obj.y + obj.speedY + "px";
                        // console.log(document.body.scrollTop);
                        // console.log(document.body.scrollHeight+"ww");
                        // console.log(obj.offsetTop);
                        top = obj.offsetTop + obj.speedY  + "px";
                        left = obj.offsetLeft + obj.speedX + "px";
                    }
                    ;
                    obj.speedY += 0.16;
                    obj.speedY += 0.14;
                    //�ж��̻���ը�����Ƿ����������֮�⣬Ϊ����remove
                    //splice() ������ɾ���� index ����ʼ���������Ԫ��
                    (obj.offsetTop < 0 || obj.offsetLeft < 0 || obj.offsetTop > document.documentElement.clientHeight + document.body.scrollTop || obj.offsetLeft > document.documentElement.clientWidth) && (document.body.removeChild(obj), aChip.splice(i, 1))
                }
                ;
                //�ж��̻���ը�����Ƿ�ȫ��remove��Ϊ����clearInterval(timer);
                !aChip[0] && clearInterval(timer);
            }, 18)
        })();
    }
};

fgm.on(window, "load", function () {
    var oFireWorks = new FireWorks();
    oFireWorks.type = 1;
    oFireWorks.initialize();
});

fgm.on(document, "contextmenu", function (event) {
    var oEvent = event || window.event;
    oEvent.preventDefault ? oEvent.preventDefault() : oEvent.returnValue = false
});
