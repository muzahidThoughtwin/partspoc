$(document).ready(function() {
    // data = 'pageSize=' + '-1'+'&phase_cat=' + '3' ;
    ajaxWithHeader('GET', null, '/equipment', 'render', 'setEquipment','#equipment');
    ajaxWithHeader('GET', null, '/make', 'render', 'setSelect','#make');
    ajaxWithHeader('GET', null, '/built', 'render', 'setBuilt','#built');
    ajaxWithHeader('GET', null, '/partstype', 'render', 'setPartsType','#partstype');
});

function setEquipment(data,appender){
 
    $(appender).empty();
    $(appender).append("<option value=''>Choose...</option>");
    $.each(data.data.result, function (index, result) {
        $(appender).append("<option value='" + result.id + "'>" + (result.title?result.title:result.name) + "</option>");
        
    });    
}

function setSelect(data,appender){
 
    $(appender).empty();
    $(appender).append("<option value=''>Choose...</option>");
    $.each(data.data.result, function (index, result) {
        $(appender).append("<option value='" + result.id + "'>" + (result.title?result.title:result.name) + "</option>");
        
    });    
}

function setBuilt(data,appender){
 
    $(appender).empty();
    $(appender).append("<option value=''>Choose...</option>");
    $.each(data.data.result, function (index, result) {
        $(appender).append("<option value='" + result.id + "'>" + (result.title?result.title:result.name) + "</option>");
        
    });    
}
function setPartsType(data,appender){
 
    $(appender).empty();
    $(appender).append("<option value=''>Choose...</option>");
    $.each(data.data.result, function (index, result) {
        $(appender).append("<option value='" + result.id + "'>" + (result.title?result.title:result.name) + "</option>");
        
    });    
}

function insertDataApi(finalCallback) {
var makeUrl = "/partsname"

equipment=$("#equipment").val();
make=$("#make").val();
built=$("#built").val();
partstype=$("#partstype").val();
title= $("#title").val();
name= $("#name").val();
description= $("#description").val();
    description = encodeURIComponent(description);
    var dataString = 'equipment_id='+ equipment +'&make='+ make + '&built='+built+'&parts_type='+ partstype +'&title=' + title + '&name=' + name+ '&description=' + description ;
    ajaxWithHeader('POST', dataString, makeUrl , 'render', finalCallback);

}

function getApiResponse(data){
    var messageSuccess = data.data.message;
    alert('Information inserted successfully');
}