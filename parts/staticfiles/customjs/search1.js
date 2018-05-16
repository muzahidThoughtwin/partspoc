$(document).ready(function() {
    ajaxWithHeader('GET', null, '/partstype', 'render', 'setPartsType1','#partstype1');
    ajaxWithHeader('GET', null, '/partsname', 'render', 'setPartsName','#partsname');
});



function setPartsType1(data,appender){
    console.log(data.data.result);
    $(appender).empty();
    $(appender).append("<ol></ol>");
    // $(appender).append("<option value=''>Choose...</option>");
    $.each(data.data.result, function (index, result) {
    $(appender).append("<li value=''><a href='http://127.0.0.1:8000/partstype/"+ result.id +"'>" + (result.title?result.title:result.name) + "</a></li>");
    for(i=0;i<data.data.result.length;i++){
    $(appender).append("<p value=''>" + data.data.result[i].parts_name[i].name[i] + "</p>");
        }
    });    
}
function setPartsName(data,appender){

    $(appender).empty();
    $(appender).append("<ol></ol>");
    $.each(data.data.result, function (index, result) {
        $(appender).append("<li value=''>" + (result.title?result.title:result.name) + "</li>");
        
    });    
}

// function setPartsDetail(data,appender){
//     console.log(data);
//     $(appender).empty();
//     $(appender).append("<ol></ol>");
//     $.each(data.data.result, function (index, result) {
//         $(appender).append("<li value=''>" + (result.title?result.title:result.name) + "</li>");
        
//     });    
// }

