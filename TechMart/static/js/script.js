document.addEventListener("DOMContentLoaded", function () {
    const API_URL = "http://127.0.0.1:5000/productos";
    const productList = document.getElementById("productList");
    
    // Elementos del modal
    const editModal = document.getElementById("editModal");
    const closeModal = document.querySelector(".close");
    const editForm = document.getElementById("editForm");
    const cancelEdit = document.getElementById("cancelEdit");

    // Campos del modal
    const editId = document.getElementById("editId");
    const editNombre = document.getElementById("editNombre");
    const editDescripcion = document.getElementById("editDescripcion");
    const editPrecio = document.getElementById("editPrecio");
    const editStock = document.getElementById("editStock");

    // Cargar productos
    fetchProducts();

    function fetchProducts() {
        fetch(API_URL)
            .then(response => response.json())
            .then(data => {
                productList.innerHTML = "";
                data.forEach(product => {
                    const row = document.createElement("tr");
                    row.innerHTML = `
                        <td>${product.nombre}</td>
                        <td>${product.descripcion}</td>
                        <td>$${product.precio}</td>
                        <td>${product.stock}</td>
                        <td>
                            <button class="edit-btn" onclick="editProduct(${product.id}, '${product.nombre}', '${product.descripcion}', ${product.precio}, ${product.stock})">
                                <i class="fa-solid fa-pen-to-square"></i>
                            </button>
                            <button class="delete-btn" onclick="deleteProduct(${product.id})">
                                <i class="fa-solid fa-trash"></i>
                            </button>
                        </td>
                    `;
                    productList.appendChild(row);
                });
            })
            .catch(error => console.error("Error al obtener productos:", error));
    }

    // Mostrar el modal con los datos del producto
    window.editProduct = function (id, nombre, descripcion, precio, stock) {
        editId.value = id;
        editNombre.value = nombre;
        editDescripcion.value = descripcion;
        editPrecio.value = precio;
        editStock.value = stock;
        editModal.style.display = "flex";
    };

    // Cerrar el modal al hacer clic en "Cancelar" o en la "X"
    cancelEdit.addEventListener("click", function () {
        editModal.style.display = "none";
    });

    closeModal.addEventListener("click", function () {
        editModal.style.display = "none";
    });

    // Actualizar el producto al enviar el formulario del modal
    editForm.addEventListener("submit", function (event) {
        event.preventDefault();
        const id = editId.value;

        fetch(`${API_URL}/${id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                nombre: editNombre.value,
                descripcion: editDescripcion.value,
                precio: parseFloat(editPrecio.value),
                stock: parseInt(editStock.value),
            }),
        })
        .then(response => response.json())
        .then(data => {
            console.log("Producto actualizado:", data);
            fetchProducts(); // Recargar lista de productos
            editModal.style.display = "none"; // Cerrar modal
        })
        .catch(error => console.error("Error al actualizar producto:", error));
    });

    // Eliminar producto
    window.deleteProduct = function (id) {
        fetch(`${API_URL}/${id}`, {
            method: "DELETE",
        })
        .then(response => response.json())
        .then(data => {
            console.log("Producto eliminado:", data);
            fetchProducts();
        })
        .catch(error => console.error("Error al eliminar producto:", error));
    };
});



