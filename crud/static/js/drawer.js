// Initialize drawer component
document.addEventListener('DOMContentLoaded', function() {
    // Get the drawer toggle button and drawer element
    const drawerToggle = document.querySelector('[data-drawer-toggle="logo-sidebar"]');
    const drawer = document.getElementById('logo-sidebar');

    if (drawerToggle && drawer) {
        drawerToggle.addEventListener('click', function() {
            // Toggle the translate class to show/hide the drawer
            drawer.classList.toggle('-translate-x-full');
        });
    }
}); 