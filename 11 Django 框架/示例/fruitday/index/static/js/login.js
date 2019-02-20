function $useName(name){
    return window.document.getElementsByName(name)
}

var phone_parttern = /\d{11}/    /* 标准的电话检查: /^((0\d{2,3}-\d{7,8})|(1[3584]\d{9}))$/ */
var upwd_parttern = /\w{6,18}/

var uphone = $useName("uphone").value
var upwd = $useName("upwd").value

if (phone_parttern.test(uphone) && upwd_parttern.test(upwd)){
    return true
} else {
    window.alert("电话号码或密码格式不正确 ")
    return false 
}
