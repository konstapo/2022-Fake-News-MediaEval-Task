# FakeNews: Corona Virus and Conspiracies Multimedia Analysis Task
### Fighting against misinformation spreading

The FakeNews Detection task explores various machine-learning approaches to automatically detect misinformation and its spreaders in social networks.

Spontaneous and intentional digital FakeNews wildfires over online social media can be as dangerous as natural fires. A new generation of data mining and analysis algorithms is required for early detection and tracking of such information cascades. This task focuses on the analysis of tweets, public user properties and their connections related to Coronavirus conspiracy theories in order to detect conspiracies and misinformation spreaders.


## Announcements
* **30 August 2021:** The development and test datasets are released.

## Task Schedule
* 30 August: Development and test datasets release
* 5 November: Runs due
* 10 November: Results returned
* 20 November: Working notes paper due
* December: MediaEval 2022 Workshop


## Task Description

The FakeNews Detection Task offers three fake news detection subtasks on COVID-19-related conspiracy theories. The first subtask includes text-based topics and conspiracy detection. The second subtask asks for graph based detection of conspiracy theory posters in a social network graph with node attributes. The third subtasks combine the two, aiming topic and conspiracy detection based on both graph and textual data. 
All subtasks are related to misinformation disseminated in the context of the COVID-19 pandemic. We focus on conspiracy theories that assume some kind of nefarious actions by governments or other actors related to CODID-19, such as intentionally spreading the virus, lying about the nature of the pandemic, or using vaccines that have some hidden functionality and purpose.

***Text-Based Misinformation and Conspiracies Detection***: In this subtask, the participants receive a dataset consisting of tweet text blocks in English related to COVID-19 and various conspiracy theories. The goal of this subtask is to build a complex multi-labelling multi-class detector that for each topic from a list of nine categories of conspiracy theories can predict whether a tweet promotes ideas in that category, discusses ideas from that category, or discusses a topic unrelated to that category. This task is identical to a task posed in last year’s challenge, but it uses a larger development and test datasets.  

***Graph-Based Conspiracy Source Detection***: In this subtask, the participants are given a directed graph derived from Twitter where the vertices are users and the edges represent interactions between them. Each vertex has a set of attributes, including location and number of followers. Edges have weights that represent the strength of interactions between users. Users who posted the misinformation preading tweets (promoting any of conspiracy ideas) from subtask 1 are labeled as misinformation spreaders, while users who posted non-misinformation tweets (just discussing or criticizing any of conspiracies or posting non-conspiracy-related tweets) are labeled as non-misinformation spreaders. Just like in subtask 1, labels belonging to the the test set are hidden. This subtask asks participants to predict the labels of all users in the graph, based on their connection to the labeled users as well as their attributes. Scoring will be based on correctly classifying users/vertices in the graph that have manually generated hidden labels. 

***Graph and Text-Based Conspiracy Detection***: this subtasks combines the data of both subtasks above with the aim of improving the text-based classification. For each text to be evaluated, the vertex corresponding to the author is specified in the graph. The goal of this subtask is the same as that of subtask 1, but participants can make full use of the graph data and vertex attributes. This subtask will use the same development and a different test set from that of subtask 1.


#### Motivation and Background
Digital wildfires, i.e., fast-spreading inaccurate, counterfactual, or intentionally misleading information, can quickly permeate public consciousness and have severe real-world implications, and they are among the top global risks in the 21st century. While a sheer endless amount of misinformation exists on the internet, only a small fraction of it spreads far and affects people to a degree where they commit harmful and/or criminal acts in the real world. The COVID-19 pandemic has severely affected people worldwide, and consequently, it has dominated world news for months. Thus, it is no surprise that it has also been the topic of a massive amount of misinformation, which was most likely amplified by the fact that many details about the virus were unknown at the start of the pandemic. This task aims at the development of methods capable of detecting such misinformation. Since many different misinformation narratives exist, such methods must be capable of distinguishing between them. For that reason we consider a variety of well-known conspiracy theories related to COVID-19.   


#### Target Group
The task is of interest to researchers in the areas of online news, social media, multimedia analysis, multimedia information retrieval, natural language processing, and meaning understanding and situational awareness to participate in the challenge. The target knowledge areas include Machine and Deep Learning, Natural Language Processing, and Graph Analytics Algorithms.


#### Data
The datasets contain several sets of tweet texts mentioning Corona Virus and different conspiracy theories and corresponding directed graph of user connections derived from social network data where the vertices are users and the edges represent connections between them. The tweet-text sets consist of only English language posts and it contains a variety of long tweets with neutral, positive, negative, and sarcastic phrasing. The vertices of user-graph contain a set of user attributes. The datasets are not balanced with respect to the number of samples of conspiracy-promoting and other tweets, the number of tweets per conspiracy class, and the graph structures. The dataset items have been collected from Twitter during a period between 20th of January 2020 and 1st of April 2022, by searching for the Corona-virus-related keywords (e.g., “corona”, “COVID-19”, etc.) inside the tweets’ text, followed by a search for keywords related to the conspiracy theories. Since not all tweets and users are available online, the participants will be provided a full-text set of already downloaded tweets as well as the user connection graph and user properties captured at the moment of captring the user-posted tweets. In order to be compliant with the Twitter Developer Policy, only the members of the participants’ participating teams are allowed to access and use the provided dataset. Distribution, publication, sharing and any form of usage of the provided data apart from the research purposes within the FakeNews task is strictly prohibited. A copy of the dataset in form of Tweet ID and annotations will be published after the end of MediaEval 2022.



#### Ground truth

The ground truth for the provided dataset was created by the team of well-motivated students and researchers using an overlapping annotation process with the following cross-validation and verification by an independent assisting team.


#### Evaluation methodology

Evaluation will be performed using standard implementation of the multi-class generalization of the Matthews correlation coefficient [MCC](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.matthews_corrcoef.html) computed on the optimally threshold conspiracy promoting probabilities (threshold that yields the best MCC score).


## Dataset

### Overview

The dataset consists of three development and three test sets containing full-text tweet bodies. Development sets are annotated differently for different subtasks: ***Text-Based Misinformation and Conspiracies Detection*** and ***Graph and Text-Based Conspiracy Detection*** subtasks uses annotations with nine categories each uses three classes, and ***Graph-Based Conspiracy Source Detection*** subtask uses simple binary annotations.


### Ground Truth

In the ***Text-Based Misinformation and Conspiracies Detection*** and ***Graph and Text-Based Conspiracy Detection*** subtasks we use three different class labels to mark the tweet contents: *Promotes/Supports Conspiracy*, *Discusses Consparacy* and *Non-Conspiracy*.

* ***Promotes/Supports Conspiracy*** This class contains all tweets that promotes, supports, claim, insinuate some connection between COVID-19 and various conspiracies, such as, for example, the idea that 5G weakens the immune system and thus caused the current corona-virus pandemic; that there is no pandemic and the COVID-19 victims were actually harmed by radiation emitted by 5G network towers; ideas about an intentional release of the virus, forced or harmful vaccinations, or the virus being a hoax, etc. The crucial requirement is the claimed existence of some causal link.

* ***Discusses Consparacy*** This class contains all tweets that just mentioning the existing various conspiracies connected to COVID-19, or negating such a connection in clearly negative or sarcastic maneer.

* ***Non-Conspiracy*** This class contains all tweets not belonging to the previous two classes. Note that this also includes tweets that discuss COVID-19 pandemic itself.

In the ***Text-Based Misinformation and Conspiracies Detection*** and ***Graph and Text-Based Conspiracy Detection*** subtasks we use nine different categories that corresponds to the most popular conspiracy theories: *Suppressed cures*, *Behaviour and Mind Control*, *Antivax*, *Fake virus*, *Intentional Pandemic*, *Harmful Radiation/ Influence*, *Population reduction/ Control*, *New World Order*, and *Satanism*.

In the ***Graph-Based Conspiracy Source Detection*** subtask we use two different class labels to mark the tweet contents: *Misinformation spreader*, and *Regular user*.

### Data release

The following files are provided:

* `fakenews_2022_dataset.zip` contains all the task-dataset-related files and is shared directly to the participants via a time-limited download link.

##### Development dataset

* `task_1_dev.csv` file contains all the tweets for ***Text-Based Misinformation and Conspiracies Detection*** subtask
* `task_2_dev.csv` file contains all the users for ***Graph-Based Conspiracy Source Detection*** subtask
* `task_3_dev.csv` file contains all the tweets and corresponding users for ***Graph and Text-Based Conspiracy Detection*** subtask


The ***Text-Based Misinformation and Conspiracies Detection*** subtask development dataset file is provided in CSV format with the following fields defined:
* *TweetID* - a FakeNews task internal tweet ID that do not match with the original tweet ID.
* *Class Label for Suppressed cures* - a class identifier value for the correcponding conspiracy theory in the papticular tweet, 3 == ***Promotes/Supports Conspiracy***, 2 == ***Discusses Consparacy***, 1 == ***Non-Conspiracy*** (the same for the following Class Label fields). 
* *Class Label for Behaviour and Mind Control* - a class identifier value for the correcponding conspiracy theory in the papticular tweet (1, 2 and 3 as in the previous field). 
* *Class Label for Antivax* - a class identifier value for the correcponding conspiracy theory in the papticular tweet (1, 2 and 3 as in the previous field). 
* *Class Label for Fake virus** - a class identifier value for the correcponding conspiracy theory in the papticular tweet (1, 2 and 3 as in the previous field). 
* *Class Label for Intentional Pandemic* - a class identifier value for the correcponding conspiracy theory in the papticular tweet (1, 2 and 3 as in the previous field). 
* *Class Label for Harmful Radiation/ Influence* - a class identifier value for the correcponding conspiracy theory in the papticular tweet (1, 2 and 3 as in the previous field). 
* *Class Label for Population reduction* - a class identifier value for the correcponding conspiracy theory in the papticular tweet (1, 2 and 3 as in the previous field). 
* *Class Label for New World Order* - aa class identifier value for the correcponding conspiracy theory in the papticular tweet (1, 2 and 3 as in the previous field). 
* *Class Label for Satanism* - a class identifier value for the correcponding conspiracy theory in the papticular tweet (1, 2 and 3 as in the previous field). 
* *Tweet Text* - full tweet text block. Note that this field ends with the end of the CSV file line and it can contain extra commas that are not separators.


The ***Graph-Based Conspiracy Source Detection*** subtask development dataset file is provided in CSV format with the following fields defined:
* *UserID* - a FakeNews task internal Twitter user ID that do not match with the original Twitter user ID.
* *Class Label* - a user class identifier value, 2 == ***Misinformation spreader***, 1 == ***Regular user***.



The ***Graph and Text-Based Conspiracy Detection*** subtask development dataset file is provided in CSV format with the following fields defined:
* *TweetID* - a FakeNews task internal tweet ID that do not match with the original tweet ID.
* *Class Label for Suppressed cures* - a class identifier value for the correcponding conspiracy theory in the papticular tweet, 3 == ***Promotes/Supports Conspiracy***, 2 == ***Discusses Consparacy***, 1 == ***Non-Conspiracy*** (the same for the following Class Label fields). 
* *Class Label for Behaviour and Mind Control* - a class identifier value for the correcponding conspiracy theory in the papticular tweet (1, 2 and 3 as in the previous field). 
* *Class Label for Antivax* - a class identifier value for the correcponding conspiracy theory in the papticular tweet (1, 2 and 3 as in the previous field). 
* *Class Label for Fake virus** - a class identifier value for the correcponding conspiracy theory in the papticular tweet (1, 2 and 3 as in the previous field). 
* *Class Label for Intentional Pandemic* - a class identifier value for the correcponding conspiracy theory in the papticular tweet (1, 2 and 3 as in the previous field). 
* *Class Label for Harmful Radiation/ Influence* - a class identifier value for the correcponding conspiracy theory in the papticular tweet (1, 2 and 3 as in the previous field). 
* *Class Label for Population reduction* - a class identifier value for the correcponding conspiracy theory in the papticular tweet (1, 2 and 3 as in the previous field). 
* *Class Label for New World Order* - aa class identifier value for the correcponding conspiracy theory in the papticular tweet (1, 2 and 3 as in the previous field). 
* *Class Label for Satanism* - a class identifier value for the correcponding conspiracy theory in the papticular tweet (1, 2 and 3 as in the previous field). 
* *UserID* - a FakeNews task internal Twitter user ID that do not match with the original Twitter user ID.
* *Class Label* - a user class identifier value, 2 == ***Misinformation spreader***, 1 == ***Regular user***.
* *Tweet Text* - full tweet text block. Note that this field ends with the end of the CSV file line and it can contain extra commas that are not separators.


##### Test dataset

* `task_1_test.csv` file contains all the tweets for ***Text-Based Misinformation and Conspiracies Detection*** subtask
* `task_2_test.csv` file contains all the users for ***Graph-Based Conspiracy Source Detection*** subtask
* `task_3_test.csv` file contains all the tweets and corresponding users for ***Graph and Text-Based Conspiracy Detection*** subtask


The ***Text-Based Misinformation and Conspiracies Detection*** subtask test dataset file is provided in CSV format with the following fields defined:
* *TweetID* - a FakeNews task internal tweet ID that do not match with the original tweet ID.
* *Tweet Text* - full tweet text block. Note that this field ends with the end of the CSV file line and it can contain extra commas that are not separators.


The ***Graph-Based Conspiracy Source Detection*** subtask test dataset file is provided in CSV format with the following fields defined:
* *UserID* - a FakeNews task internal Twitter user ID that do not match with the original Twitter user ID.



The ***Graph and Text-Based Conspiracy Detection*** subtask test dataset file is provided in CSV format with the following fields defined:
* *TweetID* - a FakeNews task internal tweet ID that do not match with the original tweet ID.
* *UserID* - a FakeNews task internal Twitter user ID that do not match with the original Twitter user ID.
* *Tweet Text* - full tweet text block. Note that this field ends with the end of the CSV file line and it can contain extra commas that are not separators.


#### Common info dataset

The ***Graph-Based Conspiracy Source Detection*** and ***Graph and Text-Based Conspiracy Detection*** subtasks deals with user properties and connection graphs. We provide two files that holds this info serapately.

The ***user_info.csv*** file contains properties of Twitter users captured at the moment of publication of the latest captured tweet from that user. It is provided in CSV format with the following fields defined:
* *UserID* - a FakeNews task internal Twitter user ID that do not match with the original Twitter user ID.
* *User Creation Date* - the date when the corresponding user account was created.
* *Was User Account Verivied?* - flag, taht shows verification status of the user account.
* *Description Length* - length of the user-provided account descriprion, in characters.
* *Number of Favourites* - number of posts user added to favourites.
* *Number of Followers* - number of user's followers.
* *Number of Statuses* - number of Twitter statuses posted by user.
* *Number of Friends* - number of user's friends.
* *User Location Country* - user's country, if provided.
* *User Location State* - user's state, if provided.
* *User Location City* - user's city, if provided.


The ***user_graph.csv*** file contains directed graph that describes connections between Twitter users from the area of the task interest. It is provided in CSV format with the following fields defined:
* *UserID_i* - a FakeNews task internal Twitter user ID that do not match with the original Twitter user ID. Information source user.
* *UserID_j* - a FakeNews task internal Twitter user ID that do not match with the original Twitter user ID. Information target user.
* *Weight* - the value that represent the strength of interactions between users.


#### Dataset remarks

* Please be aware that in the development set the ordering of tweets and, consequently, users are the same across all the three subtasks and we use the same set of tweets and users here as well. However, in the test set ordering of users in the ***Text-Based Misinformation and Conspiracies Detection*** and ***Graph-Based Conspiracy Source Detection*** tasks are different and ***Graph and Text-Based Conspiracy Detection*** subtask uses it's own set of tweets and users. Thus predictions of the test set of the ***Text-Based Misinformation and Conspiracies Detection*** task cannot be efficiently used to predict labels for the ***Graph-Based Conspiracy Source Detection*** and ***Graph and Text-Based Conspiracy Detection*** subtasks.

*All CSV files has the column headers as the very first line of the files*.

*All CSV files use comma as a field separator. Note that fields that corresponds to *Tweet Text* ends with the end of the CSV file line and can contain extra commas that are not separators, but parts of the tweet text content*.

*All CSV files are UTF-8 encoded and stored in Linux-style text file format using only one line ending character (0x0A in hex, '\n' in C/C++)*.




## Submission

### Run Submissions

TBA


### Submission Format

TBA


## References and recommended reading

***General***

[1] Nyhan, Brendan, and Jason Reifler. 2015. [Displacing misinformation about events: An experimental test of causal corrections](https://www.cambridge.org/core/journals/journal-of-experimental-political-science/article/displacing-misinformation-about-events-an-experimental-test-of-causal-corrections/69550AB61F4E3F7C2CD03532FC740D05#). Journal of Experimental Political Science 2, no. 1, 81-93.

***Twitter data collection and analysis***

[2] Burchard, Luk, Daniel Thilo Schroeder, Konstantin Pogorelov, Soeren Becker, Emily Dietrich, Petra Filkukova, and Johannes Langguth. 2020. [A Scalable System for Bundling Online Social Network Mining Research](https://ieeexplore.ieee.org/document/9336577). In 2020 Seventh International Conference on Social Networks Analysis, Management and Security (SNAMS), IEEE, 1-6.

[3] Schroeder, Daniel Thilo, Konstantin Pogorelov, and Johannes Langguth. 2019. [FACT: a Framework for Analysis and Capture of Twitter Graphs](https://ieeexplore.ieee.org/document/8931870). In 2019 Sixth International Conference on Social Networks Analysis, Management and Security (SNAMS), IEEE, 134-141.

[4] Achrekar, Harshavardhan, Avinash Gandhe, Ross Lazarus, Ssu-Hsin Yu, and Benyuan Liu. 2011. [Predicting flu trends using twitter data](https://ieeexplore.ieee.org/document/5928903). In 2011 IEEE conference on computer communications workshops (INFOCOM WKSHPS), IEEE, 702-707.

[5] Chen, Emily, Kristina Lerman, and Emilio Ferrara. 2020. [Covid-19: The first public coronavirus twitter dataset](https://arxiv.org/abs/2003.07372v1?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+CoronavirusArXiv+%28Coronavirus+Research+at+ArXiv%29). arXiv preprint arXiv:2003.07372.

[6] Kouzy, Ramez, Joseph Abi Jaoude, Afif Kraitem, Molly B. El Alam, Basil Karam, Elio Adib, Jabra Zarka, Cindy Traboulsi, Elie W. Akl, and Khalil Baddour. 2020. [Coronavirus goes viral: quantifying the COVID-19 misinformation epidemic on Twitter](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7152572/). Cureus 12, no. 3.

***Natural language processing***

[7] Bourgonje, Peter, Julian Moreno Schneider, and Georg Rehm. 2017. [From clickbait to fake news detection: an approach based on detecting the stance of headlines to articles](https://www.aclweb.org/anthology/W17-4215/). In Proceedings of the 2017 EMNLP Workshop: Natural Language Processing meets Journalism, 84-89.

[8] Imran, Muhammad, Prasenjit Mitra, and Carlos Castillo. 2016. [Twitter as a lifeline: Human-annotated twitter corpora for NLP of crisis-related messages](https://arxiv.org/abs/1605.05894). arXiv preprint arXiv:1605.05894.

***Information spreading***

[9] Liu, Chuang, Xiu-Xiu Zhan, Zi-Ke Zhang, Gui-Quan Sun, and Pak Ming Hui. 2015. [How events determine spreading patterns: information transmission via internal and external influences on social networks](https://iopscience.iop.org/article/10.1088/1367-2630/17/11/113045/pdf). New Journal of Physics 17, no. 11.

***Online news sources analysis***

[10] Pogorelov, Konstantin, Daniel Thilo Schroeder, Petra Filkukova, and Johannes Langguth. 2020. [A System for High Performance Mining on GDELT Data](https://ieeexplore.ieee.org/document/9150419). In 2020 IEEE International Parallel and Distributed Processing Symposium Workshops (IPDPSW), IEEE, 1101-1111.


#### Task Organizers
* Konstantin Pogorelov, Simula Research laboratory (Simula), Norway, konstantin (at) simula.no
* Johannes Langguth, Simula Research laboratory (Simula), Norway, langguth (at) simula.no
* Daniel Thilo Schroeder, Simula Research laboratory (Simula), Norway

#### Task auxiliaries
* Özlem Özgöbek, Norwegian University of Science and Technology (NTNU), Norway

## Acknowledgements

This work was funded by the Norwegian Research Council under contracts #272019 and #303404 and has benefited from the Experimental Infrastructure for Exploration of Exascale Computing (eX3), which is financially supported by the Research Council of Norway under contract #270053. We also acknowledge support from Michael Kreil in the collection of Twitter data.
