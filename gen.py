from string import Template
import io


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
  def gen_template(self):
    temp = self.read_template()
    s = Template(temp)
    self.write_file(s.substitute({'title':title,'code':code}))

  @classmethod
  def write_file(self,s):
    with open("app/app.py", "w") as file:
      file.write(s)
      file.close()

if __name__ == '__main__':
  Gen.gen_template()