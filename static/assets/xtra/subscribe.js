$(document).ready(function(){
    $('#subscribenews').submit(function(event){
        event.preventDefault();
        
        $.ajax({
        url: '/subscribe',
        type: 'POST',
        data: $(this).serialize()         
        }).done(function(resp) {
            if(resp.result == 'ok') {
                alert('Thank You for Subscribing')
                $('#subscribenews').trigger("reset");
            }else {
                $('#subscribenews').trigger("reset");
                
            }
        })            
    });
});     
