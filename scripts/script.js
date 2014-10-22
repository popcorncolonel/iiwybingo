
function toggleClass(element) {
    button = element.target;
    if (button.className.indexOf('checked') >= 0) {
        button.className = 'btn';
    } else {
        button.className += ' checked';
    }
}

[].forEach.call(document.getElementsByTagName('td'), function(btn) {
    btn.addEventListener('click', toggleClass);
});

