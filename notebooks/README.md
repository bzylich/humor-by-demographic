# notebooks



## gabriel-olid-davidson.ipynb:
This notebook was used to train single models for the fourth task (offensiveness score). In it you will find cells that initialize and train models, and run them on our test data and the competition dev data. The models can be pretrained on the olid and davidson datasets or not, depending on which cell you run. All of the models and training in here are based on the huggingface-transformers "Trainer" class and related classes, so refer to their documentation to better understand what is happening.

## brian-olid.ipynb

## ColBERT_3_dev.ipynb
This notebook uses the model described in the ColBERT  (Annamoradne-jad,  2020) paper. It is  a  pretrained  BERT  model  that  has been  finetuned  for  humor  prediction,  as  a  starting  point  for  intermediate  finetuning  (ColBERTHumor  +IF=200k)  and  as  a  pretrained  language model  for  the  standard  transfer  approach  (ColBERT Humor). In this approach we use  BERT  to  tokenize and generate sentence embeddings for texts.  It sends embedding outputs as input to a two-layered neural network that predicts the target value. We discuss the results in the project report.  

## data analysis.ipynb
This notebook has various data analysis, insights and statistic charts. We use it to explore the characteristics of the competition dataset. We discuss our findings in the project report. 


**Note:** For all the .ipynb files, the Jupyter notebooks were run on Google Colab, any extra packages required are included in the notebook itself.
