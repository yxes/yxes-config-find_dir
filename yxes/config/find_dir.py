#!/usr/bin/env python
# yxes/config/find_dir.py

__version__ = '1.0.0'

import os

class FindDir():
    _base_dir = os.path.dirname(os.path.realpath(__file__))
    conf_dir = ''
    log_dir  = ''
    report_dir = ''
    found_dir = '' # for special cases

    def __init__(self, dirname=None):
        if dirname is None: # maybe these should 'always' be the case
            self.conf_dir = self._find_dir('conf')
            self.log_dir = self._find_dir('log')
            self.report_dir = self._find_dir('reports')
        else:
            self.found_dir = self._find_dir(dirname)

    def _find_dir(self, dirname=None):
        if dirname is None: dirname = 'conf' # default

        current_dir = os.path.join(self._base_dir, dirname)
        while not os.path.isdir(current_dir):
            if os.path.dirname(current_dir) == '/': return None

            current_dir = os.path.join(
              os.path.dirname(os.path.dirname(current_dir)), dirname
            )

        return current_dir + '/'

if __name__ == "__main__":
    cd = FindDir() # pragma: no cover
    print(f"conf dir: {cd.conf_dir}") # pragma: no cover
    print(f"log dir: {cd.log_dir}") # pragma: no cover
    print(f"report dir: {cd.report_dir}") # pragma: no cover

    cd2 = FindDir("home") # pragma: no cover
    print(f"home dir: {cd2.found_dir}") # pragma: no cover

    cd3 = FindDir("asjejafs") # pragma: no cover
    print(f"not found dir: {cd3.found_dir}") # pragma: no cover
