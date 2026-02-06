# 📘 COMPLETE SETUP INSTRUCTIONS

## 🎯 Overview

This guide will walk you through **every step** needed to run your Conversational Knowledge Bot. Follow the instructions for your operating system.

---

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation Steps](#installation-steps)
3. [Getting API Key](#getting-api-key)
4. [Running the Bot](#running-the-bot)
5. [Usage Guide](#usage-guide)
6. [Troubleshooting](#troubleshooting)
7. [Advanced Setup](#advanced-setup)

---

## 🔧 Prerequisites

### What You Need:
- ✅ Computer (Windows, Mac, or Linux)
- ✅ Internet connection
- ✅ Python 3.6 or higher
- ✅ Google account (for free API key)

### Check Python Installation:

**Windows:**
```cmd
python --version
```

**Mac/Linux:**
```bash
python3 --version
```

**Should show:** `Python 3.x.x`

**If Python is NOT installed:**
1. Visit: https://www.python.org/downloads/
2. Download latest version
3. Run installer
4. ✅ **IMPORTANT:** Check "Add Python to PATH"
5. Click "Install Now"
6. Restart computer

---

## 📦 Installation Steps

### OPTION 1: Simple Mode (No Installation Required!)

**This works immediately without any setup!**

1. Download `free_bot.py`
2. Open terminal/command prompt
3. Navigate to the folder:
   ```bash
   cd path/to/folder
   ```
4. Run:
   ```bash
   python free_bot.py
   ```
5. Choose option **1** (Simple Mode)
6. Start chatting! ✅

**That's it! No API key, no installation, just works!**

---

### OPTION 2: Gemini AI Mode (FREE - Recommended!)

#### Step 1: Install Google Gemini Package

**Windows:**
```cmd
pip install google-generativeai
```

**Mac/Linux:**
```bash
pip3 install google-generativeai
```

**What you'll see:**
```
Collecting google-generativeai
  Downloading google_generativeai-0.3.2...
Installing collected packages: google-generativeai
Successfully installed google-generativeai-0.3.2
```

✅ **If you see "Successfully installed" - you're done!**

#### Step 2: Get FREE API Key

**See section:** [Getting API Key](#getting-api-key) below

#### Step 3: Run with Gemini

```bash
python free_bot.py
```
- Choose option **2** (Gemini AI Mode)
- Paste your API key
- Start chatting with AI! ✅

---

### OPTION 3: Advanced LangChain Mode (Optional)

**For advanced users who want full features**

#### Step 1: Install All Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- langchain
- langchain-anthropic
- langchain-community
- anthropic
- requests
- python-dotenv

#### Step 2: Get Anthropic API Key

1. Visit: https://console.anthropic.com/
2. Sign up (get $5 FREE credits!)
3. Go to API Keys
4. Create new key
5. Copy it

#### Step 3: Set Environment Variable

**Windows:**
```cmd
set ANTHROPIC_API_KEY=your-key-here
```

**Mac/Linux:**
```bash
export ANTHROPIC_API_KEY=your-key-here
```

**Or create .env file:**
```
ANTHROPIC_API_KEY=your-key-here
```

#### Step 4: Run Advanced Bot

```bash
python conversational_bot.py
```

or

```bash
python advanced_bot.py
```

---

## 🔑 Getting API Key (Detailed Guide)

### For Google Gemini (FREE - Unlimited!)

#### Step 1: Visit Google AI Studio
- Go to: **https://ai.google.dev/**
- Or directly: **https://makersuite.google.com/app/apikey**

#### Step 2: Sign In
- Click **"Get API Key"** or **"Sign In"**
- Use your Google/Gmail account
- Accept terms of service

#### Step 3: Create API Key
- Click **"Create API Key"** button
- Select **"Create API key in new project"**
- Wait 2-3 seconds

#### Step 4: Copy Your Key
- Your key appears: `AIzaSyDXXXXXXXXXXXXXXXXXXXXX`
- Click the copy icon 📋
- Save it somewhere safe (Notepad, Notes app)

#### Step 5: Keep It Private!
⚠️ **Never share your API key publicly!**

---

## 🚀 Running the Bot

### Starting the Bot

#### Windows:
```cmd
# Navigate to bot folder
cd C:\Users\YourName\Desktop\convo_bot

# Run the bot
python free_bot.py
```

#### Mac/Linux:
```bash
# Navigate to bot folder
cd ~/Desktop/convo_bot

# Run the bot
python3 free_bot.py
```

### Choosing Mode

You'll see:
```
🎯 Choose your mode:
   1 - Simple Mode (Works right now, no setup!)
   2 - Gemini AI Mode (Need FREE API key)

Your choice (1 or 2):
```

**Type 1 or 2 and press Enter**

### If You Choose Mode 2 (Gemini):

```
Enter your Gemini API key (or press Enter to skip):
```

**Paste your API key and press Enter**

How to paste:
- **Windows:** Right-click
- **Mac:** Cmd + V
- **Linux:** Ctrl + Shift + V

---

## 📖 Usage Guide

### Available Commands

While chatting with the bot:

| Command | What it does |
|---------|--------------|
| `quit` | Exit the bot |
| `exit` | Exit the bot |
| `bye` | Exit the bot |
| `history` | Show conversation history |
| Any question | Get a response! |

### Example Conversations

#### 1. Calculator (Both Modes)
```
You: Calculate 25 * 4 + 10
Bot: ✓ Result: 110

You: What's 100 / 5?
Bot: ✓ Result: 20.0
```

#### 2. Time Query (Both Modes)
```
You: What time is it?
Bot: 🕐 Current time: 2026-02-06 15:30:00
```

#### 3. Knowledge Questions (Both Modes)
```
You: Tell me about Python
Bot: 🐍 Python is an easy-to-learn programming language 
     created in 1991. Great for beginners!
```

#### 4. AI Conversations (Gemini Mode Only)
```
You: Write a haiku about programming
Bot: 🤖 Code flows like water
        Bugs hide in silent shadows  
        Debug brings the light

You: Explain what loops are in coding
Bot: 🤖 Loops are a way to repeat actions in programming...

You: Create a simple Python function
Bot: 🤖 Here's a simple function:
     def greet(name):
         return f"Hello, {name}!"
```

#### 5. Creative Writing (Gemini Mode Only)
```
You: Write a short story about AI
Bot: 🤖 In a world where circuits dreamed, 
     there lived a curious AI named Nova...

You: Tell me a programming joke
Bot: 🤖 Why do programmers prefer dark mode?
     Because light attracts bugs! 😄
```

---

## 🐛 Troubleshooting

### Common Issues & Solutions

#### Issue 1: "Python not recognized" or "command not found"

**Solution:**
1. Python not installed - Install from python.org
2. Not in PATH - Reinstall with "Add to PATH" checked
3. Use full path:
   ```
   C:\Python310\python.exe free_bot.py
   ```

#### Issue 2: "pip not recognized" or "pip: command not found"

**Solution A - Use python -m pip:**
```bash
python -m pip install google-generativeai
```

**Solution B - Install pip:**
```bash
python -m ensurepip --upgrade
```

#### Issue 3: "ModuleNotFoundError: No module named 'google'"

**Solution:**
```bash
# Install the package
pip install google-generativeai

# Or with python -m
python -m pip install google-generativeai

# Or with --user flag
pip install --user google-generativeai
```

#### Issue 4: "Permission denied" or "Access denied"

**Solution - Add --user flag:**
```bash
pip install --user google-generativeai
```

#### Issue 5: "API key invalid" or "Authentication failed"

**Solution:**
1. Check for spaces at beginning/end of key
2. Make sure you copied the FULL key
3. Key should start with: `AIza`
4. Key should be ~39 characters long
5. Generate a new key if needed

#### Issue 6: Bot doesn't respond / hangs

**Solution:**
1. Check internet connection
2. Wait 5-10 seconds (first request can be slow)
3. Press Ctrl+C and restart
4. Try a simpler question first

#### Issue 7: "SyntaxError" when running bot

**Solution:**
1. Check Python version: `python --version`
2. Must be Python 3.6 or higher
3. Update Python if needed

#### Issue 8: Multiple Python versions installed

**Solution - Specify version:**
```bash
python3 free_bot.py
# or
python3.9 free_bot.py
```

---

## 🔧 Advanced Setup

### Setting Up Virtual Environment (Optional)

**Why?** Keeps dependencies isolated

#### Create Virtual Environment:

**Windows:**
```cmd
python -m venv bot_env
bot_env\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv bot_env
source bot_env/bin/activate
```

#### Install Dependencies:
```bash
pip install google-generativeai
```

#### Run Bot:
```bash
python free_bot.py
```

#### Deactivate When Done:
```bash
deactivate
```

### Using .env File for API Keys

**Step 1: Create .env file**

Create a file named `.env` in the same folder as your bot:

```
GEMINI_API_KEY=AIzaSyDXXXXXXXXXXXXXXXXXXXXX
```

**Step 2: Modify bot to read from .env**

Add to top of `free_bot.py`:
```python
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('GEMINI_API_KEY')
```

**Step 3: Install python-dotenv**
```bash
pip install python-dotenv
```

---

## 📝 Configuration Options

### Customizing the Bot

#### Change Bot Personality:

Edit `free_bot.py`, find the system prompt and modify it:
```python
system_prompt = "You are a helpful, friendly assistant..."
```

#### Add Custom Knowledge:

In `free_bot.py`, find the `knowledge_base` dictionary and add entries:
```python
knowledge = {
    "python": "Your custom Python info...",
    "your_topic": "Your custom information..."
}
```

#### Adjust Temperature (Creativity):

For Gemini mode, modify:
```python
generation_config = {
    "temperature": 0.7,  # 0 = focused, 1 = creative
}
```

---

## 📊 System Requirements

### Minimum:
- **OS:** Windows 7+, macOS 10.12+, or Linux
- **Python:** 3.6+
- **RAM:** 256 MB
- **Storage:** 50 MB
- **Internet:** 1 Mbps (for Gemini mode)

### Recommended:
- **OS:** Windows 10+, macOS 11+, or Ubuntu 20.04+
- **Python:** 3.8+
- **RAM:** 1 GB
- **Storage:** 200 MB
- **Internet:** 5 Mbps

---

## ✅ Installation Checklist

Complete setup checklist:

- [ ] Python installed (3.6+)
- [ ] Python in PATH
- [ ] pip working
- [ ] Bot files downloaded
- [ ] google-generativeai installed (for Gemini mode)
- [ ] API key obtained (for Gemini mode)
- [ ] Bot runs successfully
- [ ] Can send messages
- [ ] Can receive responses

---

## 🎓 Next Steps

After successful setup:

1. **Experiment** - Try different questions
2. **Read the code** - Understand how it works
3. **Customize** - Add your own features
4. **Learn** - Check documentation files
5. **Build** - Create your own tools

---

## 📚 Additional Resources

### Documentation Files:
- `BEGINNER_GUIDE.md` - For absolute beginners
- `VISUAL_GUIDE.md` - Step-by-step screenshots
- `QUICKSTART.md` - 5-minute quick start
- `PROJECT_SUMMARY.md` - Technical overview

### Learning Resources:
- Python Tutorial: https://www.learnpython.org/
- Google Gemini Docs: https://ai.google.dev/docs
- LangChain Guide: https://python.langchain.com/

---

## 🆘 Still Need Help?

If you're stuck:

1. **Check error message carefully** - It usually tells you what's wrong
2. **Google the error** - Copy exact error message
3. **Check Python version** - Must be 3.6+
4. **Try Simple Mode first** - No setup needed
5. **Read VISUAL_GUIDE.md** - Has screenshots
6. **Start fresh** - Restart computer and try again

---

## 🎉 Success!

If you've completed all steps, you should now have a working AI chatbot!

**Test it with:**
```
You: Hello!
Bot: Hi! How can I help you today?

You: Calculate 2+2
Bot: ✓ Result: 4
```

---

**🎊 Congratulations! You're ready to chat with your AI bot!**

**Start exploring and have fun learning!** 🚀

---

*Last Updated: February 6, 2026*
*Version: 2.0*
*For more help, check other documentation files*
