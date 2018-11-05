This is my Insight Data Engineering Fall 2018 Coding Challenge Submission. 

The run.sh bash script calls to the h1b_counting.py python script, with the module
h1bwrite. The arguments for h1bwrite should be the input dataset path, the output
dataset paths in the order of occupations and states, and the variable names for
soc name, certification status, and state, in that order. 

Here are the steps to running this script:

1. Decide on the input dataset and make sure it's in the input folder in the 
   codingchallenge_h1b_statistics directory (default H1B_FY_2014.csv, but also 
   tested with H1B_FY_2015.csv). 
   NOTE: Given the size limitation, an edited/truncated version of H1B_FY_2014.csv
   is included in this repo.
2. Open the h1b_counting.py script in the src folder in a text folder or using
   any other preferred method and set the input path, output paths, and variable 
   names based on their name in the input. It is currently pre-set for h1B_FY_2014.csv.
3. Run gitbash or some other bash terminal and cd to the h1b_statistics directory.
4. Run chmod +x run.sh
5. Run ./run.sh
6. Check the output folder or open the output in bash to see if it worked!

And here are the steps for running the test script:

1. Decide on the input dataset and make sure it's in the input folder in the
   h1b_statistics/insight_testsuite/tests/(test_#)/input folder, the correct
   output files are in the output folder, and the arguments in the h1b_counting.py
   script in the main src folder are correct.
2. In run_tests.sh, on line 54, make sure the input dataset name is correct. So if the
   dataset is H1B_FY_2014.csv, that should show in two places on that line:
   cp -r ${GRADER_ROOT}/tests/${test_folder}/input/H1B_FY_2014.csv ${TEST_OUTPUT_PATH}/input/H1B_FY_2014.csv
3. Run gitbash or some other bash terminal and cd to h1b_statistics/insight_testsuite.
4. Run chmod +x run_tests.sh
5. Run ./run_tests.sh
6. The test should output as pass. You can inspect results.txt in the same folder as well.
