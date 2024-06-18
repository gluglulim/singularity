import unittest

branch_coverage = {
    "detect_chance_1": False,  # if detects_per_day > 225
    "detect_chance_2": False,  # elif detects_per_day > 150
    "detect_chance_3": False,  # elif detects_per_day > 75
    "detect_chance_4": False,  # else
}

def detect_chance_to_danger_level(detects_per_day):
    if detects_per_day > 225:
        branch_coverage["detect_chance_1"] = True
        print(f"detect_chance_1 was {'hit' if branch_coverage['detect_chance_1'] else 'not hit'}")
        return 3
    elif detects_per_day > 150:
        branch_coverage["detect_chance_2"] = True
        print(f"detect_chance_2 was {'hit' if branch_coverage['detect_chance_2'] else 'not hit'}")
        return 2
    elif detects_per_day > 75:
        branch_coverage["detect_chance_3"] = True
        print(f"detect_chance_3 was {'hit' if branch_coverage['detect_chance_3'] else 'not hit'}")
        return 1
    else:
        branch_coverage["detect_chance_4"] = True
        print(f"detect_chance_4 was {'hit' if branch_coverage['detect_chance_4'] else 'not hit'}")
        return 0

def print_coverage():
    for branch, hit in branch_coverage.items():
        print(f"{branch} was {'hit' if hit else 'not hit'}")

class TestDetectChanceFunctions(unittest.TestCase):

    def setUp(self):
        global branch_coverage
        branch_coverage = {
            "detect_chance_1": False,
            "detect_chance_2": False,
            "detect_chance_3": False,
            "detect_chance_4": False,
        }

    def test_detect_chance_to_danger_level(self):
        # Test case 1: detects_per_day > 225
        result = detect_chance_to_danger_level(230)
        self.assertEqual(result, 3)
        self.assertTrue(branch_coverage["detect_chance_1"])

        # Test case 2: detects_per_day > 150
        result = detect_chance_to_danger_level(160)
        self.assertEqual(result, 2)
        self.assertTrue(branch_coverage["detect_chance_2"])

        # Test case 3: detects_per_day > 75
        result = detect_chance_to_danger_level(100)
        self.assertEqual(result, 1)
        self.assertTrue(branch_coverage["detect_chance_3"])

        # Test case 4: detects_per_day <= 75
        result = detect_chance_to_danger_level(50)
        self.assertEqual(result, 0)
        self.assertTrue(branch_coverage["detect_chance_4"])

if __name__ == "__main__":
    unittest.main(exit=False)
    print_coverage()