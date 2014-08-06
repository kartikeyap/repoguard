import unittest
import os
from mock import patch
from repoguard import RepoGuard


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.mock_logger_patcher = patch('repoguard.logging')
        self.mock_logger = self.mock_logger_patcher.start()

        self.rg = RepoGuard(self.mock_logger)
        self.test_data_folder = "%s/test_data/" % os.path.dirname(os.path.realpath(__file__))

    def tearDown(self):
        self.mock_logger_patcher.stop()
