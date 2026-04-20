var express = require('express')
var path = require('path')
var app = express()

app.use(express.urlencoded({extended:false}))

// app.use(express.static(__dirname, {index:'p.html'}))
app.use(express.static(path.join(__dirname, '../frontend'), { index: 'p.html' }))


app.post('/process',function(req,res) {
    console.log(req.body.first_name + ' ' + req.body.last_name)

    res.send(req.body)
})

app.listen(3000)