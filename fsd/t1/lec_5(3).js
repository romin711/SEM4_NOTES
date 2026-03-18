var pm = require('path')

path = pm.dirname('D:/lj/abc.html')
console.log(path)

path = pm.basename('D:/lj/abc.html')
console.log(path)

ext = pm.extname('D:/lj/abc.html')
console.log(ext)

path = pm.parse('D:/lj/abc.html')
console.log(path)

if(path.ext == '.html') {
    console.log('html document')
}

else {
    console.log('not a html document')
}