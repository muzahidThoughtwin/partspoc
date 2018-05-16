var a = 0

$(document).ready(function() {
    // data = 'pageSize=' + '-1'+'&phase_cat=' + '3' ;

    ajaxWithHeader('GET', null, '/make', 'render', 'setMake','#make');
});

function setMake(data,appender){
 
    $(appender).empty();
    $(appender).append("<option value=''>Choose...</option>");
    $.each(data.data.result, function (index, result) {
        // console.log(result);
        $(appender).append("<option value='" + result.id + "'>" + (result.title?result.title:result.name) + "</option>");
        
    });    
}


$(document).on('change', '#make', function() {
    var makeval=$("#make").val();
    
    ajaxWithHeader('GET', null, '/make/'+ makeval, 'render', 'setMakeNext','next');

    });    
// }

    function setMakeNext(data,appender){
        // alert($("#make").val());
    // console.log(data.data);
   // if(data.data.result.make_type=='Model'){
    $("#next").append('<span>&nbsp;' + data.data.result.make_type +'&nbsp;</span>');
     ajaxWithHeader('GET', null, '/built?make='+ $("#make").val()+'&level=0', 'render', 'setNext',null);
  
}

function setNext(data){
    a = a+1 ;
    // console.log(data.data.result);
    s = '<select' + ' id="step'+a+'"'+ 'onchange="jsFunction(step'+a+')"' +'>';
    s += '<option>' + 'Choose....'+'</option>';
    for(i=0;i<data.data.result.length;i++){
        // console.log(data.data.result[i].make);
        var makeid=data.data.result[i].make;
       s += setSelect(data.data.result[i],makeid);
    }
    s += '</select>'
    $("#next").append(s);

}
function setSelect(title,makeid, attrId){
    console.log(makeid);

    return '<option'+ ' value='+ title.id   +'>' + title.title +'</option>';
}

function jsFunction(val){
    alert(val);
    val = $("#"+val).val();
    alert(val);
    // $("#next").append('<span>&nbsp;' + data.data.result.make_type +'&nbsp;</span>');
    ajaxWithHeader('GET', null, '/built?parent_id='+ val+'&level=1', 'render', 'setNextmodal', null);
}
function setNextmodal(data){
    if(data.data.result.length > 0){
        a = a+1 ;
        // console.log(data.data.result);
        s = '<select' + ' id="step'+a+'"'  + 'onchange="jsFunction(step'+a+')"' +'>';
        s += '<option>' + 'Choose....'+'</option>';
        for(i=0;i<data.data.result.length;i++){
            // console.log(data.data.result[i].make);
            var makeid=data.data.result[i].make;
           s += setSelect(data.data.result[i],makeid, a+1);
        }
        s += '</select>'

        $(".form-area").append(s);
    }

}
