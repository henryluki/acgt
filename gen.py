# coding=utf-8
import io,os
from bottle import SimpleTemplate

class Gen(object):

  """docstring for Gen"""
  def __init__(self):
    super(Gen, self).__init__()

  @classmethod
  def read_template(self):
    with open("template/_app.py", "r") as file:
      buff = file.read()
      file.close()
    return buff

  @classmethod
  def gen_template(self, code):
    temp = self.read_template()
    s = SimpleTemplate(temp)
    s = s.render({'routes':code})
    self.write_file(s)

  @classmethod
  def write_file(self, s):
    path = "app"
    self.check_dir(path)
    with open(path + "/app.py", "w") as file:
      file.write(s)
      file.close()

  @classmethod
  def check_dir(self, path):
    if not os.path.exists(path):
      os.makedirs(path)

if __name__ == '__main__':
  Gen.gen_template()