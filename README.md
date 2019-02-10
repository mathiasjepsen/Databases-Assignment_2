# Databases-Assignment_2
## Dependencies
* Python >=3.5
* MongoDB 
* PyMongo

## Execution
Clone the repository, and run the command below.
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
```
### Who is are the most mentioned Twitter users? (Provide the top five.)
```
@mileycyrus    — 3824
@tommcfly      — 3631
@ddlovato      — 2954
@DavidArchie   — 1106
@Jonasbrothers — 1068
```
### Who are the most active Twitter users (top ten)?
```
lost_dog        — 549
webwoke         — 345
tweetpet        — 310
SallytheShizzle — 281
VioletsCRUK     — 279
mcraddictal     — 276
tsarnick        — 248
what_bugs_u     — 246
Karen230683     — 238
DarkPiano       — 236
```
### Who are the five most grumpy (most negative tweets) and the most happy (most positive tweets)? (Provide five users for each group)
```
grumpy: lost_dog    – 549
        tweetpet    – 310
        webwoke     – 264
        mcraddictal – 210
        wowlew      – 210
            
happy:  what_bugs_u – 246
        DarkPiano   – 231
        VioletsCRUK – 218
        tsarnick    – 212
        keza34      – 211
```
