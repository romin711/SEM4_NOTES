const fs = require('fs')
const path = require('path')

let oldPath = 'lj/sample.txt'

let dir = path.dirname(oldPath)

let fileName = path.basename(oldPath)

let newFilePath = dir + '/' + fileName

fs.mkdir(dir , (err) => {
    if(err) throw err

    console.log('directory created' , dir)

    fs.writeFile(newFilePath , 'sample data for file' , (err) => {
        if(err) throw err
    
        console.log('original file created' , newFilePath)
    })
})

