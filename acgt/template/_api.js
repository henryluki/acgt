// generate by acgt
var Api = {
  host: "",
% if routes:
% for m in routes:
% for r in m["detail"]:
  {{r["name"]}}: function(args, cb_success) {
    $.ajax({
      type: '{{r["method"]}}',
      url: this.host + '{{ "/" + m["module"]+ "/" + r["name"]}}',
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
% end
% end
% end
}