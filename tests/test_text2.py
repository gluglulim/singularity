
import unittest

branch_coverage = {
    "strip_to_null_1": False,  # if not a_string
    "strip_to_null_2": False,  # if a_string[0] == " "
    "strip_to_null_3": False,  # if a_string[-1] == " "
}

def strip_to_null(a_string):
    if not a_string:
        branch_coverage["strip_to_null_1"] = True
        print(f"strip_to_null_1 was {'hit' if branch_coverage['strip_to_null_1'] else 'not hit'}")
        return a_string
    if a_string[0] == " ":
        branch_coverage["strip_to_null_2"] = True
        print(f"strip_to_null_2 was {'hit' if branch_coverage['strip_to_null_2'] else 'not hit'}")
        a_string = "\uFEFF" + a_string[1:]
    if a_string[-1] == " ":
        branch_coverage["strip_to_null_3"] = True
        print(f"strip_to_null_3 was {'hit' if branch_coverage['strip_to_null_3'] else 'not hit'}")
        a_string = a_string[:-1] + "\uFEFF"
    return a_string

def print_coverage():
    for branch, hit in branch_coverage.items():
        print(f"{branch} was {'hit' if hit else 'not hit'}")

class TestTextFunctions(unittest.TestCase):

    def test_strip_to_null(self):
        # Test case 1: Empty string
        result = strip_to_null("")
        self.assertEqual(result, "")
        self.assertTrue(branch_coverage["strip_to_null_1"])

        # Reset coverage for next test
        branch_coverage["strip_to_null_1"] = False
        branch_coverage["strip_to_null_2"] = False
        branch_coverage["strip_to_null_3"] = False

        # Test case 2: Leading space
        result = strip_to_null(" abc")
        self.assertEqual(result, "\uFEFFabc")
        self.assertTrue(branch_coverage["strip_to_null_2"])

        # Reset coverage for next test
        branch_coverage["strip_to_null_1"] = False
        branch_coverage["strip_to_null_2"] = False
        branch_coverage["strip_to_null_3"] = False

        # Test case 3: Trailing space
        result = strip_to_null("abc ")
        self.assertEqual(result, "abc\uFEFF")
        self.assertTrue(branch_coverage["strip_to_null_3"])

        # Reset coverage for next test
        branch_coverage["strip_to_null_1"] = False
        branch_coverage["strip_to_null_2"] = False
        branch_coverage["strip_to_null_3"] = False

        # Test case 4: Both leading and trailing spaces
        result = strip_to_null(" abc ")
        self.assertEqual(result, "\uFEFFabc\uFEFF")
        self.assertTrue(branch_coverage["strip_to_null_2"])
        self.assertTrue(branch_coverage["strip_to_null_3"])

if __name__ == "__main__":
    unittest.main()

