const u = require('url')
const addr = 'http://localhost:8080/default,html?year=2025&month=feb'
process.noDeprecation = true
const q = u.parse(addr , true)
// console.log(q)

const qdata = q.query
// console.log(qdata.year)

if(qdata.year % 4 ==0) {
    // console/log('its a leap year')
}

else {
    // console.log('its a not leap year')
}





// const ps = require('fs')
// const addr2 = 'http://localhost:8080/default.html?year=2045&month=april'
// const q2 = u.parse(addr2 , false)
// console.log(q2)
// const qdata2 = JSON.stringify(q2.query)
// ps.writeFile('fsd2.txt' , qdata2 , (err) => {
//     console.log('completed')
// })




// const {url} = require('url')
// const myurl = new URL("http://localhost:8080/default.html?year=2045&month=april")
// console.log('href :' , myurl.href)
// console.log('href :' , myurl.host)
// console.log('href :' , myurl.port)



const myurl2 = new URL("http://localhost:8080/test?m1=50&m2=30&m3=20")
const result3 = u.parse(myurl2)
console.log(result3)
