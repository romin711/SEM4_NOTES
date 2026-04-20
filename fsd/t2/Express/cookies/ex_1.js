var express = require('express')
var app = express()

var cp = require('cookie-parser')

app.use(cp())
app.get('/cookie'   , function(req , res) {
    res.cookie('name' , 'ExpressJs')
    res.cookie('fname' , 'express')
    res.cookie('lname' , 'js')
    res.cookie('ID' , '2' , {
        expires : new Date(Date.now() + 10000)
    })
    res.cookie('email' , 'xyz@gmail.com' , {maxAge : 2000})
    res.clearCookie('fname')
    res.send(req.cookies)
}).listen(3000)