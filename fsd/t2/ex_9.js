var express = require('express')
var app = express()

stu = {
    u1 : [
            {name : 'lju' , id : 2},
            {name1 : 'ljiet' , id : 3},
            {name2 : 'ljip' , id : 4}
    ]}

app.get('/student', (req, res) => {
    res.set('content-type' , 'text/html')
    res.write('<center><table cellspacing="5px" cellpadding="8px" borser="1px solid"><tr><th>name</tr><th>id</th></tr> for(i of stu.u1){res.write}')

})