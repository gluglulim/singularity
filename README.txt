# Report for Assignment 1
## Project chosen
Name: <singularity>
URL: <https://github.com/singularity/singularity>
Number of lines of code and the tool used to count it: <Lizard - 13782 lines of code>
Programming language: <Python>
## Coverage measurement
### Existing tool
<Inform the name of the existing tool that was executed and how it was executed>
 coverage.py 
<Show the coverage results provided by the existing tool with a screenshot>
Coverage results running in Window system : 35%
 
Coverage results running on Mac - 53%
### Your own coverage tool
<The following is supposed to be repeated for each group member>
<Youngchae Lim>
coverage results of files containing the selected functions :   
 
<Function 1 :detect_chance_to_danger_level(detects_per_day):>
<Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements>
https://github.com/gluglulim/singularity/commit/4e73ea0738c6ecbf3034df3e759ea95f03a06517
 

<Provide a screenshot of the coverage results output by the instrumentation>
 
 

<Function 2: def strip_to_null(a_string):>
https://github.com/gluglulim/singularity/commit/08aedf88f5f52ef68f8e529f729e07c1c8101706#diff-0b9aa73ce494f32270b58ee8500b17328a4390bce1e96a56b1883a8495f32ac3 
 

<Provide the same kind of information provided for Function 1>
 
 

<Wiktoria Zaręba> 
<Function 1: def fake_click(down):>
<Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements>
https://github.com/gluglulim/singularity/commit/c2e03bd393d17616687adc2e21958e2ff579fd08 

<Provide a screenshot of the coverage results output by the instrumentation>
  
<Function 2: def insort_right_w_key(a, x, lo=0, hi=None, key=lambda v: v): >
https://github.com/gluglulim/singularity/commit/c2e03bd393d17616687adc2e21958e2ff579fd08 
 
<Provide the same kind of information provided for Function 1>


<Yuto Ishihara>
  
<Function 1: get_writable_file_in_dirs(filename, dir_name, outer_paths=None):>
<Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements>
<Provide a screenshot of the coverage results output by the instrumentation>
  

<Provide a screenshot of the new coverage results>
 

<Function 2: def power_state_name(self):>
<Provide a screenshot of the coverage results output by the instrumentation>
 

<Provide a screenshot of the new coverage results>
 

<Marika Litwiniak> 
def suspicion_to_danger_level(suspicion)
https://github.com/gluglulim/singularity/commit/d5256cf1932fad94cb797bcdc035975bebb2b968

 
 
def nearest_percent(value, step=100)
 
https://github.com/gluglulim/singularity/commit/d5256cf1932fad94cb797bcdc035975bebb2b968

 

 ## Coverage improvement
 ### Individual tests
 
<The following is supposed to be repeated for each group member>
<Youngchae Lim>
 
<Test 1:def strip_to_null(a_string):>
 

<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>
https://github.com/gluglulim/singularity/pull/1/commits 
<Provide a screenshot of the old coverage results (the same as you already showed above)>
  
<Provide a screenshot of the new coverage results>
 
<State the coverage improvement with a number and elaborate on why the coverage is improved>
 	the def strip_to_null(a_string): was not covered by coverage test from coverage.py at all, it was 0%, and it improved from 0% to 90% with created own test which is checking three branches in the function ‘strip_to_null’ 
1.	Checking if the string is empty
2.	Checking if the first character is space 
3.	Checking if the last character is space
so, to ensure these branches were covered I created new test cases to give input with empty string, leading space and trailing space and both leading and trailing spaces. And these tests made all branches function were executed, thus it made branch coverage improved.
<Test 2: detect_chance_to_danger_level(detects_per_day): >
<Provide the same kind of information provided for Test 1>
<old coverage test result>
 
<improved result of coverage test>
 
<commit link of new test>
https://github.com/gluglulim/singularity/pull/1/commits
 
<State the coverage improvement with a number and elaborate on why the coverage is improved>
The function ‘def detect_chance_to_danger_level(detects_per_day):’ had 0% coverage result by exist coverage tool coverage.py. This function is designed to assess the danger level based on the number of detections per day in game. To improve coverage needed to make test cover all 4 branches
1.	if detects_per_day > 225 return 3
2.	elif detects_per_day > 150 return 2
3.	elif detects_per_day > 75 return 1
4.	else return 0.
For test these 4 branches we created test cases to cover each branch with given different input, for example,
Test case 1: when detects_per_day > 225, we gave 230 expected result 3.
Test case 2: when detects_per_day > 150, we gave 160 expected result 2.
Test case 2: when detects_per_day > 75, we gave 100 expected result 1.
Test case 2: when detects_per_day <= 75, we gave 50 expected result 0.
The test cases successfully covered each branch and improved coverage from 0% to 90%.

<Wiktoria Zaręba>
<def fake_click(down):>
<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>
 https://github.com/gluglulim/singularity/commit/5321ee6ae2ab8027c959b7c7a8947fb1eb90e2ea 
<Provide a screenshot of the old coverage results (the same as you already showed above)>
 
 
<Provide a screenshot of the new coverage results>
  
 

<State the coverage improvement with a number and elaborate on why the coverage is improved>
 The coverage measured with coverage.py was 0% and now it is 100%. The reason the coverage was 0% at first is because there was no test written for it. A new test file was created test_dialog.py that contains a class TestDialog and tests. The function fake_click function is used to fake a mouse click event and can either fake a button-down event or button-up event using the pygame library. In order to improve coverage 2 branches had to be covered
1.	if down
2.	else
the following test cases were made for the two branches
1.	test_fake_click_down checks whether the simulated mouse click event button down evaluates to true and has an assertion that only passes when branch 1 is executed
2.	test_fake_click_up checks if fake_click(false) is true meaning that the simulated mouse event was a button-up. The test includes an assertion that passes once the else branch is executed. 
Function 2
<def insort_right_w_key(a, x, lo = 0, hi = None, key = lambda v: v):>
 	https://github.com/gluglulim/singularity/commit/e6a47171edccc60917b7cb54b7704c52f140ee84 
<Provide the same kind of information provided for Test 1>
 
 
The initial function coverage measurement was 0% because there was no test written for this particular function. In the file test_dialog.py that already contains a test for fake_click, I created a function Test Dialog to include both test in one file and created the test cases for the following branches:
1.	if lo < 0
2.	if hi is None
3.	while lo < hi
4.	if x_key < mid_key
5.	else
The following test cases where made:
1.	test_with_negative_lo  this test will tests if a value error will occur if the value of the parameter lo is negative
2.	test_insert_with_none_hi this test checks how the function will behave when hi is none. It is supposed to set the value of hi to the length of a. If it does the assertion passes
3.	test_insert_into_empty_list checks if someone inserted one value into an empty list that only has that value so basically if the function's behavior is correct. 
4.	test_insert_into_sorted_list this test checks whether the insertion of an element to a non-empty sorted list is done correctly. 
5.	test_insert__duplicates element checks if the function inserts the element to the right side of the element with an equal value
All the tests were done with assertEqual except the first one. 

<Yuto Ishihara>
<test_get_writable_file_in_dirs.py>
 
<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>
https://github.com/gluglulim/singularity/pull/3/commits
 

<Provide a screenshot of the old coverage results (the same as you already showed above)>
  

<Provide a screenshot of the new coverage results>
  

<State the coverage improvement with a number and elaborate on why the coverage is improved>
 The original result for the coverage of function ‘get_writable_file_in_dirs(filename, dir_name, outer_paths=None)’ was 0% according to the tool coverage.py. The purpose of the usage of this function is to get files, that are writable, in the file dir.py.  To improve coverage needed to make test cover all 3 branches:
-	Declare global variable write_dirs
-	Assign the write_dirs[dir_name] to the variable
1.	If write_dir is not None, then update branch_coverage["get_writable_file_in_dirs_1"] to True state and real_paths to os.path.join(write_dir, filename) and (if statement 2 is None) then return real_paths, otherwise jump to statement 2
2.	If the statement 1 is not None and outer_paths is not None either, then update branch_coverage["get_writable_file_in_dirs_2"] to True state and append outer_path to real_path, then return real_path
3.	Else then update branch_coverage["get_writable_file_in_dirs_3”] to True then return None
we changed the functions as:
-	Assign write.get(dir_name) to the global variable write_dirs (All if-and-else statements are unchanged)
The test cases successfully covered both branches. Hence the coverage improved as it increased from 0% to 92%.

<test_power_state_machine.py>

<Provide a screenshot of the old coverage results (the same as you already showed above)>
 

<Provide a screenshot of the new coverage results>
 
 
<State the coverage improvement with a number and elaborate on why the coverage is improved>
 The original result for the coverage of function ‘power_state_name(value, step=100):’ was 0% according to the tool coverage.py. The purpose of the usage of this function is to update power state from the signal that the function gets.
To improve coverage needed to make test cover all 8 branches:
1.	If self.power_state is “offline”, then branch_coverage[“power_state_name_1”] return “Offline”
2.	If self.power_state is “active”, then branch_coverage[“power_state_name_2”] return “Active”
3.	If self.power_state is “sleep”, then branch_coverage[“power_state_name_3”] return “Sleep”
4.	If self.power_state is “overclocked”, then branch_coverage[“power_state_name_4”] return “Overlocked”
5.	If self.power_state is “suicide”, then branch_coverage[“power_state_name_5”] return “Suicide”
6.	If self.power_state is “stasis”, then branch_coverage[“power_state_name_6”] return “Stasis”
7.	If self.power_state is “entering_stasis”, then branch_coverage[“power_state_name_7”] return “Entering_stasis”
8.	If self.power_state is “leaving_stasis”, then branch_coverage[“power_state_name_8”] return “Leaving_stasis”
9.	Else, it returns “”
we changed the function as:
1.	If self.power_state is “offline”, then branch_coverage[“power_state_name_1”] will be True and return “Offline”
2.	If self.power_state is “active”, then branch_coverage[“power_state_name_2”] will be True and return “Active”
3.	If self.power_state is “sleep”, then branch_coverage[“power_state_name_3”] will be True and return “Sleep”
4.	If self.power_state is “overclocked”, then branch_coverage[“power_state_name_4”] will be True and return “Overlocked”
5.	If self.power_state is “suicide”, then branch_coverage[“power_state_name_5”] will be True and return “Suicide”
6.	If self.power_state is “stasis”, then branch_coverage[“power_state_name_6”] will be True and return “Stasis”
7.	If self.power_state is “entering_stasis”, then branch_coverage[“power_state_name_7”] will be True and return “Entering_stasis”
8.	If self.power_state is “leaving_stasis”, then branch_coverage[“power_state_name_8”] will be True and return “Leaving_stasis”
9.	Else, it returns “”

The test cases successfully covered both branches. Hence the coverage improved as it increased from 0% to 93%

<Marika Litwiniak>
 
<test_suspicion.py>

 	https://github.com/gluglulim/singularity/commit/40f5977ca6f00075fa292ff83ab6ae30847f322c

 
 
  
<State the coverage improvement with a number and elaborate on why the coverage is improved>
The function ‘suspicion_to_danger_level(suspicion)’ had 0% coverage result according to the coverage tool coverage.py. To improve the coverage the test needed to cover all 4 branches:
1.	if suspicion < 2500 return 0
2.	elif suspicion < 5000 return 1
3.	elif suspicion < 7500 return 2
4.	else return 3.
To test these 4 branches we created test cases to cover each branch using different input : 
Test case 1: when suspicion < 2500, we gave 1000 and expected result == 0.
Test case 2: when suspicion < 5000, we gave 3000 and expected result == 1.
Test case 3: when suspicion < 7500, we gave 6000 and expected result == 2.
Test case 4: when suspicion >= 7500, we gave 8000 and expected result == 3.
The test cases successfully covered each branch and improved the function coverage from 0% to 100%, the file coverage increased by 4% (from 70% to 74%)
 
<test_nearest.py>
 https://github.com/gluglulim/singularity/commit/40f5977ca6f00075fa292ff83ab6ae30847f322c
 
 
The function ‘nearest_percent(value, step = 100)’  had 0% coverage result according to the coverage tool coverage.py. To improve the coverage the test needed to cover all 2 branches:
1.	if 2 * sub_percent <= step return value - sub_percent
2.	else return value + (step - sub_percent).
To test these 2 branches we created test cases to cover each branch using different input : 
Test case 1: when 2 * sub_percent <= step return value - sub_percent, we gave ‘value’ = 140 and expected result == 100.
Test case 2: when 2 * sub_percent > step return value - sub_percent, we gave ‘value’ = 180 and expected result == 200.
The test cases successfully covered each branch and improved the function coverage from 0% to 100%, the file coverage increased by 2% (from 74% to 76%)

### Overall
 
<Provide a screenshot of the old coverage results by running an existing tool (the same as you already showed above)>
  
<old coverage results left : window, right : mac OS>
 
<Provide a screenshot of the new coverage results by running the existing tool using all test modifications made by the group>
  
New coverage on Window : After the merge, the coverage test showed the same 35% total percentage. However, the newly generated tests we proposed were definitely over 80% after the merge.
When we compared the test results, we found that some tests failed in the system part we didn’t touch.
 
New coverage result on Mac: 55%
The overall coverage result on Mac system improved from 53% to 55% but all functions chosen are at least 80%.

## Statement of individual contributions
<Write what each group member did>
Youngchae Lim
-	Functions: ‘strip_to_null(a_string)’, ‘detect_chance_to_danger_level(detects_per_day)’
-	Focused on instrumentation and testing these functions from project singularity to gather coverage measurements. Test cases included scenarios such as checking for empty strings, leading spaces, trailing spaces, and different detection counts per day in the project software
Wiktoria Zaręba
-	Functions: ‘fake_click(down)’, ‘insort_right_w_key(a, x, lo = 0, hi = None, key = lambda v: v):’
-	Responsible for creating new tests for these two test functions, her efforts resulted in a 100% coverage improvement for the first function and 98% coverage for the second function.
-	The first function fake_click was tested in file test_dialog.py and the second function is tested in the file test_insort.
-	Both test were created (there was no testing provided for any of the function)
-	The contribution for the report is all the coverage analysis for 2 chosen functions and the description of the testing as well as the overall coverage of the project before and after

Yuto Ishihara
-	Functions: ‘get_writable_file_in_dire(filename, dir_name, outer_path=None)’, ‘power_state_name(self)’
-	Developed test cases to cover all branches of these functions, improving the coverage from 0% to 92% (for the first test) and to 87% (for the second test)
-	The contribution of the report is to check everyone’s codes in order to avoid any conflict. Then I figured out that I was accidentally using the same code as another member so I could switch to another function before it's too late. I also checked for grammar mistakes and actually corrected some of them.
Marika Litwiniak
-	Functions: ‘suspicion_to_danger_level(suspicion)’,  ‘nearest_percent(value, step = 100)’
-	Responsible for writing tests for the two chosen functions, and improving both of their coverage from 0% to 100% 
-	Provided coverage analysis for the chosen functions and contributed in writing the intro and overall part of the project's report

Our group proceeded with this task, and through periodic meetings online/offline, we found projects for the task together and shared testing methods and ideas with each other.
