# keywordFinder

Python script iterates through a series or URLs looking for the instances of a keyword provided by the user. It will return a new text file with all the times the keyword was found on each URL, along with a certain number of characters (also provided by user) before and after the keyword, to give an idea of the context that keyword was used on.

-------------------

This scripts accepts 3 arguments over the command line:

1 - Text file containing the list of URLs

2 - Number of characters to be displayed

3 - Keyword being looked for (can be a phrase, as long as it is inside a "string")

The program will look on the text file for the list of URLs, go to each of them, and look for all the times the keyword is found on the page. 
Once the keyword is found, a fragment of the text in where it is found will be extracted from the website. The size of the fragment will be dictated by the number of characters specified on the command line. Half of the characters will go before the keyword and half after, returning a string of a length of the number of characters specified + the length of the keyword.
The script will create a file called "output.txt" where it will print the URL, then on the next line print "FOUND" or "NOT FOUND", depending if the keyword was found at least once on the URL, and the string containing the keyword.

Example: python keywordFinder.py mypages.txt 200 "literature"

This will look on the "mypages.txt" file, which has the list of URLs, go to those websites and look for the word "literature". If it finds it it will return a string of 100 characters before the word "literature", then the actual word "literature", and after another 100 characters.
