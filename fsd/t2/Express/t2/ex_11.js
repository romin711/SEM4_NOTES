var express = require('express')
var app = express()

const middleWare_1 = (req, res, next) => {
    req.name = 'samarth'
    console.log('name added')
    next()   
}

const middleWare_2 = (req, res, next) => {
    req.college = 'LJU'
    console.log('cld added')
    next()
}

app.get('/stu', middleWare_1, middleWare_2, (req, res) => {
    res.send('stu name: ' + req.name + 'clg name: '+ req.college)
}).listen(6001, () => {
    console.log('server started')
})