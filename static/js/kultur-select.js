function kultur_update(select){
    if(select.prop('checked')){
        select.closest('div.row').find('.kultur-hide').show();
    }else{
        select.closest('div.row').find('.kultur-hide').hide();
    }
}

$( document ).ready(function() {
    $('.kultur-select').each(function(){
        kultur_update($( this ));
        $( this).change(function(){
            kultur_update($( this ));
        });
    });
});
