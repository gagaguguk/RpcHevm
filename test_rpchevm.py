# test_rpchevm.py
"""
Tests for RpcHevm module.
"""

import unittest
from rpchevm import RpcHevm

class TestRpcHevm(unittest.TestCase):
    """Test cases for RpcHevm class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RpcHevm()
        self.assertIsInstance(instance, RpcHevm)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RpcHevm()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
