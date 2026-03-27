var http = require('http')

http.createServer(function(req, res) {
    res.writeHead(200, {'content-type' : 'application/json'})
    var data = {
        subject: 'fsd-2',
        topic: 'xyz'
    }
    res.end(JSON.stringify(data))

}).listen(3120, () => {
    console.log('server is running')    
})  