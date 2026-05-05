const abrir = document.getElementById("abrirScanner");

abrir.onclick = () => {
    window.open("/scanner", "_blank", "width=400,height=500");
};

function cargarProductos() {
    fetch("/productos")
    .then(res => res.json())
    .then(data => {
        const tabla = document.getElementById("tablaProductos");
        tabla.innerHTML = "";

        data.forEach((codigo, i) => {
            tabla.innerHTML += `
                <tr>
                    <td>${i+1}</td>
                    <td>${codigo}</td>
                    <td><button onclick="eliminar('${codigo}')">❌</button></td>
                </tr>
            `;
        });
    });
}

setInterval(cargarProductos, 1000);

function eliminar(codigo) {
    fetch("/eliminar", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({codigo})
    });
}

function limpiarLista() {
    fetch("/limpiar", {method: "POST"});
}