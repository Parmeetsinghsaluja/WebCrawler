This is a web crawler written in Python. 
To execute this crawler you need following packages: 
1. urllib - urlparse, urljoin, urlopen
2. time
3. BeautifulSoup

 urllib        =>  is a package that collects several modules for working with URLs:
			urllib.request for opening and reading URLs
			urllib.error containing the exceptions raised by urllib.request
			urllib.parse for parsing URLs
			urllib.robotparser for parsing robots.txt files

 time          =>  This module provides various time-related functions.
                   Particularly used here to delay the request of crawler so that it obeys politness policy.
 
 BeautifulSoup  => Beautiful Soup is a Python library for pulling data out of HTML and XML files.


The urllib library fetches the webpage and this is passed to Beautiful Soup which creates a soup object. 
The soup object contains a tree structure which helps to crawl the links.

How to run:
1. Install Pythonv2.7.4
2. To run this, you can install BeautifulSoup -https://pypi.python.org/pypi/beautifulsoup4
   Or download the folder named bs4 with this file and save in the same directory as this file.
   bs4 folder is present in the Parmeetsingh_Saluja_TuTh_HW1 folder.

3.The web crawler is in Parmeetsingh_Saluja_TuTh_HW1 folder so change your directory to Parmeetsingh_Saluja_TuTh_HW1 folder.

4. Run the crawler by entering command on your command line python by command -
   python filename
   For Task1- python Web_Crawler.py
   For Task1- python Focused_Crawler.py

5.In Task-1
There is defaukt value of seed url no need to explicitly enter the link
Default value for url is- "https://en.wikipedia.org/wiki/Tropical_cyclone"

6.In Task-2
 You have to enter the url and the keyword and if you want to use default values just press Enter Key.
 Default value for url is- "https://en.wikipedia.org/wiki/Tropical_cyclone"
 Default keyword is-"rain"
   
DEPTH REACHED
Task-1 - Depth reached is 3
Task-2 - Depth reached is 6 (Links of 6 are extracted)
