# data

## trial_data.csv

trial_data.csv is the shared csv by Hahackathon - [here](https://competitions.codalab.org/competitions/26083#participate)

### data information

60 texts

A humor classification based on the majority vote from all answers to question 1 (is_humor_all) and a humor score which is the average of all ratings given by users to question 2. 

Each text has offensiveness classification based on the majority vote from all answers to question 3 (is_off_all) and an offensiveness score, whcih is the average of all ratings given by users to question 4. 

Binned these annotations based on four age groups (18-25, 26-40, 41-55, 56-70), 
and two gender identities (male and female). 

The humor classification results are not binned into these groups, as this is considered to be a relatively objective question, and the responses were homogeneous across groups. However, the offensiveness classification results are broken down into age/gender groups, and are the majority decision of the group. These are found under ‘is_off_18_25’ or ‘is_off_female’, etc. 

The humor ratings and offensiveness ratings are also binned by group and are found under ‘offense_41_55’ or ‘offense_male’ etc. As noted above if the majority vote did not class the text as humorous or offensive, the humor or offensiveness score for this text will be blank. 

