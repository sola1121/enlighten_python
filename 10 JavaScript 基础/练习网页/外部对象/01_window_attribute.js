/* 确认框对象 */
function conBtn(){
    var res = window.confirm("点击确认按钮.")   // 也可以直接写confirm()
    window.alert(res)
}

/* 计时器 */
var timer
function format_time(){
    var now = new Date()
    var year = now.getFullYear()
    var month = now.getMonth() + 1
    var date = now.getDate()
    var hour = now.getHours()
    var minute = now.getMinutes()
    var second = now.getSeconds()
    function zero_format(value){
        if (value<10)
            value = "0" + value
        return value
    }
    var format_msg = year + "年" + zero_format(month) + "月" + zero_format(date) + "日  " 
                    + zero_format(hour) + ":" + zero_format(minute) + ":" + zero_format(second)
    return format_msg
}

function begin_interval(){
    timer = setInterval(function(){console.info(format_time())}, 1000)   // 每一次点击其绑定按钮就会新建一个timer对象
}

function clear_interval(){
    clearInterval(timer)   // 但是clear方法只会清除绑定的timer变量, 如果创建多个, 那多余的就不会被清除, JS可能没有垃圾回收
}