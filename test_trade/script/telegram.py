import sys
import os

# Add the parent directory (test_trade/) to sys.path
# parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# sys.path.append(parent_dir)

from ..test_utils import test_me

print(test_me())
