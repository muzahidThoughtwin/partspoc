function insertDataApi(finalCallback) {
    var eqUrl = "/equipment"
equip_type=$("#equip_type").val();
title= $("#title").val();
name= $("#name").val();
description= $("#description").val();

    description = encodeURIComponent(description);
    var dataString = 'equip_type=' + equip_type + '&title=' + title + '&name=' + name+ '&description=' + description ;
    ajaxWithHeader('POST', dataString, eqUrl , 'render', finalCallback);

}

function getApiResponse(data){
    var messageSuccess = data.data.message;
    alert('Information inserted successfully');
}

