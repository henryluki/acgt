# acgt

Auto Code Generation Tools

This is a tool for code generatation, define an `api.json` file output api codes.
Recently, this tool is used for `flask` app.

----------
####   Install

` git clone https://github.com/henryluki/acgt.git`

` cd acgt `

` pip install -r requirement.text `

` python setup.py install `

####    Require:
- api.json :

```
{
  “api”: [ {
    "module":"module_name",
    "detail":[
      "method":"get(post)",
      "name":"method_name",
      "arguments":"",
      "result":""
    ]
  }]
}
```
Take a look at api.json for more detail.
####   Command

- acgt

` acgt usage `
- acgt init

` acgt init [option] PROJECT_NAME `

- for flask

` acgt init --flask=True PROJECT_NAME `

####  Run example

` acgt init --flask=True "example" `
