const url = require('url')
process.noDeprecation = true
const addr = 'https://example.com:3000/about?name=xyz&age=20'
const result = url.parse(addr , true)
// console.log(result.query)



const addr2 = '//example.com/about'
const result2 = url.parse(addr2 , false , true)
// console.log(result2.host)



const addr3 = 'https://xyz:1234@example.com:3000/about?name=xyz&age=20#section1'
const result3 = url.parse(addr3)
console.log(result3.auth)