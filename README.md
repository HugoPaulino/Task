# Task

This repo contains two tasks, product analysis and product classification. The task one is focus on product analysis using SQL and NO SQL databases. The second comprises the product classification with machine learning models.

## How to run the product analysis

In order to run the product analysis you need to have docker installed, after installed go the the product_analysis folder and run

`docker compose up`

This command will:

1. Create a container with Postgres sql database.
2. Create a table products, and fill the table with the dataset testset_B.tsv that can be found in **data** folder.
3. Create a MongoDB no sql database.
4. You can check the postgres database with adminer that will run in port 8080. With that tool you can connect to the postgres database and check the table creation and the table insertion.

Run the python script to get the results:

**Create a virtual environment:**

```
python -m venv venv 
source venv/bin/activate 
pip install -r requirements.txt
```
**After environment creation run code:**

`python app.py`

**Results**

You can check the results connected when connected to MongoDB using Compass.

3a.
| price      | pricerank |
| ----------- | ----------- |
| 14900      | 1       |
| 15900	     | 2        |
|16900|	3|
|17900|	4|
|18900|	5|
|19900|	6|
|20900|	7|
|21900|	8|
|22900|	9|
|23900|	10|
|23900|	10|
|23900|	10|
| ...||

3b. 
| min_hdd_gb      | max_hdd_gb |
| ----------- | ----------- |
| 500GB      | 2000 GB       |

3c. 
| median_ghz      | ram_gb |
| ----------- | ----------- |
| 2.5474382433668801      | 4       |
| 2.5389019239793524   | 8        |
| 2.5558011049723757   | 16        |

## How to run the product analysis

The first part of this job was the creation of a notebook where I've trained a model to classify products based on text.
After I did multiple experiments in the training the model I've save it as pickle to use it later in the REST-API.

Then a Rest api using FastAPI framework was created with a unit test to test the endpoint.


In order to run the code we have two ways, one is to create a virtual environment and run our application :


```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

The other is using a container:

on the folder product classification do:

`docker compose up -d`

This will initiate the product classification api,we can test it in :

`localhost:8085/docs`






## How to make the code production ready

1. Use a container seamsly improve the deployment process to multiple machines(already done).
2. Create a CI CD pipeline with stages: build, pre-commit(to lint and standerize the code), test and deploy.
3. Create a model version management. One posibility is using tags in gitlab to when someone changes the model the model will be saved in the artifact registry or in any other management.
4. Other possibility is to make use of MLflow, MLflow allows the track of all the experiments and models. Then we can use the best model trained to do the inference.





