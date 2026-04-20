var express = require('express')
var app = express()

app.use(
    express.urlencoded
    ({extended: true})
)

app.get('/' , (req, res) => {
    res.send(
        '<h3>create form</h3><form action="/user" method="post"><input type="text" name="name" placeholder="enter name"><button type="submit">submit</button></form>'
    )
})


app.post("/user", (req, res) => {
    const name = req.body.name
    res.send('user submit with name:' + name)
})

app.listen(5504, () => {
    console.log("sever started")
})