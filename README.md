# Amazon product price tracker 
![alt_text](https://m.media-amazon.com/images/G/31/social_share/amazon_logo._CB633266945_.png)
Hello guys today we are going to see about how to get data from amazon website of a specific product and send the alert mail to the mail id.

### Please see the requirements.txt to install required packages

1. First import the required packages and intitate connection with the amazon website using request package.
2. Use Beautifulsoup command find and gettext to get the appropriate details from html tags 
3. To get appropriate html tag just click inspect in your browser and get the id or class value of the element from it
4.Now you have informations about product then use smtp package to send mail to your desired email
#### Please note google disabled smtp package function to enable it you need to change some settings
 https://stackoverflow.com/questions/16512592/login-credentials-not-working-with-gmail-smtp
 ###### Please see this link
