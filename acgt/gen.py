# -*- coding: utf-8 -*-
import io,os
from bottle import SimpleTemplate

class Gen(object):

  """docstring for Gen"""
  def __init__(self, project_name):
    super(Gen, self).__init__()
    self.project_name = project_name
    self.feature = "flask"
    self.file = "_app.py"

  def read_template(self):
    path = os.path.dirname(os.path.abspath(__file__))
    with open(path + "/template/" + self.file, "r") as file:
      buff = file.read()
      file.close()
    return buff

  def gen_template(self, code, feature):
    self.check_feature(feature)
    temp = self.read_template()
    s = SimpleTemplate(temp)
    s = s.render({'routes':code})
    self.write_file(s)

  def check_feature(self, feature):
    if feature != self.feature:
      self.feature = feature

    if self.feature == "flask":
      self.file = "_app.py"
    elif self.feature == "js":
      self.file = "_api.js"
    else:
      self.file = "_app.py"

  def write_file(self, s):
    path = self.project_name
    self.check_dir(path)
    with open(path + "/" + self.file.strip("_"), "w") as file:
      file.write(s)
      file.close()

  def check_dir(self, path):
    if not os.path.exists(path):
      os.makedirs(path)

if __name__ == '__main__':
  Gen("app").gen_template("","js")