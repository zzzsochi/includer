from setuptools import setup


setup(name='includer',
      version='1.0.0',
      description='Include and run callables',
      classifiers=[
          "License :: OSI Approved :: BSD License",
          "Operating System :: POSIX",
          "Programming Language :: Python :: 3",
          "Development Status :: 5 - Production/Stable",
      ],
      author='Alexander Zelenyak',
      author_email='zzz.sochi@gmail.com',
      license='BSD',
      url='https://github.com/zzzsochi/includer',
      keywords=['include', 'configure', 'pyramid'],
      py_modules=['includer'],
      install_requires=['zope.dottedname'],
      tests_require=['pytest'],
)
