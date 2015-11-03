from setuptools import setup

setup(name='acgt',
      version='0.1',
      packages=['acgt'],
      url='https://github.com/henryluki/acgt',
      description='Auto Code Generation Tools',
      author='Sam',
      author_email='nicksite68@gmail.com',
      license='MIT',
      include_package_data=True,
      install_requires=[
        'bottle', 'click'
      ],
      entry_points='''
        [console_scripts]
        acgt=acgt.cmd:cli
      ''',
      package_data = {
        'acgt': ['template/*'],
      },
      zip_safe=False)