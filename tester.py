import logging
import unittest
from os.path import dirname, join
from bot.logging import log

project_root = dirname(dirname(__file__))

if __name__ == '__main__':
    # Create runner
    logging.disable(logging.CRITICAL)
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner(verbosity=2)

    # Create test suite
    all_tests = loader.discover(start_dir=project_root)

    # Run suite
    runner.run(all_tests)