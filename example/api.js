// generate by acgt
var Api = {
  host: "",
  get_all_article: function(args, cb_success) {
    $.ajax({
      type: 'get',
      url: this.host + '/article/get_all_article',
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
  get_detail: function(args, cb_success) {
    $.ajax({
      type: 'get',
      url: this.host + '/article/get_detail',
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