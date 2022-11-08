# Mail Merge For the Revolution!  

Be their voice!  

The idea is to use the resources of google to our advantage and make 
it possible to send out mass mailings.  The inspiration came from a
google video that explains it all.  

Mail Merge with Google Sheets and Gmail:  
[Youtube Video Mail Merge](https://www.youtube.com/watch?v=YTeV4i1W3Zo)  

## Pre-requisites:  
1. gmail account - if you don't have one, get one!  Create a burner account if you are not comfortable about using your own personal one.  At no point in time should you ever undertake something that you're not comfortable with.  

## Steps:  
Instead of re-inventing the wheel, I have the link to the instructions.  These are pretty good.  

[Mail Merge Instructions](https://developers.google.com/apps-script/samples/automations/mail-merge)  

## Moving forward:  
1. Take a copy of the sheet and rename it to something like: UN Missions email list and copy the .csv data from: [CSV data](https://github.com/glebite/2022/blob/main/snapshot/country_email.csv) also add a column: Email Sent  
2. I am not certain but try to remove any trailing rows that are not necessary.  
3. Create a draft email and add {{Recipient}} in the "To" field of the draft email.  
4. Enter your subject such as: "The cruelty of the IRGC must be acted on."  
5. In the body of the text, enter: "To the Mission to the UN from {{Country Long Name}}:"
6. Fill out the body of the text - add links to news articles, hash tags, pictures, and of course, Regards, Sincerely, etc...  Leave it as a draft.  
7. Return to the sheets tab and press Mail Merge.  
8. You will be prompted for the Subject line of the draft.  In this example, it is: "The cruelty of the IRGC must be acted on."  
9. You may be requested for permissions - give them.  This is not about you, it's about being their voice.  Be their voice!

## Further fun:  
Fork this repo, build your own list, join in with the repo owner, make changes and suggestions.  This is a tool that can be used by others.  

Be their voice!!!
