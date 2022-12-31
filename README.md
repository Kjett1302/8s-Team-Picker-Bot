# 8s-Team-Picker-Bot
Discord bot that randomly picks teams for videogame 8s

Bot Invite: https://discord.com/api/oauth2/authorize?client_id=1058729301396164640&permissions=534723950656&scope=bot

If running locally add discord application token to .env and comment out keep_running() at the bottom of main.py because it won't be necessary.

If running on https://replit.com/, keep "keep_running()" in main.py.
Create a new Python Replit and upload both main.py and keep_running.py.
Then on the left dashboard find the lock icon that says Sercets and click on it to add application token from discord.
Name key "TOKEN" and value is the app application token.
Then run the replit which might fail after install packages, if so, type 'kill 1' in the shell and wait for it to reconnect.
Run the replit again and you should see the bot is active in your server and running on replit.
Replit as a timeout where after an hour the application will timeout, to avoid this, use https://uptimerobot.com/.
Create an account and add a monitor, go to replit and copy the programs server url which will look like this https://projectName.userName.repl.co
Select https on uptime robot and add the url. If you paste the url into your web browser and it doesn't work, change https to http in the url
so it will look like this http://projectName.userName.repl.co and copy it into uptime robot.
Set the interval to 10 or 15 minutes and it should all be set.
