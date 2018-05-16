var a = 0

$(document).ready(function() {
    ajaxWithHeader('GET', null, '/make', 'render', 'setMake','#make');
    ajaxWithHeader('GET', null, '/built', 'render', 'setBuilt','#model');
});



function setMake(data,appender){
    
    $(appender).empty();
    $(appender).append("<option value=''>Choose...</option>");
    $.each(data.data.result, function (index, result) {
        // console.log(result);
        $(appender).append("<option makeid='"+ result.id +"' value='" + (result.title?result.title:result.name) + "'></option>");
        
    });    
}

function setBuilt(data,appender){
 
    $(appender).empty();
    $(appender).append("<option value=''>Choose...</option>");
    $.each(data.data.result, function (index, result) {
        $(appender).append("<option modelid='"+ result.id +"' value='" + (result.title?result.title:result.name) + "'></option>");   
    });    
}



$(document).on('change', '#makeId', function() {
    var makeval=$("#make option[value='" + $('#makeId').val() + "']").attr('makeid');
    // alert(makeval);
    ajaxWithHeader('GET', null, '/make/'+ makeval, 'render', 'setMakeNext','next');

    });    
// }

    function setMakeNext(data,appender){
        // alert($("#make").val());
    // console.log(data.data.result.make_type);
   if(data.data.result.make_type=='MODEL' || 'Model'){
  
    $("#next").append('<span>&nbsp;' + data.data.result.make_type +'&nbsp;</span>');
     ajaxWithHeader('GET', null, '/built?make='+ $("#make").val()+'&level=0', 'render', 'setNext',null);
  
}
}


function setNext(data){
    a = a+1 ;
    // console.log(data.data.result);
    s ='<input type="text" id="step'+a+'" list="model" placeholder="Choose Model">';
    s += '<datalist' + ' id="step'+a+'"'+ 'onchange="jsFunction(step'+a+')"' +'>';
    s += '<option>' + 'Choose....'+'</option>';
    for(i=0;i<data.data.result.length;i++){
        // console.log(data.data.result[i].make);
        var makeid=data.data.result[i].make;
       s += setSelect(data.data.result[i],makeid);
    }
    s += '</datalist>'
    $("#next").append(s);
    ss='&nbsp;&nbsp;<label> Serial </label>&nbsp;&nbsp;<input type="text" id="serial" list="serial" placeholder="Serial Number"><datalist id="serial" name="serial"><option value="">Select</option></datalist>';
    $("#next").append(ss);

}


// function setNext(data){
//     a = a+1 ;
//     // console.log(data.data.result);
//     s = '<select' + ' id="step'+a+'"'+ 'onchange="jsFunction(step'+a+')"' +'>';
//     s += '<option>' + 'Choose....'+'</option>';
//     for(i=0;i<data.data.result.length;i++){
//         // console.log(data.data.result[i].make);
//         var makeid=data.data.result[i].make;
//        s += setSelect(data.data.result[i],makeid);
//     }
//     s += '</select>'
//     $("#next").append(s);

// }
function setSelect(title,makeid, attrId){
    // console.log(makeid);

    return '<option'+ ' value='+ title.id   +'>' + title.title +'</option>';
}

// function jsFunction(val){
//     alert(val);
//     val = $("#"+val).val();
//     alert(val);
//     // $("#next").append('<span>&nbsp;' + data.data.result.make_type +'&nbsp;</span>');
//     ajaxWithHeader('GET', null, '/built?parent_id='+ val+'&level=1', 'render', 'setNextmodal', null);
// }
// function setNextmodal(data){
//     if(data.data.result.length > 0){
//         a = a+1 ;
//         // console.log(data.data.result);
//         s = '<select' + ' id="step'+a+'"'  + 'onchange="jsFunction(step'+a+')"' +'>';
//         s += '<option>' + 'Choose....'+'</option>';
//         for(i=0;i<data.data.result.length;i++){
//             // console.log(data.data.result[i].make);
//             var makeid=data.data.result[i].make;
//            s += setSelect(data.data.result[i],makeid, a+1);
//         }
//         s += '</select>'

//         $(".form-area").append(s);
//     }

// }




// $(document).on('change', '#makeId', function() {
//  alert($("#make option[value='" + $('#makeId').val() + "']").attr('makeid'));

// });



// $(document).on('change','#modelId', function() {

//  alert($("#model option[value='" + $('#modelId').val() + "']").attr('modelid'));
// });



function insertId(){
  var makeid=  $("#make option[value='" + $('#makeId').val() + "']").attr('value');
var modelid= $("#model option[value='" + $('#step'+a).val() + "']").attr('value');
// window.location.href="http://search-2";
// window.location = "search-2";
// $(location).attr('href', 'http://stackoverflow.com')
// alert("1");
window.location.href = 'search-2?make='+makeid+'&model='+ modelid +'';
// window.location.replace('http://sidanmor.com');
}
