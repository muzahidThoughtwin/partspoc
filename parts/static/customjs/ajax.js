var URL = "127.0.0.0:8080"


function ajaxRender(method, data, url, callback, finalMethod){
  var result;

  $.ajax({
    type: method,
    dataType: "json",
    url: URL+url,
    data: data,
    cache: false,
    async:false,
    success: function(data){
      return window[callback](finalMethod, data)
    }
  });
}

function ajaxWithHeader(method, data, url, callback, finalMethod,appender= null){
  // alert(method);
  // console.log(data);
  // alert(URL+url);
  // alert(callback);
  // alert(finalMethod);
  // alert(appender);

  // var result;
  // var valid = specialCharaterValidate();
  // alert('------------');
  // if(valid && method!="GET")
  //   return alert(valid)
  // $('button').attr('disabled','disabled');
  // $('.fakeloader').show();
    // headers:{
    //   "Authorization": userAuthorization
    // },
// console.log(url);
  $.ajax({
    type: method,
    dataType: "json",
    url: url,
    data: data,
    statusCode: {
      401: function(data) {
        console.log(data);
        var messageError = data.data.message;
        alert(messageError);
        return false;
      },
      400: function() {
        var messageError = data.data.message;
        alert(messageError);
        return false;
      },
      403: function() {
        var messageError = data.data.message;
        alert(messageError);
        return false;
      },
      404: function() {
        alert('Something went wrong. Please try again later. 4');
        return false;
      },
      500: function() {
        var messageError = data.data.message;
        alert(messageError);
        return false;
      }
    },          
    success: function(data){
      // if((data.data.error) && (data.data.responseCode==400 || res.data.responseCode==404){

      // } 
      setTimeout(function () {
        // $('button').removeAttr('disabled','disabled');
        // $('.fakeloader').hide();
        return window[callback](finalMethod, data,appender)
      }, 2000);
    },
    error: function (err) {
      console.log(err)
      alert('Something went wrong. Please try again later. 1');
      return false;
    }

  });
}


function specialCharaterValidate(){
  var error = false;
   $("input:text:visible, textarea:visible").each(function(){
    if($(this).attr("allow-special") ) return true;
    console.log($(this).val(),$(this).text())
    if(!$(this).val().match(/^[\w\s]+$/g) && !$(this).text().match(/^[\w\s]+$/g)){
      var match = $(this).parent().prev().text().trim().match(/[\w\s]+/g);
      if(!match || !match[0])
        return true;  
      error =  "Special characters are not allowed in "+ match[0].toLowerCase();
      return false;
    }

  });
  return error
}

function render(callback, data,appender){
  if(data == null || data == ''){
    alert("Something went wrong. Please try again later. 22 ");
    return false;
  }  
  if(data.data.responseCode == null || data.data.responseCode == ''){
    notifySuccess("Something went wrong. Please try again later. 3");
    location.reload();
  }
  if(data.data.responseCode == 400 || data.data.responseCode == 404 || data.data.responseCode == 500){

    if(typeof data.data.error =='object'){                   
      $.each(data.data.error,function(key,val){
        console.log(key);
      // if(val.length > 0)                            
      //   alert(val[0]);
      // })                
    }) }
    else
      {
        alert(data.data.error)
      }

    return false;

  }
  window[callback](data,appender)
}
