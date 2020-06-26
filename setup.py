import os

from yxes.config.find_dir import __version__ as version

readme = os.path.join(os.path.dirname(__file__), 'README.md')
long_description = open(readme).read()

SETUP_ARGS = dict(
    name='yxes-config-find_dir',
    version=version,
    description=('locate specific folders from a local environment'),
    long_description=long_description,
    url='https://github.com/yxes/yxes-config-find_dir',
    author='Steve Wells',
    author_email='yxes123@gmail.com',
    license='MIT',
    include_package_data=True,
    classifiers=[
      'Development Status :: 5 - Production/Stable',
      'Environment :: Console',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: MIT License',
      'Operating System :: Unix',
      'Programming Language :: Python :: 3.8',
    ],
    py_modules = ['yxes.config.find_dir',],
    install_requires = [],
)

if __name__ == '__main__':
    from setuptools import setup, find_packages

    SETUP_ARGS['packages'] = find_packages()
    setup(**SETUP_ARGS)
