const express = require('express')
const app = express()




//  if in same folder
// app.use(express.static(__dirname))
// // filename must be inde.html
// app.listen(5200)




const path = require('path')
const staticPath = path.join(__dirname, '../frontend')

app.use(express.static(staticPath))
app.get('/', (req,res) => {
    res.sendFile(staticPath + '/index.html')
})

app.listen(3000)





// const staticPath = path.join(__dirname, '../frontend')

// app.use(express.static(staticPath))
// app.get('/precess_get' , function(req, res) {
//     var first = req.query.fn
//     var last = req.query.ln

//     console.log(req.query)

//     res.send(`welcome ${fn} ${ln}`)
// }).listen(3000)