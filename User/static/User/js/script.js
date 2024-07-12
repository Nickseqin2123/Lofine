const openModal = document.querySelector('.open-modal');
const modal = document.querySelector('.modal');
const closeBtn = document.querySelector('.close');

openModal.addEventListener('click', function() {
    modal.style.display = 'block';
});

closeBtn.addEventListener('click', function() {
    modal.style.display = 'none';
});

window.addEventListener('click', function(event) {
    if (event.target === modal) {
        modal.style.display = 'none';
    }
});