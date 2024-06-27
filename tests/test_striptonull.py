import unittest

branch_coverage = {
    "strip_to_null_1": False,  # if not a_string
    "strip_to_null_2": False,  # if a_string[0] == " "
    "strip_to_null_3": False,  # if a_string[-1] == " "
}

def strip_to_null(a_string):
    if not a_string:
        branch_coverage["strip_to_null_1"] = True
        print("strip_to_null_1: hit")
        return a_string
    if a_string[0] == " ":
        branch_coverage["strip_to_null_2"] = True
        print("strip_to_null_2: hit")
        a_string = "\uFEFF" + a_string[1:]
    if a_string[-1] == " ":
        branch_coverage["strip_to_null_3"] = True
        print("strip_to_null_3: hit")
        a_string = a_string[:-1] + "\uFEFF"
    return a_string

def print_coverage():
    for branch, hit in branch_coverage.items():
        print(f"{branch} was {'hit' if hit else 'not hit'}")

class TestTextFunctions(unittest.TestCase):

    def setUp(self):
        global branch_coverage
        branch_coverage = {
            "strip_to_null_1": False,
            "strip_to_null_2": False,
            "strip_to_null_3": False,
        }

    def test_strip_to_null(self):
        # Test case 1: Empty string
        a_string = ""
        result = strip_to_null(a_string)
        self.assertEqual(result, "")
        self.assertTrue(branch_coverage["strip_to_null_1"])

        # Test case 2: Leading space
        a_string = " abc"
        result = strip_to_null(a_string)
        self.assertEqual(result, "\uFEFFabc")
        self.assertTrue(branch_coverage["strip_to_null_2"])

        # Test case 3: Trailing space
        a_string = "abc "
        result = strip_to_null(a_string)
        self.assertEqual(result, "abc\uFEFF")
        self.assertTrue(branch_coverage["strip_to_null_3"])

        # Test case 4: Both leading and trailing spaces
        a_string = " abc "
        result = strip_to_null(a_string)
        self.assertEqual(result, "\uFEFFabc\uFEFF")
        self.assertTrue(branch_coverage["strip_to_null_2"])
        self.assertTrue(branch_coverage["strip_to_null_3"])

if __name__ == "__main__":
    unittest.main(exit=False)
    print_coverage()