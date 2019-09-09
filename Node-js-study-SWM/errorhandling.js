process.on('uncaughtException', function(error) {
    console.log('Error ' + error.stack);
    process.exit(1);
})

function makeException() {
    throw new Error('Custom Exception!!');
}

setTimeout(function() {
    console.log('Hello');
    setTimeout(function() {
        console.log('World');
    }, 1000);
}, 1000);

try {
    makeException();
}catch(err) {
    console.log('try-catch ' + err.stack);
}

//makeException();

console.log('!!!!');