# yxes-config-find_dir
locate specific folders (conf, log, reports, custom) from a local environment

This may not prove useful to everyone (anyone?) but the basic structure I use
for my scripts is as follows:

```
app/
|--bin
|--config
|--reports
|--log
|--...
```

Instead of explicitly stating where I should drop a report or pick up a config
file, it finds the directory based on my location. This allows me to use
different folders for different purposes (_mostly testing_). Eventually, 
linking my local directories to a global one that does something useful.

You will find a lot of my objects inherit this. It's very flexible and you
don't have to rely on it yourself.

## Installation

```
git clone https://github.com/yxes/yxes-config-find_dir.git
cd yxes-config-find_dir
pip install .
```

### Requirements

`pip install -r requirements` is only required if you intend to develop 
(_including tests_) against this package. Otherwise simply install it as
outlined above.

## Usage

In objects...
```
from yxes.config.find_dir import FindDir

import os

class MyObj(FindDir):

    def __init__(self, ...):
        FindDir.__init__(self)

    def config_file_full_path(self, config_file):
        return os.path.join(self.conf_dir, config_file)
```

In a script...
```
#!/usr/bin/env python

from yxes.config.find_dir import FindDir

fd = FindDir()

config_file = fd.conf_dir + "myconfig.cfg"
log_file = fd.log + "myscript.log"
```

## Tests

Tests are run using [coverage](https://coverage.readthedocs.io/en/coverage-5.1/)
with a shortcut called [runtests.sh](runtests.sh) that performs housekeeping
and runs the tests. All tests are located in the `tests` sub directory.

### Subfolders

The following subdirectories are only used for tests purposes. We need to have
some folders to find afterall.

- conf
- reports
- log
- test_dir

## Todo

Possibly?

- [ ] functionality for environment variables to set locations
- [ ] drop the requirement of building out a new object each time

## Contributing

You are welcome to fork this repository and updates, fixes, etc are strongly 
encouraged.

[how to contribute](https://help.github.com/articles/setting-guidelines-for-repository-contributors/)

## License

The contents of this repository are covered under the [MIT License](https://github.com/udacity/ud777-writing-readmes/blob/master/LICENSE).

## Author

[Steve Wells](https://www.stephendwells.com/)


