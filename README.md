# Joint Modeling of Humor and Offense
 
 This repo is for our 685 - Final Project & SemEval'21 Event 7. 


Humor classification is one the hardest problems in the area of Natural Language Understanding.  In this project, we explore different pre-trained models and ensembles to combine and classify humor and offensive detection.


We are able to achieve submissions with significant performance in all of the tasks (detailed more in the report). As of the end of day of the submission ofthe project report, our team holds a position in the top 3 for each of the tasks, and we hold the first rank for 3 of the 4 tasks, among 21 other com-peting teams. We discuss this in more detail in our report - (https://competitions.codalab.org/competitions/27446#results)

## Folder structure 

    .
    ├── notebooks               # Contains all the colab .ipynb used for model training and analysis
    ├── pipeline                # Contains all the .py files used for data collection and analysis
    ├── data                    # The data files (.csv) used in our work
    │   ├── train_split   		    # Has the 90-10 train-test (.csv) files that we use for internal evaluations
    ├── docs                    # Documentation files - project report
    │   ├── related_work   		   # Contains some of the relavent related work
    └── README.md

## Datasets
- Hahackathon dataset (https://competitions.codalab.org/competitions/27446)
- 200k short texts for humor detection (https://www.kaggle.com/moradnejad/200k-short-texts-for-humor-detection, binary humor/not humor labels)
- Hate speech/offensive language/clean speech (https://github.com/t-davidson/hate-speech-and-offensive-language)
- Offensive Tweets (https://sites.google.com/site/offensevalsharedtask/olid, binary offensive, targeted/untargeted insult, targeted at individual, group, or other)


## Notebooks

Jupyter notebook is run on Google Colab, any extra packages required are included in the notebook itself.

## Libraries
- PyTorch
- Transformers (https://github.com/huggingface/transformers)
- SpaCy
- Pandas
- Numpy

