$(document).ready(function(){
    $('.sendInput').attr('disabled',true);
    $('#messageInput').keyup(function(){
        if($(this).val().length !=0)
            $('.sendInput').attr('disabled', false);            
        else
            $('.sendInput').attr('disabled',true);
    })
});