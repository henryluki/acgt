/*
   apis example
*/

var json = {
  "api": [{
    "module": "order",
    "detail": [{
      "method": "get",
      "name": "get_order_list",
      "arguments": ["id"],
      "results": ""
    }, {
      "method": "post",
      "name": "get_order",
      "arguments": "",
      "results": ""
    }]
  }, {
    "module": "article",
    "detail": [{
      "method": "get",
      "name": "get_article_list",
      "arguments": ["id"],
      "results": ""
    }, {
      "method": "post",
      "name": "get_article",
      "arguments": "",
      "results": ""
    }]
  }]
};

/*
  common func
*/

function print(argument) {
  console.log(argument)
}

/*
  logic
*/

function parse_api(argument) {
  if (argument["api"] != undefined && argument["api"].length != 0) {
    var apis = argument["api"];
    // moduels
    apis.map(function(elem, index) {
      parse_modules(elem)
    })
  } else {
    print("argument type errors")
  }
}

function parse_modules(argument) {
  if (argument["module"] != undefined && argument["module"].length != 0) {
    var details = argument["detail"];
    // datails
    details.map(function(elem, index) {
      parse_details(elem)
    })
  } else {
    print("argument type errors")
  }
}

function parse_details(argument) {
  print(argument)
}

/*
  app
*/

function main() {
  parse_api(json)
}

main()