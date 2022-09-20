# Notes for viewers

* Changes in Github after the submission deadline (29/08/2022 onwards) only contain file renaming and creation of 2 extra folders for better navigation. Check history of commits for proof.
* All notebooks whose names start with 'PD' stand for Post-Dissertation and are not meant to be marked. These notebooks are created for further work with S2R Analytics as a part-time job.

To install all dependenceis and libraries, run the following line in your terminal:
```r
git clone https://github.com/marfappv/dissertation.git
pip install -r requirements.txt
```

The main files you want to have a look at are:
* ETL/data_transformation.ipynb
* ML/binary/recoverability.ipynb
* ML/binary/profitability.ipynb

Files that are NOT included in the repository:
* all CSV files due to their size and data sensitivity;
* Jupyter Notebook checkpoints as they keep changing locally, so Github always gives an error when pushing;
* virtual environmemnt files ('venv' folder).

## Project abstract

This paper reports business approach and technicalities of predicting recoverability and profitability for projects in the Architecture, Engineering, Construction industry (AECI). This project was made possible thanks to S2R Analytics (henceforth, S2R) who kindly provided data of one of their clients – an engineering company Client X (real name of the company is withheld due to data sensitivity). S2R is interested to learn about predictors of profitability of the client’s projects, while Client X is more concerned about their recoverability. 

Incorporating evidence from literature reviews and 154 classification models, this study reveals that top predictors for both metrics are the same: (1) quality of data health prior the start of the project, (2) project size, (3) project complexity level based on the number of stagesit has, (4) default rate group of project charge, and (5) percentage of stages with fixed fee. This discovery is counter-intuitive, considering the trade-off between recoverability and profitability, briefly covered in the paper. Since the project examined the two targets in isolation from each other, further research should be done on the inverse relationship between them, graphically reminding a Production Possibility Frontier (PPF) curve in macroeconomics.

To maximise recoverable amount and profit margin of their projects, AEC companies are advised to set up data maintenance practices and run data quality checks before agreeing on the project’s rate group charge. Based on statistically insignificant drivers of profitability and recoverability, companies can be more relaxed about decision-making in human resources, like percentage of subcontractors hired for the project, and longevity of project leads’ employment at the company. The final models succeeded to predict recoverability class with 88.8% precision, and profitability class with 82.7% precision.