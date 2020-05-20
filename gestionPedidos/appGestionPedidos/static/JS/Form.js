//console.log("Funcionando")
var formulario= document.getElementById("formulario");

formulario.addEventListener('submit',function(e){
    e.preventDefault();
    console.log("CLICK")

    var datos = new FormData(formulario);
   // console.log(datos.get("cif"))
   // console.log(datos.get("nombre_empresa"))
   // console.log(datos.get("direccion"))
   // console.log(datos.get("codigo_postal"))
   // console.log(datos.get("Localidad"))
   // console.log(datos.get("Provincia"))
   // console.log(datos.get("telefono"))
   // console.log(datos.get("email"))
   // console.log(datos.get("persona_contacto"))
   var myFormData = {
    cif: datos.get('cif'),
    nombre_empresa: datos.get('nombre_empresa'),
    direccion: datos.get('direccion'),
    codigo_postal: datos.get('codigo_postal'),
    Localidad: datos.get('Localidad'),
    Provincia: datos.get('Provincia'),
    telefono: datos.get('telefono'),
    email: datos.get('email'),
    persona_contacto: datos.get('persona_contacto')
};


    for (var key in myFormData) {
      console.log(key, myFormData[key]);
      datos.append(key, myFormData[key]);
}

      fetch('http://127.0.0.1:8000/appGestionPedidos/clientes/crear/', {
      method: 'POST',
      body: datos

      })
      .then((response) =>{
      return response.json()
      })

      .then((data) => {
      console.log(data)
      })

   // datos.get('cif');
   // console.log(datos.textContent);
})


function limpiarFormulario(){
    formulario.reset();
}
let guardar = document.getElementById('guardar');
guardar.addEventListener('click', limpiarFormulario);


