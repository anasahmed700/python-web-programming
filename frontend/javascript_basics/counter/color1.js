document.addEventListener('DOMContentLoaded', () => {
    // change the color when dropdown changes
    document.querySelector('#change-color').onchange = function() {
        document.querySelector('#bye').style.color = this.value;
    };
});