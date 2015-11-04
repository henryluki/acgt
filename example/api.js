// generate by acgt
var Api = {
  host: "",
  get_order_list: function(args, cb_success) {
    $.ajax({
      type: 'get',
      url: this.host + '/order/get_order_list',
      data: args,
      success: function(data) {
        cb_success(data);
      },
      error: function() {
        console.log("ajax error");
      },
      dataType: 'JSON'
    });
  },
  get_order: function(args, cb_success) {
    $.ajax({
      type: 'post',
      url: this.host + '/order/get_order',
      data: args,
      success: function(data) {
        cb_success(data);
      },
      error: function() {
        console.log("ajax error");
      },
      dataType: 'JSON'
    });
  },
  get_article_list: function(args, cb_success) {
    $.ajax({
      type: 'get',
      url: this.host + '/article/get_article_list',
      data: args,
      success: function(data) {
        cb_success(data);
      },
      error: function() {
        console.log("ajax error");
      },
      dataType: 'JSON'
    });
  },
  get_article: function(args, cb_success) {
    $.ajax({
      type: 'get',
      url: this.host + '/article/get_article',
      data: args,
      success: function(data) {
        cb_success(data);
      },
      error: function() {
        console.log("ajax error");
      },
      dataType: 'JSON'
    });
  },
}