const student = [
    {
        name : "NAS",
        age : 25
    },

    {
        name : "IRK",
        age : 19
    },

    {
        name : "RJK",
        age : 20
    }
]

const a = student.sort((a,b) => b.age - a.age)

for (x of a) {
    // console.log(x.name + " " + x.age)
}









var test = {
    "division1" : {
        "name" : ['Z' , 'B' , 'H']
    },

    "division2" : {
        "name" : ['I' , 'R' , 'K']
    },
}


const div1_data = test.division1.name;
const div2_data = test.division2.name;


var combine_data = div1_data.concat(div2_data).sort()
// console.log(combine_data)












function firstLost(a1) {
    var temp = {};
    temp[a1[0]] = a1[a1.length - 1];
    return temp;
}

var data = ['RJK' , 'IRK' , 'ZNP' , 'APB'];
// console.log(firstLost(data))









const person = [
    {
        name : 'IRK',
        height : 5.2
    },


    {
        name : 'RJK',
        height : 6.0
    },

    {
        name : 'KGB',
        height : 5.0
    },

    {
        name : 'KKB',
        height : 5.4
    }
]

// console.log(Math.max(
//     ...person.map(obj => obj.height)
// ))


