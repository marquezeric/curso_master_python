/*alert('Hola Mundo!!!');*/

var nombre = "Eric Márquez";
var altura = 167;

/*document.write(nombre);*/
/*document.write(altura);*/

/* Comentado para ejemplo Function
var concatenacion = nombre + " " + altura;

var datos = document.getElementById("datos")
datos.innerHTML = `
<h1>Hola caja de datos</h1>
<h2>mi nombre es: ${nombre}</h2>
<h3>mido: ${altura} cm</h3>
`;
fin Comentado para ejemplo Function*/
/* cuando se pone += agregará el contenido del div más lo que se agrega en las líneas de abajo  */
/* Comentado para ejemplo Function
if (altura >= 190){
    datos.innerHTML += `<h1>Eres una persona ALTA</h1>`
} else {
    datos.innerHTML += `<h1>Eres una persona BAJITA</h1>`
}

/* Bucle for
Inicializador, Condición, Incrementador
*/
/*fin Comentado para ejemplo Function*/
/*for(var i = 2000; i<=2021; i++){
    datos.innerHTML += "<h2>estamos en el año: "+i;
}
*/
function MuestraMiNombre(nombre, altura) {
    var misDatos =`
        <h1>Hola caja de datos</h1>
        <h2>mi nombre es: ${nombre}</h2>
        <h3>mido: ${altura} cm</h3>
    `;
    return misDatos;
}

function imprimir(){
    var datos = document.getElementById("datos");
    datos.innerHTML = MuestraMiNombre("Juan Rivera", 190);
}
imprimir();

var nombres = ['Víctor','Antonio','Joaquín'];
/*alert(nombre[1])*/

document.write('<h1>Listado de nombres</h1>')

/*for (i=0; i < nombres.length; i++){
    document.write(nombres[i]+ '<br/>');
}
*/

/*nombres.forEach(function (nombre){
    document.write(nombre + '<br/>')
});
*/
nombres.forEach((nombre) => {
    document.write(nombre + '<br/>')
});