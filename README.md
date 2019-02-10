# Databases-Assignment_2
## Dependencies
* Python >=3.5
* MongoDB 
* PyMongo

## Execution
Clone the repository, and move into Databases-Assignment_2/
```
git clone git@github.com:mathiasjepsen/Databases-Assignment_2.git && cd Databases-Assignment_2/
```
Then simply run the following command, which will download the .csv file, unzip it, import its content into Mongo as a new database called _social_net_, and execute the five queries sequentially.
```
python twitter_data_analysis.py
```
You may need to substitute _python_ with _python3_ if you have multiple versions of Python installed.

## Results

### How many Twitter users are in the database?
```
659775
```
### Which Twitter users link the most to other Twitter users? (Provide the top ten.)
```
lost_dog        — 549
tweetpet        — 310
VioletsCRUK     — 251
what_bugs_u     — 246
tsarnick        — 245
SallytheShizzle — 229
mcraddictal     — 217
Karen230683     — 216
keza34          — 211
TraceyHewins    — 202
