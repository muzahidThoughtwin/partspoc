$(document).ready(function() {
	var urls = $(location).attr('href'),
    value = urls.split("/"),
    last_id = value[value.length-1];
    ajaxWithHeader('GET', null, '/partsdetail/'+last_id, 'render', 'setPartsAllDetails','#partsdetail');
});


function setPartsAllDetails(data,appender){
   console.log(data.data.result);
   // var trHTML = '';
$('#image').html('<img style="max-width:100%;" height="200px" src=/static/'+data.data.result.image+'>');
document.getElementById('title').innerHTML = data.data.result.title;
document.getElementById('price').innerHTML = data.data.result.price;
document.getElementById('ref').innerHTML = data.data.result.ref;
document.getElementById('remarks').innerHTML = data.data.result.remarks;
document.getElementById('fuel').innerHTML = data.data.result.fuel;
   }

