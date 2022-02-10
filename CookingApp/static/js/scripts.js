/*!
* Start Bootstrap - Heroic Features v5.0.4 (https://startbootstrap.com/template/heroic-features)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-heroic-features/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

function mark(id) {
    if (document.getElementById(id).className == ("list-group-item d-flex list-group-item-secondary")) {
        document.getElementById(id).className += " bg-transparent";
        document.getElementById(id).className = document.getElementById(id).className.replace( /(?:^|\s)list-group-item-secondary(?!\S)/g , '' );
    }
    else {
        document.getElementById(id).className += " list-group-item-secondary";
        document.getElementById(id).className = document.getElementById(id).className.replace( /(?:^|\s)bg-transparent(?!\S)/g , '' )
    }
}

function quote() {
    const list = ["My one and only", "My sweetheart", "Love of my life", "My Abigail", "Honey bunny", "My honey bunches of oats", "You are mine"]

    const random = Math.floor(Math.random() * list.length);
    console.log(random, list[random]);
    
    document.getElementById("love").innerHTML = list[random];
}

function locationreload() {
    document.location.reload();
}

document.addEventListener("DOMContentLoaded", function(event) { 
    var scrollpos = localStorage.getItem('scrollpos');
    if (scrollpos) window.scrollTo({top: scrollpos,left: 0,behavior: 'instant'});
});
window.onbeforeunload = function(e) {
    localStorage.setItem('scrollpos', window.scrollY);
};

if ( window.history.replaceState ) {
    window.history.replaceState( null, null, window.location.href );
}