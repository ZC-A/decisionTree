# DecisionTree

A decision tree implemented by Hunt's Algorithm.

## Dataset

- training set : adult.data
- evaluation set : adult.test
- Listing of attributes
  - label : `>50K`, `<=50K`
  - attribute: `age`, `workclass`, `fnlwgt`, `education`, `education-num`, `marital-status`, `occupation`, `relationship`, `race`,`sex`, `capital-gain`, `capital-loss`, `hours-per-week`, `native-country`, `income`

## Usage

You can run the code with the following command :

```
python main.py
```

then you can train a new tree and evaluate this decision tree using `adult.test` by entering following operations and All results will be displayed on the terminal :

- T for training new tree and save
- E for using current tree to evaluate (which will be error if no tree load or train before)
- Q for quit

## File Structure

### Source  Codes

- `load.py` : preprocess the raw data,remove specified columns and missing values,use binary to read from `tree.pickle` or write decision trees into `tree.pickle`
- `train.py`:implemente the Hunt's algorithm to create Decision tree, it can process both ordinal attributes and  nominal attributes.
- `evaluate.py`:evaluate this decision tree using `adult.test`
- `struture.py`:define decision tree node
- `main.py`: execute and display result

## Documentation


1. - `tree.pickle`:decision trees can be written into `tree.pickle`
   - `output.txt`: visualize binary decision tree and describe the decision tree built from the Adult training set
   - `res.csv`: the test dataset and it's evaluation result, the last column represents whether this row evaluated correctly
2. 
    - the decision tree built from the Adult training set can be found in the output of `train.py`, it shows the best split attribute and its GINI value for each iteration.
    - evaluation correct number: 12694
    - evaluation correct rates: 0.8428950863213811
