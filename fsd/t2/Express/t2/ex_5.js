var express = require('express')
var app = express()

app.get('/calendar/:day/event/:ename' , (req , res) => {

    const day = parseInt(req.params.day)
    const ename = req.params.ename

    res.write(typeof day)
    // res.send({
    //     day: day,
    //     type: typeof day,
        
    // })
}).listen(3000 , () => {
    console.log("server started")
    // console.log(typeof day)
    // console.log(typeof ename)
})