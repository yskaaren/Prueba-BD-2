let botonesEditar = document.querySelectorAll("#editar-autor");
let formulario = document.getElementById("agregar_autor");

function llenarFormulario(
  idAutor,
  nombreAutor,
  nacionalidad
) {
  let id_autor_input = document.getElementById("id_autor_input");
  let nombre_autor_input = document.getElementById("nombre_autor_input");
  let nacionalidad_input = document.getElementById("nacionalidad_input");

  id_autor_input = id_autor_input.value = idAutor;
  nombre_autor_input = nombre_autor_input.value = nombreAutor;
  nacionalidad_input = nacionalidad_input.value = nacionalidad;
}

botonesEditar.forEach(function (boton) {
  boton.addEventListener("click", function (event) {
    let elementoAutor = event.target.closest("li");

    let idAutor = elementoAutor.querySelector('label[id="idAutor"]');
    let nombreAutor = elementoAutor.querySelector('label[id="nombreAutor"]');
    let nacionalidad = elementoAutor.querySelector('label[id="nacionalidad"]');

    llenarFormulario(
        idAutor.textContent,
        nombreAutor.textContent,
        nacionalidad.textContent,
    );
  });
});
