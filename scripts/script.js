
function toggleClass(element) {
    button = element.target;
    if (button.className.indexOf('free') >= 0) return;
    if (button.className.indexOf('checked') >= 0) {
        button.className = 'btn';
    } else {
        button.className += ' checked';
    }
    if (done()) alert('BINGO!');
}

[].forEach.call(document.getElementsByTagName('td'), function(btn) {
    btn.addEventListener('click', toggleClass);
});


//plz dont look at this fnctn it's mad unoptimized
function done() {
    //horizontal
    for (var i=0; i < 5; i++) {
        cnt = 0;
        for (var j=0; j < 5; j++) {
            cnt += document.getElementById(i+','+j).className.indexOf('checked') >= 0 ? 1 : 0;
        }
        if (cnt == 5) {
            return true;
        }
    }
    //vertical
    for (var i=0; i < 5; i++) {
        cnt = 0;
        for (var j=0; j < 5; j++) {
            cnt += document.getElementById(j+','+i).className.indexOf('checked') >= 0 ? 1 : 0;
        }
        if (cnt == 5) {
            return true;
        }
    }
    //topleft to bottomright diag
    cnt = 0;
    for (var i=0; i < 5; i++) {
        cnt += (document.getElementById(i+','+i).className.indexOf('checked') >= 0) ? 1 : 0; 
        if (cnt == 5) {
            return true;
        }
    }
    //topright to bottomleft diag
    cnt = 0;
    for (var i=0; i < 5; i++) {
        cnt += document.getElementById(i+','+(4-i)).className.indexOf('checked') >= 0 ? 1 : 0; 
        if (cnt == 5) {
            return true;
        }
    }
}

