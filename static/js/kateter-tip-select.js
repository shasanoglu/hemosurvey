function select_update(select){
    if(select.val()=='fistul'){
        select.closest('fieldset').find('.fistul-hide').hide();
    }else{
        select.closest('fieldset').find('.fistul-hide').show();
    }
}

$( document ).ready(function() {
    $('.tip-select').each(function(){
        select_update($( this ));
        $( this).change(function(){
            select_update($( this ));
        });
    });
});
