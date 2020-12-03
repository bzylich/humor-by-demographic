# Joint Modeling of Humor and Offense
 
 This repo is for our 685 - Final Project & SemEval'21 Event 7. 


Humor classification is one the hardest problem in the area of Natural Language Understanding.  In this project, we explore different pre-trained models and ensembles to combine and classify humor and offensive detection.

We develop a jokes classifier by fine-tuning pre-trained (BERT, RoBERTa, ...) to classify jokes and attempt to predict ..  

This is down to the observation that what is humorous to one user, may be offensive to another.

## Datasets
- Hahackathon dataset (https://competitions.codalab.org/competitions/27446)
- 200k short texts for humor detection (https://www.kaggle.com/moradnejad/200k-short-texts-for-humor-detection, binary humor/not humor labels)
- Hate speech/offensive language/clean speech (https://github.com/t-davidson/hate-speech-and-offensive-language)
- Offensive Tweets (https://sites.google.com/site/offensevalsharedtask/olid, binary offensive, targeted/untargeted insult, targeted at individual, group, or other)


## Notebooks

Jupyter notebook is run on Google Colab, any extra package requried is being included in the notebook itself.

## Libraries
- PyTorch
- Transformers (https://github.com/huggingface/transformers)
- SpaCy
- Pandas
- Numpy


## Results
