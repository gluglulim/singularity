# Report for Assignment 1

## Project chosen
**Name:** singularity  
**URL:** [https://github.com/singularity/singularity](https://github.com/singularity/singularity)  
**Number of lines of code and the tool used to count it:** Lizard - 13782 lines of code  
**Programming language:** Python  

## Coverage measurement

### Existing tool
**Name of the existing tool:** coverage.py

**How it was executed:** 

**Coverage results provided by the existing tool with a screenshot:**

![Coverage results running in Windows system](https://github.com/gluglulim/singularity/blob/master/link-to-screenshot/coverage_result_window.png)
Coverage results running in Windows system: 35%

![Coverage results running on Mac]([link-to-screenshot/Coverage results running on Mac.png](https://github.com/gluglulim/singularity/blob/master/link-to-screenshot/Coverage%20results%20running%20on%20Mac.png?raw=true))
Coverage results running on Mac: 53%

### Your own coverage tool

**Youngchae Lim**

**Function 1:** `detect_chance_to_danger_level(detects_per_day)`
[Patch (diff) or commit link](https://github.com/gluglulim/singularity/commit/4e73ea0738c6ecbf3034df3e759ea95f03a06517)

**Screenshot of the coverage results output by the instrumentation:**
![Coverage results for detect_chance_to_danger_level]([link-to-screenshot](https://github.com/gluglulim/singularity/blob/master/link-to-screenshot/Coverage%20results%20for%20detect_chance_to_danger_level.png?raw=true))

**Function 2:** `strip_to_null(a_string)`
[Patch (diff) or commit link](https://github.com/gluglulim/singularity/commit/08aedf88f5f52ef68f8e529f729e07c1c8101706#diff-0b9aa73ce494f32270b58ee8500b17328a4390bce1e96a56b1883a8495f32ac3)

**Screenshot of the coverage results output by the instrumentation:**
![Coverage results for strip_to_null](link-to-screenshot)

**Wiktoria Zaręba**

**Function 1:** `fake_click(down)`
[Patch (diff) or commit link](https://github.com/gluglulim/singularity/commit/c2e03bd393d17616687adc2e21958e2ff579fd08)

**Screenshot of the coverage results output by the instrumentation:**
![Coverage results for fake_click](https://github.com/gluglulim/singularity/blob/master/link-to-screenshot/Zrzut%20ekranu%202024-06-27%20o%2022.39.50.png)

**Function 2:** `insort_right_w_key(a, x, lo=0, hi=None, key=lambda v: v)`
[Patch (diff) or commit link](https://github.com/gluglulim/singularity/commit/c2e03bd393d17616687adc2e21958e2ff579fd08)

**Screenshot of the coverage results output by the instrumentation:**
![Coverage results for insort_right_w_key](link-to-screenshot)

**Yuto Ishihara**

**Function 1:** `get_writable_file_in_dirs(filename, dir_name, outer_paths=None)`
[Patch (diff) or commit link](https://github.com/gluglulim/singularity/pull/3/commits)

**Screenshot of the coverage results output by the instrumentation:**
![Coverage results for get_writable_file_in_dirs](link-to-screenshot)

**Function 2:** `power_state_name(self)`
[Patch (diff) or commit link](link-to-commit)

**Screenshot of the coverage results output by the instrumentation:**
![Coverage results for power_state_name](link-to-screenshot)

**Marika Litwiniak**

**Function 1:** `suspicion_to_danger_level(suspicion)`
[Patch (diff) or commit link](https://github.com/gluglulim/singularity/commit/d5256cf1932fad94cb797bcdc035975bebb2b968)

**Screenshot of the coverage results output by the instrumentation:**
![Coverage results for suspicion_to_danger_level](link-to-screenshot)

**Function 2:** `nearest_percent(value, step=100)`
[Patch (diff) or commit link](https://github.com/gluglulim/singularity/commit/d5256cf1932fad94cb797bcdc035975bebb2b968)

**Screenshot of the coverage results output by the instrumentation:**
![Coverage results for nearest_percent](link-to-screenshot)

## Coverage improvement

### Individual tests

**Youngchae Lim**

**Test 1:** `strip_to_null(a_string)`
[Patch (diff) or commit link](https://github.com/gluglulim/singularity/pull/1/commits)

**Old coverage results:** 
![Old coverage results](link-to-screenshot)

**New coverage results:**
![New coverage results](link-to-screenshot)

**Coverage improvement:**
The `strip_to_null(a_string)` function was not covered by coverage.py at all (0%) and improved to 90% with newly created tests. The tests check three branches in the function:
- Checking if the string is empty
- Checking if the first character is a space
- Checking if the last character is a space

To ensure these branches were covered, new test cases were created to give input with an empty string, leading space, trailing space, and both leading and trailing spaces. These tests executed all branches of the function, improving the branch coverage.

**Test 2:** `detect_chance_to_danger_level(detects_per_day)`
[Patch (diff) or commit link](https://github.com/gluglulim/singularity/pull/1/commits)

**Old coverage results:**
![Old coverage results](link-to-screenshot)

**New coverage results:**
![New coverage results](link-to-screenshot)

**Coverage improvement:**
The `detect_chance_to_danger_level(detects_per_day)` function had 0% coverage by coverage.py. This function assesses the danger level based on the number of detections per day in the game. To improve coverage, tests were created to cover all 4 branches:
- If `detects_per_day > 225`, return 3
- If `detects_per_day > 150`, return 2
- If `detects_per_day > 75`, return 1
- Else, return 0

Test cases were created to cover each branch with different input values:
- `detects_per_day > 225`: input 230, expected result 3
- `detects_per_day > 150`: input 160, expected result 2
- `detects_per_day > 75`: input 100, expected result 1
- `detects_per_day <= 75`: input 50, expected result 0

These test cases successfully covered each branch, improving the coverage from 0% to 90%.

**Wiktoria Zaręba**

**Test 1:** `fake_click(down)`
[Patch (diff) or commit link](https://github.com/gluglulim/singularity/commit/5321ee6ae2ab8027c959b7c7a8947fb1eb90e2ea)

**Old coverage results:** 
![Old coverage results](https://github.com/gluglulim/singularity/commit/e46c18a60d16ef0db69cc8aaefd0df17de161374)

**New coverage results:**
![New coverage results](link-to-screenshot)

**Coverage improvement:**
The initial coverage measured with coverage.py was 0% and now it is 100%. This was because there were no tests written for it initially. A new test file, `test_dialog.py`, was created containing a class `TestDialog` with tests. The function `fake_click` simulates a mouse click event and can fake either a button-down or button-up event using the Pygame library. To improve coverage, the following test cases were created:
- `test_fake_click_down` checks if the simulated mouse click event button down evaluates to true.
- `test_fake_click_up` checks if `fake_click(false)` is true, meaning the simulated mouse event was a button-up.

**Test 2:** `insort_right_w_key(a, x, lo=0, hi=None, key=lambda v: v)`
[Patch (diff) or commit link](https://github.com/gluglulim/singularity/commit/e6a47171edccc60917b7cb54b7704c52f140ee84)

**Old coverage results:** 
![Old coverage results](link-to-screenshot)

**New coverage results:**
![New coverage results](https://github.com/gluglulim/singularity/blob/master/link-to-screenshot/Zrzut%20ekranu%202024-06-27%20o%2018.40.23.png)

**Coverage improvement:**
The initial function coverage measurement was 0% due to the absence of tests. In `test_dialog.py`, the following test cases were created:
- `test_with_negative_lo`: tests if a value error occurs if `lo` is negative.
- `test_insert_with_none_hi`: checks if the function sets `hi` to the length of `a` when `hi` is None.
- `test_insert_into_empty_list`: checks if inserting a value into an empty list behaves correctly.
- `test_insert_into_sorted_list`: verifies correct insertion of an element into a sorted list.
- `test_insert_duplicates`: ensures that elements with equal values are inserted to the right side.

**Yuto Ishihara**

**Test 1:** `get_writable_file_in_dirs(filename, dir_name, outer_paths=None)`
[Patch (diff) or commit link](https://github.com/gluglulim/singularity/pull/3/commits)

**Old coverage results:** 
![Old coverage results](link-to-screenshot)

**New coverage results:**
![New coverage results](link-to-screenshot)

**Coverage improvement:**
The original result for `get_writable_file_in_dirs(filename, dir_name, outer_paths=None)` was 0%. This function aims to get writable files in `dir.py`. To improve coverage, tests were created for the following branches:
- Declare global variable `write_dirs`.
- Assign `write_dirs[dir_name]` to the variable.
- If `write_dir` is not None, update `branch_coverage["get_writable_file_in_dirs_1"]` to True and set `real_paths` accordingly.
- If the first statement is not None and `outer_paths` is not None, update `branch_coverage["get_writable_file_in_dirs_2"]` to True.
- Else, update `branch_coverage["get_writable_file_in_dirs_3"]` to True.

**Test 2:** `power_state_name(self)`
[Patch (diff) or commit link](link-to-commit)

**Old coverage results:** 
![Old coverage results](link-to-screenshot)

**New coverage results:**
![New coverage results](link-to-screenshot)

**Coverage improvement:**
The initial coverage for `power_state_name(self)` was 0%. This function updates the power state. Tests were created for the following branches:
- If `self.power_state` is "offline", update `branch_coverage["power_state_name_1"]`.
- If `self.power_state` is "active", update `branch_coverage["power_state_name_2"]`.
- If `self.power_state` is "sleep", update `branch_coverage["power_state_name_3"]`.
- If `self.power_state` is "overclocked", update `branch_coverage["power_state_name_4"]`.
- If `self.power_state` is "suicide", update `branch_coverage["power_state_name_5"]`.
- If `self.power_state` is "stasis", update `branch_coverage["power_state_name_6"]`.
- If `self.power_state` is "entering_stasis", update `branch_coverage["power_state_name_7"]`.
- If `self.power_state` is "leaving_stasis", update `branch_coverage["power_state_name_8"]`.

**Marika Litwiniak**

**Test 1:** `suspicion_to_danger_level(suspicion)`
[Patch (diff) or commit link](https://github.com/gluglulim/singularity/commit/40f5977ca6f00075fa292ff83ab6ae30847f322c)

**Old coverage results:** 
![Old coverage results](link-to-screenshot)

**New coverage results:**
![New coverage results](link-to-screenshot)

**Coverage improvement:**
The `suspicion_to_danger_level(suspicion)` function had 0% coverage. Tests were created for the following branches:
- If `suspicion < 2500`, return 0.
- If `suspicion < 5000`, return 1.
- If `suspicion < 7500`, return 2.
- Else, return 3.

**Test 2:** `nearest_percent(value, step=100)`
[Patch (diff) or commit link](https://github.com/gluglulim/singularity/commit/40f5977ca6f00075fa292ff83ab6ae30847f322c)

**Old coverage results:** 
![Old coverage results](link-to-screenshot)

**New coverage results:**
![New coverage results](link-to-screenshot)

**Coverage improvement:**
The `nearest_percent(value, step=100)` function had 0% coverage. Tests were created for the following branches:
- If `2 * sub_percent <= step`, return `value - sub_percent`.
- Else, return `value + (step - sub_percent)`.

## Overall

**Old coverage results by running an existing tool:**
![Old coverage results (Windows)](link-to-screenshot)
![Old coverage results (Mac)](link-to-screenshot)

**New coverage results by running the existing tool using all test modifications:**
**New coverage on Windows:** After the merge, the overall coverage test showed 35% total percentage. However, the newly generated tests proposed had over 80% coverage. Some tests failed in areas we did not modify.

**New coverage result on Mac:** Improved from 53% to 55%. All functions chosen are at least 80%.

## Statement of individual contributions
**Youngchae Lim**  
Functions: `strip_to_null(a_string)`, `detect_chance_to_danger_level(detects_per_day)`  
Focused on instrumentation and testing these functions from project singularity to gather coverage measurements. Test cases included scenarios such as checking for empty strings, leading spaces, trailing spaces, and different detection counts per day in the project software.

**Wiktoria Zaręba**  
Functions: `fake_click(down)`, `insort_right_w_key(a, x, lo=0, hi=None, key=lambda v: v)`  
Responsible for creating new tests for these functions, resulting in a 100% coverage improvement for the first function and 98% coverage for the second function. Tests were created in `test_dialog.py`.

**Yuto Ishihara**  
Functions: `get_writable_file_in_dirs(filename, dir_name, outer_path=None)`, `power_state_name(self)`  
Developed test cases to cover all branches of these functions, improving coverage from 0% to 92% (first function) and to 87% (second function). Also checked for grammar mistakes in the report.

**Marika Litwiniak**  
Functions: `suspicion_to_danger_level(suspicion)`, `nearest_percent(value, step=100)`  
Responsible for writing tests for the chosen functions, improving their coverage from 0% to 100%. Contributed to coverage analysis and writing the introduction and overall part of the report.

Our group proceeded with this task through periodic meetings online/offline, found projects together, and shared testing methods and ideas.
