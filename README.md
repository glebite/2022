# 2022
![Quqnus](The_phoenix_rises.jpg)
Image from: [Wikimedia](https://commons.wikimedia.org/wiki/File:The_phoenix_rises.jpg)
New tools with hacktivism for doing humanitarian stuff. 

## installation:  
Clone from github:  
> cd projects (or wherever you store your cloned repos)  
> git clone https://github.com/glebite/2022.git  
> cd 2022

Build a python virtual environment:  
> python3 -m venv venv  
Linux/MAC:  
(I don't have a MAC but I suspect it's the same)  
> source venv/bin/activate  
Windows:  
> venv\Scripts\Activate  

Install prerequisites:  
> python3 -m pip install -r requirements.txt  

Have fun:  
> theskyisthelimit  

## tools:  
  
### unmembers.py  
This tool retrieves the .json data from the unmeetings.org and extracts
the country name and email information for the various missions at the UN.  
  
  
### worldleaders.py  
This tool will find the world leaders from wikipedia and hopefully using some
other magic, find the email addresses of their government or to their office.  

### CanadianMPs.py  
Outputs .csv data with the Names, email, Party, Riding, and Province in Canada
of all MPs registered with the house of commons.  I will capture the output
as it shouldn't change too much over a few months.  

### CanadianMedia.py  
Grabs and outputs a list of Canadian Media sites.

### twit_gen.py
Stupid tool that can pump out auto tweets to the console.  Yes, a twitter bot could do this faster but I have had warnings in the past with my account so for now copying and pasting will suffice.

