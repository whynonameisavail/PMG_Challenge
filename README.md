# PMG_Challenge
A solution to https://github.com/AgencyPMG/ProgrammingChallenges/tree/master/csv-combiner. 

Run: ```python3 combiner.py ./fixtures/accessories.csv ./fixtures/clothing.csv > combined.csv``` to get the correct combined file. 

Several error handlings: 

```python3 combiner.py ./fixtures/accessories.csv ./fixtures/clothin.csv > test_nonexist_path.csv``` to test the case when input contains an non-existing path. The result is written in ```test_nonexist_path.csv```. 

```python3 combiner.py ./fixtures/clothing.csv > test_one_file.csv``` to test the case when input only contains one file path. The result is written in ```test_one_file.csv```. 

```python3 combiner.py > test_wrong_arg_number.csv``` to test if the input arg number is not correct. The result is written in ```test_wrong_arg_number.csv```. 
