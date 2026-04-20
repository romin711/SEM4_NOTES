var express = require('express')
var app = express()

const entryLog = (req, res, next) => {
    console.log('stu entered campus')
    next()
}

const checkId = (req, res, next) => {
    const hashId = true //false

    if(hashId) {
        res.student = 'xyz'
        console.log('id verified')
        next()
    }

    else {
        res.send('access not found: no id card')
    }
}

app.use('/class' , entryLog , checkId)
app.get('/class' , (req, res) => {
    res.send(`welcome ${req.student}`)
}).listen(3000)