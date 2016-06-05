window.addEventListener("load",onPageLoaded,false);

function onPageLoaded(){
	var socket = io.connect("127.0.0.1:9892");
}

