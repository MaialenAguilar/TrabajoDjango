//Cálculo del precio total en el formulario del pedido
function calcularPrecio(){

    let base_imponible = document.getElementById("id_base_imponible").value;
    let iva = document.getElementById("id_iva").value;
    document.getElementById("id_precio").value = base_imponible*(1+ iva/100);

}


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
//Creamos una función para que el usuario pueda filtrar si quiere ver los pedidos Pendientes, Entregados o Todos
function mostrar () {
    var im = document.getElementById('imostrar').value;
    var datos = document.getElementsByClassName('dato');
    var todos = 'Todos';
    if(im!='')
      for (var i = 0; i < datos.length; i ++)
        if(datos[i].textContent.indexOf(im)>-1) //retorna el primer índice en el que se puede encontrar un elemento dado en el array, ó retorna -1 si el elemento no esta presente.
          datos[i].style.display="block";
        else if (im == todos)
          datos[i].style.display="block";

        else
          datos[i].style.display="none";
}

