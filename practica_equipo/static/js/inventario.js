console.log("Inventario JS cargado");

const buscador = document.getElementById("busqueda");

if(buscador){

buscador.addEventListener("keyup",async()=>{

const texto=buscador.value;

const respuesta=await fetch(`/inventario/buscar/?q=${texto}`);

const datos=await respuesta.json();

const tabla=document.getElementById("tablaEquipos");

tabla.innerHTML="";

datos.forEach(e=>{

tabla.innerHTML+=`

<tr>

<td>${e.codigo}</td>

<td>${e.tipo}</td>

<td>${e.marca}</td>

<td>${e.modelo}</td>

<td>${e.estado}</td>

<td>

<a class="btn btn-warning btn-sm"
href="/inventario/editar/${e.id}/">

Editar

</a>

<a class="btn btn-danger btn-sm"
href="/inventario/eliminar/${e.id}/">

Eliminar

</a>

</td>

</tr>

`;

});

});

}

document.addEventListener("mouseover",(e)=>{

if(e.target.tagName=="TD"){

e.target.style.background="#d9ecff";

}

});

document.addEventListener("mouseout",(e)=>{

if(e.target.tagName=="TD"){

e.target.style.background="";

}

});



