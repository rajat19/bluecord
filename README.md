# Bluecord (BlueStacks Discord Bot)

## Play with bot:
> The bot is already hosted on heroku.
[Click this link](https://discord.com/api/oauth2/authorize?client_id=792292031300501514&permissions=67584&scope=bothttps://discord.com/api/oauth2/authorize?client_id=792292031300501514&permissions=67584&scope=bot) to add bot to your discord server

## Steps to run bot (locally/development):

1. Create a virtual environment
```bash
virtualenv -p /usr/local/bin/python3 venv
```
1. Install dependencies
```bash
pip install -r requirements.txt
```
2. Create `.env` file and add the contents using **.env.example** file.
3. Create your discord bot by visiting [developers console](https://discordapp.com/developers/applications)
4. Copy the bot token and add to .env file.
5. Create your **_PostgreSQL database_** and enter credentials in .env file
6. Create the **_table 'searches'_** using the SQL query:
```sql
Create table searches (user_id varchar(256), keyword varchar(256), created_at timestamp);
```
7. Create custom search engine using Google Search API and insert the developer Api key and search engine ID in .env file.
8.  Run the app
```bash
python3 bot.py
```

### Expected Output -

1. If a user sends 'hi', the bot will reply 'hey'
2. if a user sends '!google YOUR_QUERY_HERE', and it'll reply with the top five links
3. if a user sends '!recent YOUR_QUERY_HERE', and it'll reply with a list of similar searches in the user's history