# Joint Modeling of Humor and Offense
 
 This repo is for our 685 - Final Project & SemEval'21 Event 7. 


Humor classification is one the hardest problem in the area of Natural Language Understanding.  In this project, we explore different pre-trained models and ensembles to combine and classify humor and offensive detection.

We develop a jokes classifier by fine-tuning pre-trained (BERT, RoBERTa, ...) to classify jokes and attempt to predict ..  

This is down to the observation that what is humorous to one user, may be offensive to another.

## Datasets

- 200k short texts for humor detection (https://www.kaggle.com/moradnejad/200k-short-texts-for-humor-detection, binary humor/not humor labels)
- Humicroedit- edited news titles (https://www.cs.rochester.edu/u/nhossain/humicroedit.html, continuous funniness labels- averaged)
- Puns, short jokes, mixed jokes Reddit, etc. (https://github.com/orionw/RedditHumorDetection, some jokes separated into setup and punchline, binary joke/non-joke, binary pun/non-pun, Reddit upvotes)
- English joke dataset (https://github.com/taivop/joke-dataset)

- Hate speech/offensive language/clean speech (https://github.com/t-davidson/hate-speech-and-offensive-language)
- Hate speech Twitter (https://github.com/ZeerakW/hatespeech, requires scraping twitter using tweet IDs and annotations)
- Offensive Tweets (https://sites.google.com/site/offensevalsharedtask/olid, binary offensive, targeted/untargeted insult, targeted at individual, group, or other)


## Notebooks

Jupyter notebook is run on Google Collab, any extra package requried required is being included in the notebook itself.

## Libraries
- PyTorch
- Transformers (https://github.com/huggingface/transformers)



## Results
