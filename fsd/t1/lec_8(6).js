var h = require('http')
var server = h.createServer(function(req, res) {
    if(req.url == '/about')
    {
        res.writeHead(200, {'content-type' : 'text/html'})
        data = ps.readFileSync('b.txt' , 'utf-8')

        res.write('')
        res.end()
    }

})
server.listen(5051)