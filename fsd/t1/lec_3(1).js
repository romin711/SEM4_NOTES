function main(cb) { 
    console.log("perform operation 1");

    setTimeout(function() {    
        console.log("operation completed"); 
    }, 2000);

    console.log("perform operation 2");
}

function callback_fun(result) {
    console.log("result: " + result);
}

main(callback_fun);