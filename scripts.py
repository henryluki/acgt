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