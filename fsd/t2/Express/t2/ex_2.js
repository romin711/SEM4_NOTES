const express = require('express')
const app = express()

app.get('/' , (req , res) => {
    res.set('content-type' , 'text/plain')
    res.send('hi')
})

app.get('/about' , (req , res) => {
    res.set('content-type' , 'text/html')
    // res.write('hello')
    // res.send('romin')
    res.write('hello')

}).listen(3001 , () => {
    console.log('server started')
})