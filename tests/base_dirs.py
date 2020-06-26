#!/usr/bin/env python

# test: base_dirs.py

from unittest import TestCase
#from unittest.mock import patch

from yxes.config.find_dir import FindDir

class TestFindDir(TestCase):

    def setUp(self):
        self.fd = FindDir()

    def test_conf(self):
        self.assertTrue(
          self.fd.conf_dir.endswith("yxes-config-find_dir/conf/")
        )

    def test_log(self):
        self.assertTrue(
          self.fd.log_dir.endswith("yxes-config-find_dir/log/")
        )

    def test_report(self):
        self.assertTrue(
          self.fd.report_dir.endswith("yxes-config-find_dir/reports/")
        )

    def test_test_dir(self):
        fd = FindDir('test_dir')
        self.assertTrue(
          fd.found_dir.endswith("yxes-config-find_dir/test_dir/")
        )

    def test_not_found_dir(self):
        fd = FindDir('no-way-this-exists-afsd')
        self.assertFalse( fd.found_dir )

# if __name__ == "__main__":
#     from unittest import main
#     main()