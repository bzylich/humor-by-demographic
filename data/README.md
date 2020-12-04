# data

## train.csv

train.csv is the 8k dataset released by Hahackathon - [here](https://competitions.codalab.org/competitions/27446#participate). While the dev set was unrelased, we had created a 90-10 split for our experiments. 

### data information

Each row has a unique identifier, the text, and the following values to be predicted:

* The label of the text: is_humor.  This is based on the majority class given by 20 annotators. In the rare cases where the votes were tied, the humor label was selected. 
* The humor rating, based on the average rating given by 20 annotators 
* Humor controversy (i.e. the variance of the rating between annotators is higher than the median variance )
* Offense rating

### train_split
This folder has the 90-10 split we had created of train.csv

## public_dev.csv

public_dev.csv is the dev set shared by Hahackathon. It contains 1000 text sentences - [here](https://competitions.codalab.org/competitions/27446#participate). This is the dataset used by the event to measure our model performance. 

This dataset does not contain labels and evaluation is only available by submitting predictions to the leaderboard. We use this as our final test set since the actual test set for the competition is not released until after the project deadline.

## trial_data.csv

trial_data.csv is the shared csv by Hahackathon - [here](https://competitions.codalab.org/competitions/27446#participate)


## reddit_compiled.csv

reddit_compiled.csv is the dataset we collect from reddit. It contains 200k posts

## public_test.csv
public_test.csv is the dataset released by the event organizers for use as the public dataset for model evaluation, this would be used in January for the competiotion. 

### data information

60 texts

A humor classification based on the majority vote from all answers to question 1 (is_humor_all) and a humor score which is the average of all ratings given by users to question 2. 

Each text has offensiveness classification based on the majority vote from all answers to question 3 (is_off_all) and an offensiveness score, whcih is the average of all ratings given by users to question 4. 

Binned these annotations based on four age groups (18-25, 26-40, 41-55, 56-70), 
and two gender identities (male and female). 

The humor classification results are not binned into these groups, as this is considered to be a relatively objective question, and the responses were homogeneous across groups. However, the offensiveness classification results are broken down into age/gender groups, and are the majority decision of the group. These are found under ‘is_off_18_25’ or ‘is_off_female’, etc. 

The humor ratings and offensiveness ratings are also binned by group and are found under ‘offense_41_55’ or ‘offense_male’ etc. As noted above if the majority vote did not class the text as humorous or offensive, the humor or offensiveness score for this text will be blank. 

