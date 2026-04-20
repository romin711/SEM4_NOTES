var express = require('express')
var app = express()

app.get('/user' , (req, res) => {
    const name = req.query.name
    const age = req.query.age

    res.send(
        `name:${name}, age: ${age}`
    )
}).listen(3000)

