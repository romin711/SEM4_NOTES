var express = require('express')
var app = express()

var cp = require('cookie-parser')

app.use(cp())
app.use(express.static(__dirname , {index : 'form.html'}))
app.use(express.urlencoded())

app.post('/next'   , (req , res , next) => {
    res.cookie('fname' , req.body.first_name)
    res.cookie('lname' , req.body.last_name)
    res.cookie('radiobutton' , req.body.review , {maxAge:10000})
    res.redirect('/admin')

    const {name , email, review} = req.body
    const feedback = {name , email, review}

    res.cookie('feed ' , feedback, {maxAge:10000} )
    res.send('ty for your feedback<br> <a href=""/feedback>show</a>')

})


app.listen(3000)

if(feedback) 
{
    res.send(`feedback details

    name : ${feedback.name}
    name : ${feedback.name}
    name : ${feedback.name}
    
    `)
}