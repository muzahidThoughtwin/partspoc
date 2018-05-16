function insertDataApi(finalCallback) {
var makeUrl = "/built"
equipment=$("#equipment").val();
make=$("#make").val();
title= $("#title").val();
level= $("#level").val();
name= $("#name").val();
description= $("#description").val();
is_last= $("#isLast").val();
parent= $("#parent").val();
    description = encodeURIComponent(description);
    var dataString = 'equipment_id='+ equipment +'&make='+ make + '&level=' + level+ '&title=' + title + '&name=' + name+ '&description=' + description +'&is_last=' + is_last +'&parent=' + parent ;
    ajaxWithHeader('POST', dataString, makeUrl , 'render', finalCallback);

}

function getApiResponse(data){
    var messageSuccess = data.data.message;
    alert('Information inserted successfully');
}

$(document).ready(function() {
    // data = 'pageSize=' + '-1'+'&phase_cat=' + '3' ;
    ajaxWithHeader('GET', null, '/equipment', 'render', 'setEquipment','#equipment');
    ajaxWithHeader('GET', null, '/make', 'render', 'setSelect','#make');
});



$(document).on('change', '#isLast', function() {
    // data = 'pageSize=' + '-1'+'&phase_cat=' + '3' ;
    if($("#isLast option:selected").val() == 0){
        ajaxWithHeader('GET', null, '/built', 'render', 'selectModel','#parent');
    }
});





function setSelect(data,appender){
 
    $(appender).empty();
    $(appender).append("<option value=''>Choose...</option>");
    $.each(data.data.result, function (index, result) {
        $(appender).append("<option value='" + result.id + "'>" + (result.title?result.title:result.name) + "</option>");
        
    });    
}
function setEquipment(data,appender){
 
    $(appender).empty();
    $(appender).append("<option value=''>Choose...</option>");
    $.each(data.data.result, function (index, result) {
        $(appender).append("<option value='" + result.id + "'>" + (result.title?result.title:result.name) + "</option>");
        
    });    
}
function selectModel(data,appender){
 
    $(appender).empty();
    $(appender).append("<option value=''>Choose...</option>");
    $.each(data.data.result, function (index, result) {
        $(appender).append("<option value='" + result.id + "'>" + (result.title?result.title:result.name) + "</option>");
        
    });    
}

function setParent(){
    ajaxWithHeader('GET', null, '/built', 'render', 'setSelect','#make');
}
