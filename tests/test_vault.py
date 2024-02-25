import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))


import unittest
import tempfile
import shutil
from vault import File, Vault


class TestFile(unittest.TestCase):
    def test_file_initialization(self):
        path = "/path/to/file"
        file = File(path)
        self.assertEqual(file.path, path)


class TestVault(unittest.TestCase):
    def setUp(self):
        # Setup a temporary directory
        self.temp_dir = tempfile.mkdtemp()
        # Create some dummy files and directories
        os.makedirs(os.path.join(self.temp_dir, ".obsidian"))
        os.makedirs(os.path.join(self.temp_dir, "notes"))
        with open(os.path.join(self.temp_dir, "notes", "note1.md"), "w") as f:
            f.write("This is a test note.")

    def test_vault_initialization(self):
        vault = Vault(self.temp_dir)
        self.assertEqual(vault.full_path, self.temp_dir)

    def test_read_files(self):
        vault = Vault(self.temp_dir)
        expected_file_path = os.path.join(self.temp_dir, "notes", "note1.md")
        self.assertTrue(any(file.path == expected_file_path for file in vault.files))

    def tearDown(self):
        # Remove the directory after the test
        shutil.rmtree(self.temp_dir)


if __name__ == "__main__":
    unittest.main()
