//Vamos a utilizar la API fetch para llamar a nuestro servidor desde la vista de un cliente
const URL_BASE = 'http://127.0.0.1:8000/appGestionPedidos/PedidosCliente/'
let identificador = document.getElementById('id_js').textContent;
let botonHistorial = document.getElementById('boton-historial');

//Añadimos un escuchador de eventos al botón, para poder llamar a la API, y que cargue los datos solicitados
botonHistorial.addEventListener("click", (event) => {
    cargarDatos();
});

/*Con esta función, le decimos al servidor que nos proporciones los pedidos de un cliente determinado
 **Nos los devuelve en un json que posteriormente tratamos para crear una tabla
 */
function cargarDatos(){
    let url = URL_BASE + identificador //Esta es la url que corresponde a cada cliente según su id
    fetch(url)
        .then((response) => response.json())
        .then((json) => {
            //Mostramos por consola para probar que carga bien
            console.log(json);
            //Seleccionamos el div que hemos creado
            let div = document.getElementById('miPopup');
            let tabla = crearTabla(json); // Devuelve la tabla para insertar en el DIV
            div.innerHTML=''; //Borramos el contenido del div por si tuviera algo
            div.innerHTML = tabla; //Insertamos la tabla en el div


        })

}
//Con esta funcion creamos cada una de las lineas de la tabla con los valores que nos interesan
function crearLineaTabla(id, fecha, estado, importe){
    return `
        <tr>
            <td>${id}</td>
            <td>${fecha}</td>
            <td>${estado}</td>
            <td>${importe}</td>
        </tr>`;
}

function crearTabla(json) {
    let tabla = `
        <table>
            <thead>
                <tr>
                    <td>Id</td>
                    <td>Fecha Pedido</td>
                    <td>Estado</td>
                    <td>Importe</td>
                </tr>
            </thead>
            <tbody>
    `;

    // Recorrer el listado de pedidos para crear una fila por cada pedido
    for(let elemento of json) {
        tabla += crearLineaTabla(elemento.id, elemento.fecha_pedido, elemento.entregado, elemento.precio);
    }
    tabla += '</tbody></table>'
    return tabla;
}




