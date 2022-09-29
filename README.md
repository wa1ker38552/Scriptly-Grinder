# Scriptly-Grinder
A API based bot to farm XP and gems on Scriptly Studios

Several built-in functions which include `ECONOMY_GRINDER` and `BUMP_GRINDER`. The economy grinder grinds MEE6 economy with randomization added to avoid detection. The bump grinder grinds the command `/bump` for Disboard.

**Getting Started**
<br>
`$ git clone https://wa1ke3r38552/Scriptly-Grinder`
Create a client using:
```py
client = MEE6('TOKEN')
```
This will initialize your Discord client which the script sends requests from. You can then start the pre-coded functions.
```py
# range is the amount of time between messages in commands
client.ECONOMY_GRINDER(CHANNEL, INTERVAL, [COMMAND1, COMMAND2], range=[1, 5])
client.BUMP_GRINDER(interval, data_file)
```
Since application commands require more data to use than sending regular messages, It is recommended that you have a json file with the application command data for the bot to use. (See examples in `data.json`)
<br>
Now that all the basic commands are setup, you can add custom commands using:
```py
client.TASK(CHANNEL, {'MESSAGE': TIME}, offset=AMOUNT_TO_WAIT_BEFORE_STARTING)
```

Have fun!
