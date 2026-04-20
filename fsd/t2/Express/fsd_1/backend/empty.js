var express = require('express')
var path = require('path')
var app = express()

// Serve static files from frontend folder

app.use(express.urlencoded({extended:false}))

app.use(express.static(path.join(__dirname, '../frontend'), { index: 'empty.html' }))

app.post('/regi', (req, res) => {
    const {first_name,last_name} = req.body

    if(!first_name || !last_name) {
        res.send('all field must be filled')
    }

    else {
        res.send(`<h2>submit</h2> first_name: ${first_name} <br> last_name: ${last_name}`)
    }

})

app.listen(3000, () => {
    console.log('Server running on http://localhost:3000')
})
