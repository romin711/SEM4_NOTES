const express = require('express')
const app = express()

stu = {
    name : 'LJU',
    age : 28
}

app.get('/' , (req , res) => {
    // res.send(stu)
    
    // res.write(JSON.stringify(stu))
    // res.send()

    res.json(stu)
}).listen(3000)