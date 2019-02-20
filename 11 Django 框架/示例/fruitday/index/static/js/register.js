function $useName(name){
    return window.document.getElementsByName(name)
}

if ($useName("cpwd").value == $useName("upwd").value){
    return true
} else {
    return false
}