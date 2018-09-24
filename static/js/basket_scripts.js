window.onload = function () {
    $('.checkout').on('click', 'input[type="number"]', function() {
        var t_href = event.target;
        
        $.ajax({
            url: "/basket/edit/" + t_href.name + "/" + t_href.value + "/", success: function(data) {
                $('.checkout').html(data.result);
            },
        });
        event.preventDefault();
    });
}