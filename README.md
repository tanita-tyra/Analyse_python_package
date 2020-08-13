#mypackage 

# Python package with seven functions to calculate and analyse data from Eskom.

## [About Eskom](http://www.eskom.co.za/OurCompany/CompanyInformation/Pages/Company_Information.aspx)
* Eskom is a State-owned and supported electricity utility in South Africa.
* It operates 30 power stations with total nominal capacity of 44 172MW.
* Plants: coal-fired, gas turbines, hydroelectric, pumped storage and nuclear units.
* It supplies 6.2 million (and growing) direct customers  - public and municipalities.

## Eskom Crisis: [Load shedding](https://loadshedding.eskom.co.za/LoadShedding/Description)
* Eskom has been under the challenge of load shedding since December 2014.
* __Load-shedding__ is when there is insufficient power station capacity to supply the demand (load) for all the customers.
* To prevent shut-down of plants, parts of the network are switched off in a planned and controlled manner. In simple terms, some parts of the country experience power outage for a specified period of time. 
* The most effective solution is to build more power plants, but huge plants take many years to build, hence any applicable solutions should be considered towards this bigger solution. 

## About the package
* This package is created to assist in acquiring metrics that can be used in calculating and analysing data from Eskom. 
* It contains a module (named mymodule.py) containing seven functions that serve various aims of the package:

**Function 1: `dictionary_of_metrics`**
* Summarises the data into a dictionary of mean, median, maximum, minimum and unbiased standard deviation and varience. 

**Function 2: `five_num_summary`**
* Calculates a five number summary of the data and returns it as a dictionary of mean, median, maximum, minimum, 1st quartile and 3rd quartile.

**Function 3: `date_parser`**
* Converts date list string formart from 'yyyy-mm-dd hh:mm:ss' to 'yyyy-mm-dd'.

**Function 4: `extract_municipality_hashtags`**
* Takes in a pandas dataframe and returns a modified dataframe that includes two new columns. New column 'municipality' contains manucipality name while 'hashtags' contains hashtags used, these are replaced by NaN when not found.

**Function 5: `number_of_tweets_per_day`**
* Takes in pandas dataframe as input and returns a new dataframe, grouped by `Date` in `yyyy-mm-dd` format and the corresponding number of `'Tweets'` for that day in separate column.

**Function 6: `word_splitter`**
* Takes pandas dataframe and splits the sentences in a dataframe's column into a list of the separate word and place them in a new column named `Split Tweets` in the original dataframe.

**Function 7: `stop_words_remover`**
* Takes in pandas dataframe and removes english stop words from a tweet. Stop words are assigned to variable `stop_words_dict` and the resulting list is plced in a column labeled `"Without Stop Words"`.

## How to install the package:
* Internet access is required.

Issue the command below to install your package from GitHub. (make sure to replace your-name and your-repo with the appropriate text)

pip install git+https://github.com/your-name/your-repo.git

If you need to install a later version of your package, then use:

pip install --upgrade git+https://github.com/your-name/your-repo.git
