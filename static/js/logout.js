let redirect = () => {
    window.location = window.next;
};

window.redirect = redirect;
window.onload = window.redirect;
setTimeout(window.redirect, 1000 * 20);
