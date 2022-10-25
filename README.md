# Scriptly-Grinder
A API based bot to farm XP and gems on Scriptly Studios. The bot has 3 main functions, economy grinder which gets gems from MEE6 by using commands !work and !work claim 24/7, auto-count which can also auto count in the counting channel, and daily which collects MEE6's daily reward. Everything is obviously fully customizable from intervals, to offsets between accounts. The program can also handle multiple tokens at once by initializing several autocord clients. The program is written to avoid as much detection as possible. (Everything is radomized)

The Auto XP function can be used although it's pretty obvious that's you're botting if you use it too much so it's disabled by default. It works by sending AI generated responses to messages in #general using the [Kuki API](https://dev.kuki.ai/). To use it, you would need to enter your own API key. (Kuki offers 1000 free responses for a free plan). This reason why this is obvious is the AI will often get confused when hearing random parts of conversations that are already going on and give mediocre responses. The responses from this AI are parsed by putting it into lowercase and simplifying contractions. It also automatically replaces instances of Kuki or kuki with your bot's name.

**Features:**
- Auto Economy
- Auto Counting (default disabled)
- Auto Daily
- Auto XP (default disabled)
- Randomize times
- Randomize starting offset
- Handle multiple tokens

**Setup**
1. Clone the repository using 'git clone https://wa1ker38552/Scriptly-Grinder'
2. Put your tokens as individual env variables
3. Pass the env variable names as lists into the `Grinder()` initialization

**Note: I rewrote this project completely to be used with the [Autocord](https://github.com/wa1ker38552/autocord)** library that I wrote.


