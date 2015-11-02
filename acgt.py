# coding=utf-8

import io,json

class Acgt(object):
  """docstring for Acgt"""
  def __init__(self):
    super(Acgt, self).__init__()

  @classmethod
  def read_file(self):
    with io.open("api.json", "r") as file:
      buff = file.read()
      file.close()
    return str(buff).strip().encode("utf-8")

  @classmethod
  def to_json(self):
    string = self.read_file()
    api_json = json.loads(string, encoding='utf-8')
    return api_json

  @classmethod
  def parse_apis(self):
    j = self.to_json()
    for x in range(len(j["api"])):
      self.parse_module(j["api"][x])

  @classmethod
  def parse_module(self, arg):
    for x in range(len(arg["detail"])):
      self.parse_detail(arg["detail"][x])

  @classmethod
  def parse_detail(self, arg):
    print(arg)

if __name__ == '__main__':
  Acgt.parse_apis()