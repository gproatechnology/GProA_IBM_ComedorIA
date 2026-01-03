// app/static/js/kiosk.js
// JavaScript para renderizar dinámicamente los menús del kiosk

async function loadMenus() {
    try {
        const response = await fetch('/api/menu/');
        if (!response.ok) {
            throw new Error('Error al cargar menús');
        }
        const menus = await response.json();
        const menuList = document.getElementById('menu-list');
        menuList.innerHTML = menus.map(menu => `
            <div class="menu-item">
                <h3>${menu.name}</h3>
                <p>${menu.description}</p>
                <p>Precio: $${menu.price}</p>
                <button class="btn-primary">Seleccionar</button>
            </div>
        `).join('');
    } catch (error) {
        const menuList = document.getElementById('menu-list');
        menuList.innerHTML = '<p>Error al cargar los menús. Inténtalo de nuevo.</p>';
    }
}

// Cargar menús al iniciar
loadMenus();