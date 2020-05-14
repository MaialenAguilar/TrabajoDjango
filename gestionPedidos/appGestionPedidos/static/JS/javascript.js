function calcularPrecio(){

    let base_imponible = document.getElementById("id_base_imponible").value;
    let iva = document.getElementById("id_iva").value;
    document.getElementById("id_precio").value = base_imponible*(1+ iva/100);

}
let precio = document.getElementById("id_precio");
precio.onclick = calcularPrecio;
