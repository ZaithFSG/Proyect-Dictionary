async function buscar() {
  const palabra = document.getElementById("palabra").value;
  const resultadoDiv = document.getElementById("resultado");

  if (!palabra) {
    resultadoDiv.innerHTML = "<p>Por favor ingresa una palabra</p>";
    return;
  }

  resultadoDiv.innerHTML = "<p>Buscando...</p>";

  try {
    const response = await fetch(
      `/definir?palabra=${encodeURIComponent(palabra)}`
    );
    const data = await response.json();

    if (data.error) {
      resultadoDiv.innerHTML = `<p class="error">${data.error}</p>`;
    } else {
      resultadoDiv.innerHTML = `
                        <h3>${data.palabra}</h3>
                        <p>${data.definicion}</p>
                    `;
    }
  } catch (error) {
    resultadoDiv.innerHTML = `<p class="error">Error al conectar con el servidor</p>`;
  }
}
