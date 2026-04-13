var express = require('express')
var app = express()

app.get('/' , function(req , res) {
    res.set('content-type' , 'text/html')
    // res.type('text/plain')
    // res.setHeader('content-type' , 'text/plain')
    res.send("<h1>hello</h1>")
}).listen(3000)