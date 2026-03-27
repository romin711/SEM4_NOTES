var h = require('http')
var server = h.createServer(function(req, res) {
    if(req.url == '/')
    {
        res.writeHead(200, {'content-type' : 'text/html'})
        res.write('<h1>home page</h1><div> <ul><li><a href = "/">home</a></li><li><a href = "/about">about</a></li></ul></div>')
        res.end()
    }

    else if(req.url == "/about")
    {
        res.writeHead(200, {'content-type' : 'text/html'})
        res.write('<h1>about page</h1>')
        res.end()
    }

    else {
        res.writeHead(404, {'content-type' : 'text/plain'})
        res.write("page not found")
        res.end("check url")
    }
})
server.listen(5051)