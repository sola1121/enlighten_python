function testShow(){
    $useId("test").innerHTML = "<h3>" + "hello_world" + "</h3>"
}

function show_value(){
    $useId("test").innerText = $useId("input_text1").value + $useId("input_text2").value
}

function $useId(id_code){
    return document.getElementById(id_code)
}