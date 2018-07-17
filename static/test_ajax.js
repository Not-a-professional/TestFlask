var data = {
    'name': '李伟',
    'age' : 23
};

$.ajax({
    url:'/test_ajax',
    type:'POST',
    data:JSON.stringify(data),
    contentType: 'application/json; charset=UTF-8',
    dataType: 'json', //注意：这里是指希望服务端返回json格式的数据
    success: function (data) {
        alert(data)
    },
    error: function (data) {
        alert(data)
    }
});