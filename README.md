*Sentiment Analysis on Financial Sector: Web-Scraping Tool*

Latest Commit : Implemented automative functionality via config file input, then tested with 'YAML_Config.yaml'. Results were complete. 

**Snscrape's ScraperException (Blocked requests)** : 
- snscrape.modules.twitter has dependencies on Twitter API. Occassionaly, social networks block their API from being accessed. 
- JustAnotherArchivist Github Ongoing / Resolved Issues https://github.com/JustAnotherArchivist/snscrape/issues  
- 4/20/2023 https://github.com/JustAnotherArchivist/snscrape/issues/783 - Most recent open issue

**Output :**
- .csv file(s) containing data
- Quantity of .csv files written match the quantity of documents contained inside a .yaml file

**Input :** 
- .yaml configuration file
- query_term (term / phrase)
- quantity (upper limit on tweets requested)
- handle (also known by Twitter as "username")
- filename (names the .csv file)
- start_date, end_date (specifies a date range for data extraction to occur) 

**'YAML_Config.yaml' :**
- .yaml config file with preset arguments
- Three dotted-lines "---" separates each Yaml document 
- Note 3 documents are contained within the file 
- You can increase / decrease the number of documents
- You can also change argument values 
- *Note : Do not edit parameter titles or 'main.py' will not run. 

**Useful info :**
- Minimum search criteria :
- None can be passed to any string argument to loosen query restrictions
- Either handle or query_term can accept None (not both)

- Phrases (query_term containing spaces) :
- Ex. phrase1 = 'United health care' --> without double quotes around phrase --> output: tweets containing the 3 terms in no particular order or context
- Ex. phrase2 = ' "United health care" ' --> with double quotes around phrase --> output: tweets with exact match to a phrase in correct order





