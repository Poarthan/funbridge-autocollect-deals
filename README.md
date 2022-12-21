# funbridge-autocollect-deals

This is a script to go collect your daily gifted deals on funbridge website.

First get selenium:
```
pip install selenium
```

Then get the proper webdriver for your browser, from here: [https://www.selenium.dev/documentation/webdriver/getting\_started/install\_drivers/](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/)

The last thing you need to do before running it, is editing the script to put your username and password in the spots at the bottom where it says to: `your_username_or_email` and `your_password`. The script was designed for multiple funbridge accounts, therefore, it has an extra redudancy built in. 

Then you should be able to run the script with:
```
python collection.py
```

If you want to setup this to automatically run daily, use cron jobs(for linux) or task scheduler(for windows), to set up a regular run of this.
