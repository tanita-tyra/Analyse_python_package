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
* Summarises the data into a dictionary of mean, median, maximum, minimum and unbiased standard deviation and variance of the input values. 
* These are summarized components of [descriptive statistics](https://conjointly.com/kb/descriptive-statistics/) to describe basic features of the data. This function aims to give central tendency of the data as well as its unbiased spread around the central tendency.

**Function 2: `five_num_summary`**
* Calculates a [five number summary](https://www150.statcan.gc.ca/n1/edu/power-pouvoir/ch12/5214877-eng.htm#:~:text=Five%2Dnumber%20summaries,-Archived%20Content&text=A%20five%2Dnumber%20summary%20is,upper%20quartiles%2C%20and%20the%20median.) of the data and returns it as a dictionary of mean, median, maximum, minimum, 1st quartile and 3rd quartile.
* These values give a summary of a data set whereby each value describes a specific part of a data set: the median identifies the centre of a data set; the upper and lower quartiles span the middle half of a data set; and the highest and lowest observations provide additional information about the actual dispersion of the data. This is a useful descriptive analyses during the preliminary investigation of a large data set.

**Function 3: `date_parser`**
* Converts date list string formart from 'yyyy-mm-dd hh:mm:ss' to 'yyyy-mm-dd'.
* This function assist with making the date format to be more focus on the exact date excluding the time of day. 

**Function 4: `extract_municipality_hashtags`**
* Takes in a pandas dataframe and returns a modified dataframe that includes two new columns. New column 'municipality' contains manucipality name while 'hashtags' contains hashtags used, these are replaced by NaN when not found.

**Function 5: `number_of_tweets_per_day`**
* Takes in pandas dataframe as input and returns a new dataframe, grouped by `Date` in `yyyy-mm-dd` format and the corresponding number of `'Tweets'` for that day in separate column.

**Function 6: `word_splitter`**
* Takes pandas dataframe and splits the sentences in a dataframe's column into a list of the separate word and place them in a new column named `Split Tweets` in the original dataframe.

**Function 7: `stop_words_remover`**
* Takes in pandas dataframe and removes english stop words from a tweet. Stop words are assigned to variable `stop_words_dict` and the resulting list is plced in a column labeled `"Without Stop Words"`.
* Using stop_words_remover helps with decreasing the dataset size and the time to train the model. It also helps improve the performance as there are fewer and only meaningful tokens left. It also helps with fast retrieval of data from the database.

## Requirements for use:
* Internet access is required.

* Pandas and numpy library.

* Note: This package was tested on a Jupyter notebook and Anaconda prompt.

## How to install the package:
> For ease usage, follow these steps:
    1. Download the zipped-file on this [GitHub repo](https://github.com/tanita-tyra/Analyse_python_package)
    2. Extract all file in the same working directory
    3. Copy the path where you saved the files
    4. Using prompt, issue the command below to install the package from GitHub. You must be in the same working directory as in number 3.

`pip install git+https://github.com/tanita-tyra/Analyse_python_package.git`

* If you need to install a later version of your package, then use:

`pip install --upgrade git+https://github.com/tanita-tyra/Analyse_python_package.git`

* The package should now be installed and ready for setup and usage.

## How to setup the package: 
* Open the working directory in Jupyter Notebook.

* mymodule file should the be imported from myPackage folder as shown below.

![](https://github.com/tanita-tyra/Analyse_python_package/blob/master/mymodule%20import.PNG?raw=true)

> NB: Ensure correct usage of folder and module name.

## Using the package:
* Use the module.funtion() format where module will be the name used when importing. In the above example we used `mm` as our name, this is how we would then use it for function 1:

![](https://github.com/tanita-tyra/Analyse_python_package/blob/master/Example%20of%20using%20the%20package.PNG)

## How to contribute:
* Reach out to any of the contributors, they will be happy to assit with further directives.
