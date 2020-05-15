//Cálculo del precio total en el formulario del pedido
function calcularPrecio(){

    let base_imponible = document.getElementById("id_base_imponible").value;
    let iva = document.getElementById("id_iva").value;
    document.getElementById("id_precio").value = base_imponible*(1+ iva/100);

}
document.getElementById("id_precio").onclick = calcularPrecio;

//Vamos a mostrar al usuario si el pedido esta "Pendiente" o "Entregado" en lugar de "True" o "False"
function cambiarEstado(){
    let estado = document.getElementsByClassName("tercera");
    for(let i = 0;i<estado.length; i++){
        if (estado[i].textContent == "False"){
        estado[i].textContent = "Pendiente";
        }else if (estado[i].textContent == "True"){
            estado[i].textContent = "Entregado";
        }
    }
}



