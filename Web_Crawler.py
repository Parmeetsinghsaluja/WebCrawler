# Task1
# Implementing web crawler


# Importing the urllib Library
import urllib
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.request import urlopen
from urllib.parse import urljoin

# Importing the time Library
import time

#Importing BeautifulSoup
from bs4 import BeautifulSoup

#Importing ssl to handle errors
import ssl

#Creating Default Context to ignore SSL certificate errors for https
c = ssl.create_default_context()
c.check_hostname = False
c.verify_mode = ssl.CERT_NONE

visited_links_list = list()

#Defining the variable for monitoring the count
counter = 0

def web_crawler ():

	#Declaring the lists
	frontier_list = list()
	current_crawled_list = list()

	#Defining Seed URL
	seed_url = "https://en.wikipedia.org/wiki/Tropical_cyclone"

	#Appending the seed url in frontier
	frontier_list.append(seed_url)

	#Defining the variable for monitoring depth
	depth_of_crawling = 1

	global counter

    #Checking the depth and count
	while depth_of_crawling < 7  and counter <1000:

	#Checking if frontier_list is empty or not
		if len(frontier_list)>0 :

			 # Popping out the first element from list
			 url = frontier_list.pop(0)
			 print (url + " and current count=" + str(counter))

			 # Crawling this page for links
			 get_links(url, current_crawled_list) 

			 #increasing the counter value
			 counter = counter + 1

			 #Politeness policy by delaying request for atleast 1 secs
			 time.sleep(1)
		
		#If frontier_list has no links then increase the depth
		elif len(frontier_list)==0:
			depth_of_crawling = depth_of_crawling + 1
			print ("*************"+"Current depth of crawl- "+str (depth_of_crawling)+"****************")


			#Adding links from current_crawled_list to frontier_list
			for links in current_crawled_list:
				frontier_list.append(current_crawled_list.pop(0))

    #Printing the results into a file
	if len(visited_links_list)== 1000:
		print_file_with_links(visited_links_list)

# Function to extract links from current page
def get_links (current_seed, current_crawled_list):

	#Handling any error if occurs in retrieval
	try:
		html_text = urllib.request.urlopen(current_seed, context=c).read()
		#Parsing the html using beautiful soup and store in variable soup
		soup= BeautifulSoup(html_text, 'html.parser')

		#Finding all anchor tags
		tags = soup('a')

		#Adding current_seed to visited_links_list
		visited_links_list.append(current_seed)


   		#Checking all the tags to extract the good urls
		for tag in tags:

	  	    #Extracting the url from anchor tag
	  		raw_url = tag.get('href')

	  		#if url is empty then continue
	  		if(raw_url is None):
	  			continue
	  
	  		#if length of url is less then 1 then continue 
	  		if(len(raw_url)<1):
	  			continue
	  
	  		#To avoid links of images and animations  
	  		if raw_url.endswith('.png') or raw_url.endswith('.jpg') or raw_url.endswith('.gif'):
	  			continue
	  
	  		#To avoid links of pdf and text files 
	  		if raw_url.endswith('.pdf') or raw_url.endswith('.tif') or raw_url.endswith('.txt'):
	  			continue
		
	  		#Resolving Relative Refferences like href="/contact"
	  		pos_of_hash = raw_url.find('#')
	  		if pos_of_hash>1 :
	  			raw_url = raw_url[:pos_of_hash]
		
	  		#Avoiding links with colon to avoid Administrative links 
	  		pos_of_colon = raw_url.find(':')
	  		if(pos_of_colon>1) :
	  			continue

		    #Removing back slashes
	  		if raw_url.endswith('/') :
	  			raw_url=raw_url[:-1]

	  		#Processing urls so that we get full link
	  		if raw_url.startswith('/'):
	  			raw_url = urljoin("https://en.wikipedia.org/wiki", raw_url)

	  		#Avoiding links which do not start with https://en.wikipedia.org/wiki'
	  		if not raw_url.startswith('https://en.wikipedia.org/wiki'):
		  		continue

	  		#Avoiding wikipedia main page
	  		if raw_url.startswith('https://en.wikipedia.org/wiki/Main_Page'):
		  		continue

	  		#Avoiding links which are already visited
	  		if raw_url in visited_links_list:
		  		continue

	  		#Avoiding links which are already in current_crawled_list  
	  		if raw_url in current_crawled_list:
		  		continue
		  	
	  		#Checking counter and then adding url in current_crawled_list
	  		current_crawled_list.append(raw_url)

	except:
		pass

def print_file_with_links(visited_links_list):

	#Opening or Creating a file
	file = open('Task1_Links.txt' , 'w+')

	#Printing all the links in file
	while (len(visited_links_list)>0):
		file.write(visited_links_list.pop(0)+ "\n")

    #Closing the file
	file.close()

#Calling the crawler
web_crawler()

