const prompt = require("prompt-sync")();

let limite = Number(prompt("¿Cuántas líneas quieres generar? "));
let lista = [];

for (let i = 1; i <= limite; i++) {
    let resultado = "";

    if (i % 3 === 0) {
        resultado += "Fizz";
    }

    if (i % 5 === 0) {
        resultado += "Buzz";
    }

    if (i % 7 === 0) {
        resultado += "Woof";
    }

    if (resultado === "") {
        lista.push(i);
    } else {
        lista.push(resultado);
    }
}

console.log(lista);