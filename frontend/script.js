const API = "https://api-inventario-final.onrender.com/devices";

// Cargar datos
async function cargarDispositivos() {
  try {
    const res = await fetch(API);
    const data = await res.json();

    const lista = document.getElementById("lista");
    lista.innerHTML = "";

    data.forEach(d => {
      lista.innerHTML += `
        <tr>
          <td>${d.id}</td>
          <td>${d.nombre}</td>
          <td>${d.tipo}</td>
          <td>${d.estado}</td>
          <td>${d.area}</td>
          <td>
            <button onclick="eliminar(${d.id})">Eliminar</button>
          </td>
        </tr>
      `;
    });

  } catch (error) {
    console.error("Error:", error);
  }
}

// Agregar
async function agregar() {
  const nombre = document.getElementById("nombre").value;
  const tipo = document.getElementById("tipo").value;
  const estado = document.getElementById("estado").value;
  const area = document.getElementById("area").value;

  if (!nombre || !tipo || !estado || !area) {
    alert("Completa todos los campos");
    return;
  }

  await fetch(API, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ nombre, tipo, estado, area })
  });

  limpiarCampos();
  cargarDispositivos();
}

// Eliminar
async function eliminar(id) {
  await fetch(`${API}/${id}`, {
    method: "DELETE"
  });

  cargarDispositivos();
}

// Limpiar inputs
function limpiarCampos() {
  document.getElementById("nombre").value = "";
  document.getElementById("tipo").value = "";
  document.getElementById("estado").value = "";
  document.getElementById("area").value = "";
}

// Cargar al iniciar
cargarDispositivos();