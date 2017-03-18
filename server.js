
var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var express = require('express');

app.get('/', function(req, res){
  res.sendFile(__dirname + '/index.html');
});

app.use(express.static('public'))

io.on('connection', function(socket){
  console.log('a user connected');
    socket.on('on', function(index){
  		console.log("on karo bero "+index);
  		const exec = require('child_process').exec;
  		exec('python on.py '+index+ " on" , (err, stdout, stderr) => {
		  if (err) {
		    console.error(err);
		    return;
		  }
		  console.log(stdout);
		});
  	});
  	
  	socket.on('off', function(index){
  		console.log("off karo bero "+index);
  		const exec = require('child_process').exec;
  		exec('python on.py '+ index +" off", (err, stdout, stderr) => {
		  if (err) {
		    console.error(err);
		    return;
		  }
		  console.log(stdout);
		});
  	});
});

http.listen(3002, function(){
  console.log('listening on *:3000');
});