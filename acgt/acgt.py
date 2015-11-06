# -*- coding: utf-8 -*-
import io,json,sys,getopt,os
from gen import Gen

class Acgt(object):
  """docstring for Acgt"""
  def __init__(self, project_name):
    super(Acgt, self).__init__()
    self.project_name = project_name
    self.path = os.popen('pwd').readlines()[0][0:-1] + "/"

  def read_file(self):
    with io.open(self.path + "api.json", "r") as file:
      buff = file.read()
    return str(buff).strip().encode("utf-8")

  def get_json(self):
    string = self.read_file()
    api_json = json.loads(string, encoding='utf-8')
    return api_json

  def parse_apis(self, feature):
    j = self.get_json()
    apis = []
    for x in range(len(j["api"])):
      apis.append(dict({'module': j["api"][x]["module"], 'detail': self.parse_module(j["api"][x])}))
    Gen(self.project_name).gen_template(apis, feature)

  def parse_module(self, arg):
    for x in range(len(arg["detail"])):
      yield self.parse_detail(arg["detail"][x])

  def parse_detail(self, arg):
    return dict({'arguments':arg["arguments"], 'method':arg["method"], 'name':arg["name"], 'results': arg["results"]})

  def take_arguments(self):
    if sys.argv[1:] == []:
      self.usage()
    try:
      opts, args = getopt.getopt(sys.argv[1:], "h", ["help", "api="])
    except getopt.GetoptError as err:
      print str(err)
      self.usage()
      sys.exit(2)
    self.execute_feature(opts)

  def execute_feature(self, opts):
    for o, a in opts:
      if o == "-h" or o == "--help":
        self.usage()
        sys.exit(2)
      elif o == "--api":
        if a == "flask":
          print "Generate app..."
          self.parse_apis()
          print "Done!"
        elif a == "js":
          print "js..."
        else:
          print "Take some feature liki 'flask'"
      else:
        assert False, "Option error"

  def usage(self):
    print "*** usage info ***"
    print "--api=(flask,js)   generate code by acgt"
    print "-h  --help         usage info "

if __name__ == '__main__':
  acgt = Acgt("example")
  acgt.path = "../"
  acgt.parse_apis("flask")
  acgt.parse_apis("js")