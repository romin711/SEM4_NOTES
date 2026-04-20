var express = require('express')
var path = require('path')
var app = express()

// Serve static files from frontend folder
app.use(express.static(path.join(__dirname, '../frontend'), { index: 'calc.html' }))

app.get('/calc', (req, res) => {
    res.set('content-type', 'text/html')
    var n1 = parseInt(req.query.n1)
    var n2 = parseInt(req.query.n2)

    if ((n1 > 0) && (n2 > 0)) {
        let a
        if (req.query.formula == 'addition') {
            a = n1 + n2
            res.write("<h1>add is: " + a + "</h1>")
        } else if (req.query.formula == 'subtraction') {
            a = n1 - n2
            res.write("<h1>sub is: " + a + "</h1>")
        } else if (req.query.formula == 'multi') {
            a = n1 * n2
            res.write("<h1>multi is: " + a + "</h1>")
        } else if (req.query.formula == 'div') {
            a = n1 / n2
            res.write("<h1>div is: " + a + "</h1>")
        } else {
            res.write('error')
        }
    }

    res.end()
})

app.listen(3000, () => {
    console.log('Server running on http://localhost:3000')
})
