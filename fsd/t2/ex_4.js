var express = require('express')
var app = express()

app.get('/calendar/:day/event/:ename' , (req , res) => {
    res.send(req.params)
}).listen(3000 , () => {
    console.log("server started")
})