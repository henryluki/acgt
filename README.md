# acgt

Auto Code Generation Tools

This is a tool for code generatation, define an `api.json` file, output api codes.
Recently, this tool is used for `flask` app.

----------
####   Install

` pip install -r requirement.text `

` cd acgt `

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

#### Run as a script

it requires `api.json ` at the same directory

```
from acgt.acgt import Acgt

def main():
  # project_name = "example"
  Acgt("example").parse_apis()

if __name__ == '__main__':
  main()
```
Take a look at ` scripts.py`
