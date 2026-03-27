var fs = require('fs')
var http = require('http')

http.createServer(function(req, res) {
    if(req.url === '/') {
        res.writeHead(200, {'content-type':'text/html'})
        res.end('<h1>hello</h1><img src="romin.jpg"/>')
    }

    else if(req.url === '/image') {
        var img = fs.readFileSync('romin.jpg')
        res.writeHead(200, {'content-type' : 'image/jpg'})
        res.end(img)
    }
}).listen(3120)