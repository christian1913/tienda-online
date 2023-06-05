document.addEventListener("DOMContentLoaded", function() {
    var activeModal = undefined;

    window.toggleModal = function(modalId) {
        var modal = document.getElementById(modalId);
        if (modal) { // comprobamos que el modal existe antes de acceder a su propiedad style
            if (activeModal === undefined) {
                activeModal = modal;
                activeModal.style.display = "flex";
            } else if (activeModal.style.display === "flex" && activeModal.id == modalId) {
                activeModal.style.display = "none";
                activeModal = undefined;
            }
        } else {
            console.error('Modal with id ' + modalId + ' not found');
        }
    }

    window.onclick = function(event) {
        if (event.target == activeModal) {
            activeModal.style.display = "none";
            activeModal = undefined;
        }
    }
});