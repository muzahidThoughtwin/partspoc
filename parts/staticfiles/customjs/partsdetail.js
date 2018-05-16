function insertDataApi(finalCallback) {
var partsDetailUrl = "/partsdetail";
built=$("#built").val();
make=$("#make").val();
parts_type=$("#partstype").val();
parts_name=$("#partsname").val();
title= $("#title").val();
name= $("#name").val();
description = $("#description").val();
ref = $("#ref").val();
code = $("#code").val();
part = $("#part").val();
slp = $("#slp").val();
quantity = $("#quantity").val();
specifications = $("#specifications").val();
remarks = $("#remarks").val();
serial = $("#serial").val();
date = $("#date").val();
fuel = $("#fuel").val();
engine = $("#engine").val();
image = $("#image").val();

    description = encodeURIComponent(description);
    var dataString = 'make=' + make + "&built=" + built + "&parts_type=" + parts_type + "&parts_name=" + parts_name +'&title=' + title + '&name=' + name+ '&description=' + description + "&ref=" + ref + "&code=" + code + "&part=" + part + "&slp=" + slp + "&qty=" + quantity + "&spec=" + specifications + "&remarks=" + remarks + "&serial=" + serial + "&date=" + date + "&fuel=" + fuel + "&engine=" + engine +  "&image=" + image ;
    ajaxWithHeader('POST', dataString, partsDetailUrl , 'render', finalCallback);

}

function getApiResponse(data){
    var messageSuccess = data.data.message;
    alert('Information inserted successfully');
}


$(document).ready(function() {
    // data = 'pageSize=' + '-1'+'&phase_cat=' + '3' ;
    ajaxWithHeader('GET', null, '/make', 'render', 'setSelect','#make');
    ajaxWithHeader('GET', null, '/built', 'render', 'setBuilt','#built');
    ajaxWithHeader('GET', null, '/partstype', 'render', 'setPartsType','#parts_type');
    ajaxWithHeader('GET', null, '/partsname', 'render', 'setPartsName','#parts_name');
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

function setBuild(data,appender){
 
    $(appender).empty();
    $(appender).append("<option value=''>Choose...</option>");
    $.each(data.data.result, function (index, result) {
        $(appender).append("<option value='" + result.id + "'>" + (result.title?result.title:result.name) + "</option>");
        
    });    
}
function setPartsName(data,appender){
 
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