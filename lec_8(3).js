var http = require('http')

http.createServer(function(req, res) {
    res.writeHead(200, {'content-type' : 'text/html'})
    res.write(req.url + "<br>")
    res.end("url-fetched")

}).listen(3120)