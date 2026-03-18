const fs = require('fs')
const path = require('path')

let oldPath = 'lj/sample.txt'

let dir = path.dirname(oldPath)

let fileName = path.basename(oldPath)

let newFilePath = dir + '/' + fileName


fs.copyFile(newFilePath , dir + '/tempt.txt' , (err) => {
    if(err) throw err
    console.log('file copied to temmp.txt')

    fs.unlink(newFilePath , (err) => {
        if(err) throw err
        console.log('original file deleted')
        console.log('original operation completed successfully')

    })
})