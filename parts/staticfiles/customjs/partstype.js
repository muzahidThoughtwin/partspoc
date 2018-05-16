$(document).ready(function() {
    // data = 'pageSize=' + '-1'+'&phase_cat=' + '3' ;
    ajaxWithHeader('GET', null, '/make', 'render', 'setSelect','#make');
    ajaxWithHeader('GET', null, '/built', 'render', 'setBuilt','#built');
});

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

function insertDataApi(finalCallback) {
var makeUrl = "/partstype"

make=$("#make").val();
built=$("#built").val();
title= $("#title").val();
name= $("#name").val();
description= $("#description").val();
    description = encodeURIComponent(description);
    var dataString = 'make='+ make + '&built='+built+'&title=' + title + '&name=' + name+ '&description=' + description ;
    ajaxWithHeader('POST', dataString, makeUrl , 'render', finalCallback);

}

function getApiResponse(data){
    var messageSuccess = data.data.message;
    alert('Information inserted successfully');
}