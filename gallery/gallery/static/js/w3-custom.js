// custom.js

var alertDelay = 3000;
window.setTimeout(function() {$('div.alert').fadeTo(500, 0).slideUp(500, function(){ $(this).remove(); });}, alertDelay);


w3_alert = function(message, bgc, timeout, classname) {
    var bg = (typeof bgc === 'undefined') ?  'w3-blue': bgc;
    var cls = (typeof classname === 'undefined') ?  '': classname;
    var html = '<div class="p-1 alert '+ bg +' '+ cls +' " style="min-width:300px;">' +
                '<span onclick="this.parentElement.style.display=\'none\'" class="w3-button w3-right">&times;</span><h5>'+message+'</h5>' +
               '</div>'
    $('#flash-message-placeholder').append(html);

    if (timeout < 0) timeout = 3600*1000;
    if (timeout == 0) timeout = 1000;

    window.setTimeout(function() {
        $('div.alert').fadeTo(500, 0).slideUp(500, function() {
            $(this).remove();
        });
    }, timeout);
};