$(document).ready(function() {
    ajaxWithHeader('GET', null, '/partstype', 'render', 'setPartsType1','#demoTree');
    // ajaxWithHeader('GET', null, '/partsname', 'render', 'setPartsName','#partsname');
});



function setPartsType1(data,appender){
    console.log(data.data.result);
    s = '<ul id="demoTree">';
    $.each(data.data.result, function (index, result) {
        console.log(result.parts_name);
    s += '<li id="partsid"><span class="stm-icon"></span>+<span class="stm-content" value='+ result.id +'>'+  (result.title?result.title:result.name) + '</span>';
        
        s += '<ul>';
        $.each(result.parts_name, function (index, parts_name) {
            
            s += '<li id="partsid">-<span class="stm-icon"></span><span class="stm-content" value='+ parts_name.id +' onclick="getpartdetail('+ parts_name.id +')">'+  (parts_name.title?parts_name.title:parts_name.name) + '</span>';
            s += '</li>'
        });    
        s += '</ul>';
    s += '</li>'
  
    });
    s += '</ul>'
    $("#Tree").append(s); 
    $('#demoTree').simpleTreeMenu();
   
}


function getpartdetail(id){
    // alert(id);

    ajaxWithHeader('GET', null, '/partsdetail?parts_name='+id, 'render', 'setPartsDetails','#details');
}



function setPartsDetails(data,appender){
   console.log(data.data.result[0].id);
   var trHTML = '';
// var imgg= $('#image').html('<img src=/static/'+data.data.result.image+'>');
for(i=0;i<data.data.result.length;i++){


   trHTML +=
                                      
                                      '<tr><td>'
                                      + '<a href="partsdetail/view/' + data.data.result[i].id + '"><img class="img-responsive" height="50px" width="95px" src=/static/'+data.data.result[i].image+'></a>'
                                      + '</td><td>'
                                      + data.data.result[i].code
                                      + '</td><td>'
                                      + data.data.result[i].ref
                                      + '</td><td>'
                                      + data.data.result[i].part
                                      + '</td><td>'
                                      + data.data.result[i].qty
                                      + '</td><td>'
                                      + data.data.result[i].description
                                      + '</td></tr>';



   // $("#image").append(data.data.result.image);
   // $("#code").append(data.data.result.code);
   // $("#ref").append(data.data.result.ref); 
   // $("#partnumber").append(data.data.result.part); 
   // $("#qty").append(data.data.result.qty); 
   // $("#description").append(data.data.result.description); 
   }
   $( ".table-bordered" ).removeClass( "dataTable" );

   $('#tBody').append(trHTML);
}

$(document).ready(function() {

// var url = new URL(url_string);
// var c = url.searchParams.get("make");
// alert(url);

  var urls = window.location.href;
  var myurls = urls.split("?make=");
  var myurlss  = urls.split("&model=");


  var mylasturls = myurls[1];
    
  var mylasturlss = myurlss[1];

  var mynexturls = mylasturls.split("&");
  var mynexturlss = mylasturlss.split("&");
  var url = mynexturls[0];
  var urls = mynexturls[1];
// urls.replace('=','--');
var modelidd = urls.replace('model=','');
 document.getElementById("showmake").innerHTML = url;
 document.getElementById("showmodel").innerHTML = modelidd;


});