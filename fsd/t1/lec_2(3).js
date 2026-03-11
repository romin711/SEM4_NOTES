const a = {
    "a" : "LJU",
    "b" : ["CSE" , "MA&CP" , "CE"],
    "c" : [
        {
            "d" : "hi",
            "e" : ["are" , 4 , {
                'f' : ['semester' , 'we']
            }]
        }
    ],

    "g" : {
        "h" : "students",
        "i" : ["of" , "!"]
    },

    "j" : [
        {
            "k" : "python",
            "l" : "branch" 
        },
        "fsd-2"
    ]
}


console.log(a.c[0].d , a.g.i[1] , a.c[0].e[2].f[1] , a.c[0].e[0] , a.g.h , a.g.i[0] ,a.c[0].e[2].f[0] , a.c[0].e[1] , a.g.i[0] , a.b[0] , a.j[0].l)