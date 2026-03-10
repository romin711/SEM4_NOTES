var a = {
    "name" : "test",
    "age" : 30,
    "isPass" : false,
    "address" : {
        "city" : "ahm",
        "zip" : "380015"
    },

    "subjects" : ["maths" , "coa"],
    "year" : null
}

// console.log(a)
// console.log(a.age)
// console.log(a["address"])
// console.log(a["address"]["city"])

// const data = require("./lec_1.json")
// console.log(data.name)
// console.log(data.age)


let person = {
    name : "rahul",
    age : 22,
    city : "ahm"
}

person.age = 30
// console.log(person)




person["city"] = "surat"
// console.log(person)

let key = 'age'
person[key] = 25
// console.log(person)







const obj = JSON.parse('{"name" : "xyz" , "age" : "17" , "dob" : "1997-03-14"}');
// console.log(obj.dob)

b = new Date(obj.dob)
// console.log(b)

c = new Date()
// console.log(c)