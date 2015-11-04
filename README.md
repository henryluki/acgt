# acgt

Auto Code Generation Tools

This is a tool for code generatation, define an `api.json` file, output api codes.
Recently, this tool is used for `flask` app and `js` ajax codes.

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

- for js

` acgt init --js=True PROJECT_NAME `

####  Run example

` acgt init --flask=True "example" `

` acgt init --js=True "example" `

####  Run as a script

it requires `api.json ` at the same directory

```
from acgt.acgt import Acgt

def main():
  # project_name = "example"
  acgt = Acgt("example")
  # "api.json" relative path
  acgt.path = ""
  # feature = "flask"
  print "init flask app ..."
  acgt.parse_apis("flask")
  # feature = "js"
  print "init js ..."
  acgt.parse_apis("js")
  print "done!"

if __name__ == '__main__':
  main()
```
Take a look at ` scripts.py`
