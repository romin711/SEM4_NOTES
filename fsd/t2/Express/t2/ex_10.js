var express = require('express')
var app = express()

app.get('/user/:id', (req, res) => {
    const userId = req.params.id;
    const name = req.query.name;
    const age = req.query.age;

res.json({
    message: 'data receive',
    params: {id :userId},
    query: {name, age}
    
})
}).listen(4001 , () =>{
    console.log('romin')
})


