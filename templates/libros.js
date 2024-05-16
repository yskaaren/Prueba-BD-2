let botonesEditar = document.querySelectorAll("#editar-libro");
let formulario = document.getElementById("agregar_libro");

function llenarFormulario(
  idLibro,
  tituloLibro,
  idAutor,
  precioLibro,
  stockLibro
) {
  let id_libro_input = document.getElementById("id_libro_input");
  let titulo_input = document.getElementById("titulo_input");
  let id_autor_input = document.getElementById("id_autor_input");
  let precio_input = document.getElementById("precio_input");
  let stock_input = document.getElementById("stock_input");

  id_libro_input = id_libro_input.value = idLibro;
  titulo_input = titulo_input.value = tituloLibro;
  id_autor_input = id_autor_input.value = idAutor;
  precio_input = precio_input.value = precioLibro;
  stock_input = stock_input.value = stockLibro;
}

botonesEditar.forEach(function (boton) {
  boton.addEventListener("click", function (event) {
    let elementoLibro = event.target.closest("li");

    let idLibro = elementoLibro.querySelector('label[id="id_libro"]');
    let tituloLibro = elementoLibro.querySelector('label[id="titulo"]');
    let idAutor = elementoLibro.querySelector('label[id="autor_id"]');
    let precioLibro = elementoLibro.querySelector('label[id="precio"]');
    let stockLibro = elementoLibro.querySelector('label[id="stock"]');

    llenarFormulario(
      idLibro.textContent,
      tituloLibro.textContent,
      idAutor.textContent,
      precioLibro.textContent,
      stockLibro.textContent
    );
  });
});
