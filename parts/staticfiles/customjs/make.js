function insertDataApi(finalCallback) {
var makeUrl = "/make"
// equipment=$("#equipment").val();
make_type=$("#type").val();
title= $("#title").val();
name= $("#name").val();
description= $("#description").val();

    description = encodeURIComponent(description);
    var dataString = '&make_type=' + make_type + '&title=' + title + '&name=' + name+ '&description=' + description ;
    ajaxWithHeader('POST', dataString, makeUrl , 'render', finalCallback);

}

function getApiResponse(data){
    var messageSuccess = data.data.message;
    alert('Information inserted successfully');
}

// $(document).ready(function() {
//     // data = 'pageSize=' + '-1'+'&phase_cat=' + '3' ;
//     ajaxWithHeader('GET', null, '/equipment', 'render', 'setSelect','#equipment');
// });

// function setSelect(data,appender){
 
//     $(appender).empty();
//     $(appender).append("<option value=''>Choose...</option>");
//     $.each(data.data.result, function (index, result) {
//         $(appender).append("<option value='" + result.id + "'>" + (result.title?result.title:result.name) + "</option>");
        
//     });    
// }

