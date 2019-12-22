from setuptools import setup

setup(name="comware_sshconv",
      version="1.0.0",
      author="Matthias Hannig",
      py_modules=["keyconv"],
      entry_points={
          "console_scripts": "comware_sshconv = keyconv:cli_main",
      })
