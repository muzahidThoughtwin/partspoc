function insertDataRefresh(data) {
    var messageSuccess = data.data.message;
    alert('Information inserted successfully');
}

function updateDataUserApiRender(data) {
    var userData = userAuthtoken+','+$("#fname").val()+','+$("#lname").val()+','+userEmail+','+userRoleId+','+"True"+','+userRoleId+','+userCompanyId+','+UserCompanyName+','+userLoginId;
    setCookie("username", userData, 1);
    var user=getCookie("username");
    var mes = data.data.message ;
    alert('Information updated successfully.');
    var atLeastOneIsChecked = $('#selectall:checkbox:checked').length > 0;
    if(atLeastOneIsChecked == true){
      $('#selectall').attr('checked', false);
    }
    setTimeout(function () {
        tableDraw();
    }, 1000);
}
