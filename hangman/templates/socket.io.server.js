var http = require("http");
var socketio = require("socket.io");

var server = http.createServer(
function(request,response){
	response.end('Hello NodeJS');
}
);

server.listen(9892,function(){
	console.log('NodeJS Server Start port:9892');
}
);

var io = socketio.listen(server);
io.sockets.on("connection",function(socket){
	console.log('client connected');
}
);

function RandomNextInt(max){
	return 1+Math.floor(Math.random()*max);
}

var names = ["정석","성재","진","지우"]
