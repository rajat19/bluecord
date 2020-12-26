# BlueStacks Discord Bot

## Steps to run bot:

1. Create a virtual environment -
   `virtualenv -p /usr/local/bin/python3 venv`
2. Install dependencies -
   `pip install -r requirements.txt`
3. Create .env file and add the contents using **env_example.txt** file.
4. Create your discord bot by visiting [developers console](https://discordapp.com/developers/applications)
5. Copy the bot token and add to .env file.
6. Create your **_PostgreSQL database_** and enter credentials in .env file
7. Create the **_table 'searches'_** using the SQL query:
   `Create table searches (user_id varchar(256), keyword varchar(256), search_time timestamp);`
8. Create custom search engine using Google Search API and insert the developer and search engine ID in .env file.
9. Run the app -
   `python3 bot.py`

### Expected Output -

1. If a user sends 'hi', the bot will reply 'hey'
2. if a user sends '!google YOUR_QUERY_HERE', and it'll reply with the top five links
3. if a user sends '!recent YOUR_QUERY_HERE', and it'll reply with a list of similar searches in the user's history