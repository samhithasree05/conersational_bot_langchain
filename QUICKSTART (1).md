# Quick Start Guide 🚀

Get your Conversational Knowledge Bot running in 5 minutes!

## Step 1: Install Dependencies (2 minutes)

```bash
# Install required packages
pip install langchain langchain-anthropic langchain-community anthropic requests python-dotenv

# For advanced features (optional)
pip install faiss-cpu
```

## Step 2: Set Up API Key (1 minute)

### Option A: Environment Variable (Recommended)
```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

### Option B: Create .env file
```bash
echo "ANTHROPIC_API_KEY=your-api-key-here" > .env
```

Get your API key from: https://console.anthropic.com/

## Step 3: Run the Bot (30 seconds)

### Basic Bot
```bash
python conversational_bot.py
```

### Advanced Bot (with RAG)
```bash
python advanced_bot.py
```

## Step 4: Try These Commands! (1 minute)

Once the bot is running, try:

### Basic Calculations
```
You: What's 25 * 4 + 10?
You: Calculate the square root of 144
```

### Weather Queries
```
You: What's the weather in London?
You: How's the weather in Tokyo?
```

### Knowledge Questions
```
You: Tell me about Python
You: What is LangChain?
You: Explain machine learning
```

### Time Queries
```
You: What time is it?
```

### Advanced Features (advanced_bot.py only)

#### Unit Conversions
```
You: Convert 25,celsius,fahrenheit
You: Convert 100,km,miles
```

#### Note Taking
```
You: Save a note: Buy groceries|personal
You: What are my personal notes?
```

#### Advanced Math
```
You: Calculate sqrt(144) + log(100)
You: What's sin(45)?
```

## Troubleshooting 🔧

### "ANTHROPIC_API_KEY not found"
- Make sure you've exported the environment variable
- Check that your .env file is in the same directory
- Verify your API key is correct

### "Module not found"
```bash
pip install --upgrade -r requirements.txt
```

### Import Errors
```bash
# Try installing specific versions
pip install langchain==0.1.0 langchain-anthropic==0.1.0
```

## Commands Reference 📚

While chatting with the bot:

- `quit` or `exit` - Exit the bot
- `clear` - Clear conversation memory
- `stats` - Show statistics (advanced bot only)
- `new session` - Start fresh session (advanced bot only)

## What's Next? 🎯

1. **Explore the code**: Open `conversational_bot.py` to see how it works
2. **Add custom tools**: Create your own functions and add them to the tools list
3. **Modify the knowledge base**: Add your own documents and information
4. **Try the advanced bot**: Use `advanced_bot.py` for RAG and persistent memory

## Example Conversation Flow

```
🤖 Bot: Hello! I'm your AI assistant. How can I help you today?

👤 You: What's 15 * 8?
🤖 Bot: The result of 15 * 8 is 120.

👤 You: What's the weather like in Paris?
🤖 Bot: Current weather in Paris: 17°C, Partly cloudy

👤 You: Can you tell me about Python programming?
🤖 Bot: Python is a high-level, interpreted programming language 
        created by Guido van Rossum in 1991. It emphasizes code 
        readability and supports multiple programming paradigms...

👤 You: Thanks! That's helpful.
🤖 Bot: You're welcome! Feel free to ask if you need anything else.
```

## Architecture Overview 📊

```
┌──────────────┐
│  User Input  │
└──────┬───────┘
       │
       ▼
┌──────────────────┐
│  LangChain Agent │
└──────┬───────────┘
       │
       ▼
┌─────────────────────────────┐
│  Tool Selection & Execution │
│  • Calculator               │
│  • Weather                  │
│  • Knowledge Search         │
│  • Time                     │
└──────┬──────────────────────┘
       │
       ▼
┌──────────────────┐
│ Memory (Context) │
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│    Response      │
└──────────────────┘
```

## Tips for Best Results 💡

1. **Be Specific**: "Calculate 2+2" is better than "do math"
2. **One Task at a Time**: For complex queries, break them down
3. **Use Clear Language**: Simple, direct questions work best
4. **Remember Context**: The bot remembers your conversation
5. **Clear When Needed**: Use `clear` to start fresh

## Performance Tips ⚡

- Use summary memory for long conversations (advanced bot)
- Clear memory regularly to free up resources
- Keep questions focused for faster responses
- Use the basic bot for simple tasks, advanced bot for complex ones

## Security Notes 🔒

- Never commit your API key to version control
- Use environment variables for sensitive data
- The calculator uses safe evaluation (no arbitrary code execution)
- Notes are saved locally only

## Getting Help 🆘

If you run into issues:

1. Check the README.md for detailed documentation
2. Run `python test_bot.py` to verify your setup
3. Check the error messages - they usually point to the problem
4. Make sure your API key is valid and has credits

## Resources 📚

- [LangChain Documentation](https://python.langchain.com/)
- [Anthropic API Docs](https://docs.anthropic.com/)
- [Claude Models Info](https://www.anthropic.com/claude)

---

**Ready to start? Run the bot and say hello! 👋**

```bash
python conversational_bot.py
```

---

**Having fun? Try the advanced version next! 🚀**

```bash
python advanced_bot.py
```
