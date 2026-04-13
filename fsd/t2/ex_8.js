var express = require('express')
var app = express()

app.use(
    express.urlencoded
    ({extended: true})
)

app.get('/' , (req, res) => {
    res.send(
        '<h3>create form</h3><form action="/user" method="post"><input type="text" name="name" placeholder="enter name"><input type="email" name="email" placeholder="example@email.com"><button type="submit">submit</button></form>'
    )
})


app.post("/user", (req, res) => {
    const name = req.body.name
    const name1 = req.body.email
    res.write('user name:' + name)
    res.write("\nemail id: " + name1)
    res.send()
})

app.listen(5504, () => {
    console.log("sever started")
})