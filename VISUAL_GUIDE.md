# 📸 Visual Step-by-Step Guide - Getting FREE Gemini API Key

## 🎯 Goal: Get your FREE API key and run the AI bot

---

## Step 1: Visit Google AI Studio

### What to do:
1. Open your browser (Chrome, Firefox, Safari, etc.)
2. Go to: **https://ai.google.dev/**
3. OR go directly to: **https://makersuite.google.com/app/apikey**

### What you'll see:
```
┌─────────────────────────────────────────────┐
│  Google AI Studio                    [Login]│
│                                              │
│   Build with Gemini                         │
│   Get started with Google's AI              │
│                                              │
│          [Get API Key]                       │
└─────────────────────────────────────────────┘
```

### Action:
Click the **"Get API Key"** or **"Get Started"** button

---

## Step 2: Sign In with Google

### What to do:
1. Click **"Sign in with Google"**
2. Choose your Gmail account
3. Enter password if asked

### What you'll see:
```
┌─────────────────────────────────────────────┐
│  Sign in with Google                        │
│                                              │
│  📧 your.email@gmail.com                    │
│  🔒 ••••••••••••                            │
│                                              │
│          [Next]                              │
└─────────────────────────────────────────────┘
```

### Action:
Sign in with your Google/Gmail account

---

## Step 3: Accept Terms of Service

### What to do:
1. Read the terms (optional 😉)
2. Check the box "I agree"
3. Click **"Continue"** or **"Accept"**

### What you'll see:
```
┌─────────────────────────────────────────────┐
│  Terms of Service                           │
│                                              │
│  ☐ I agree to the Terms of Service         │
│                                              │
│          [Continue]                          │
└─────────────────────────────────────────────┘
```

---

## Step 4: Create Your API Key

### What to do:
1. You'll see "API Keys" page
2. Click **"Create API Key"** button
3. Select **"Create API key in new project"**
4. Wait 2-3 seconds

### What you'll see:
```
┌─────────────────────────────────────────────┐
│  API Keys                                    │
│                                              │
│  [+ Create API Key]                          │
│                                              │
│  No API keys yet                             │
└─────────────────────────────────────────────┘
```

Then:
```
┌─────────────────────────────────────────────┐
│  Create API Key                              │
│                                              │
│  ○ Create API key in new project            │
│  ○ Create API key in existing project       │
│                                              │
│          [Create]                            │
└─────────────────────────────────────────────┘
```

### Action:
Select "Create API key in new project" and click **Create**

---

## Step 5: Copy Your API Key!

### What to do:
1. Your API key appears!
2. Click the **copy icon** 📋
3. Save it somewhere safe (Notepad, Notes app)

### What you'll see:
```
┌─────────────────────────────────────────────┐
│  Your API Key                                │
│                                              │
│  AIzaSyDXXXXXXXXXXXXXXXXXXXXXXXX    [📋]   │
│                                              │
│  ⚠️ Keep this key private!                  │
│                                              │
│          [Done]                              │
└─────────────────────────────────────────────┘
```

### Your API key looks like:
```
AIzaSyDXXXXXXXXXXXXXXXXXXXXXXXX
```
- Always starts with: `AIza`
- Total length: about 39 characters
- Mix of letters and numbers

---

## Step 6: Install Google Gemini Package

### What to do:
1. Open Command Prompt (Windows) or Terminal (Mac/Linux)
2. Type the install command
3. Press Enter and wait

### In Command Prompt/Terminal, type:

**Windows:**
```cmd
pip install google-generativeai
```

**Mac/Linux:**
```bash
pip3 install google-generativeai
```

### What you'll see:
```
C:\Users\YourName> pip install google-generativeai

Collecting google-generativeai
  Downloading google_generativeai-0.3.2-py3-none-any.whl (150 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 150/150 kB 1.2 MB/s

Collecting google-ai-generativelanguage
  Downloading google_ai_generativelanguage-0.4.0-py3-none-any.whl

Installing collected packages: google-generativeai
Successfully installed google-generativeai-0.3.2

C:\Users\YourName>
```

✅ Success! Package installed.

---

## Step 7: Navigate to Bot Location

### What to do:
1. Find where you saved `free_bot.py`
2. Use `cd` command to go there

### In Command Prompt/Terminal, type:

**If your bot is in Downloads folder:**

Windows:
```cmd
cd C:\Users\YourName\Downloads
```

Mac/Linux:
```bash
cd ~/Downloads
```

**Alternative - Easy way:**
1. Type `cd ` (with a space after)
2. Drag the folder where your bot is
3. Press Enter

### What you'll see:
```
C:\Users\YourName> cd Downloads

C:\Users\YourName\Downloads>
```

The path changed to your bot's location!

---

## Step 8: Run the Bot

### What to do:
1. Make sure you're in the correct folder
2. Run the Python file

### In Command Prompt/Terminal, type:

**Windows:**
```cmd
python free_bot.py
```

**Mac/Linux:**
```bash
python3 free_bot.py
```

### What you'll see:
```
======================================================================
🤖 FREE Conversational Knowledge Bot
======================================================================

💡 This bot works in TWO modes:

   1. SIMPLE MODE (No API needed) - Basic responses
   2. GEMINI MODE (FREE API) - Smart AI responses

======================================================================

🎯 Choose your mode:
   1 - Simple Mode (Works right now, no setup!)
   2 - Gemini AI Mode (Need FREE API key from https://ai.google.dev/)

Your choice (1 or 2):
```

---

## Step 9: Choose Gemini Mode

### What to do:
1. Type `2` 
2. Press Enter

### You'll see:
```
Your choice (1 or 2): 2

Enter your Gemini API key (or press Enter to skip):
```

---

## Step 10: Paste Your API Key

### What to do:
1. Paste your API key (that you copied earlier)
2. Press Enter

### How to paste:
- **Windows**: Right-click in the black window
- **Mac**: Press `Command + V`
- **Linux**: Press `Ctrl + Shift + V`

### You'll see:
```
Enter your Gemini API key (or press Enter to skip): AIzaSyDXXXXXXXXXXXXXXX

✓ Using Google Gemini AI (FREE!)

======================================================================
✨ Try these commands:
   • 'Calculate 2+2' or '5*10'
   • 'What time is it?'
   • 'Tell me about Python'
   • 'history' - See conversation history
   • 'quit' - Exit
======================================================================

👤 You:
```

---

## Step 11: Start Chatting! 🎉

### Try these:

```
👤 You: Hello! Who are you?

🤖 Bot: 🤖 Hi! I'm an AI assistant powered by Google Gemini. 
        I can help you with questions, have conversations, 
        explain concepts, and much more. How can I help you today?

👤 You: Write a haiku about programming

🤖 Bot: 🤖 Code flows like water
        Bugs hide in silent shadows
        Debug brings the light

👤 You: What's 25 * 4?

🤖 Bot: ✓ Result: 100

👤 You: Explain Python in simple terms

🤖 Bot: 🤖 Python is a programming language that's designed to be 
        easy to read and write. Think of it as a way to give 
        instructions to a computer using words that are close to 
        English. It's great for beginners because...

👤 You: quit

👋 Goodbye! Thanks for chatting!
```

---

## ✅ Success Checklist

Check these off as you complete them:

- [ ] Visited https://ai.google.dev/
- [ ] Signed in with Google account
- [ ] Created API key
- [ ] Copied and saved API key
- [ ] Installed google-generativeai (`pip install google-generativeai`)
- [ ] Navigated to bot folder (`cd ...`)
- [ ] Ran the bot (`python free_bot.py`)
- [ ] Chose option 2 (Gemini Mode)
- [ ] Pasted API key
- [ ] Started chatting successfully!

---

## 🆘 Troubleshooting Common Issues

### "pip is not recognized"
**Solution:**
```cmd
python -m pip install google-generativeai
```

### "ModuleNotFoundError: No module named 'google'"
**Solution:** The package didn't install. Try:
```cmd
pip install --upgrade google-generativeai
```

### "API key invalid"
**Solution:**
1. Check you copied the full key
2. No extra spaces at beginning or end
3. Generate a new key if needed

### "Permission denied"
**Solution:** Add `--user` flag:
```cmd
pip install --user google-generativeai
```

### Bot doesn't respond
**Solution:**
1. Check your internet connection
2. Wait a few seconds (first request can be slow)
3. Try asking a simpler question first

---

## 📝 Quick Command Reference

| Action | Windows | Mac/Linux |
|--------|---------|-----------|
| Install package | `pip install google-generativeai` | `pip3 install google-generativeai` |
| Run bot | `python free_bot.py` | `python3 free_bot.py` |
| Navigate folder | `cd C:\folder\path` | `cd ~/folder/path` |
| Check Python | `python --version` | `python3 --version` |

---

## 🎯 What to Do Next

Once you have it working:

1. **Experiment!** Ask it different questions
2. **Try calculations:** "Calculate 123 * 456"
3. **Ask for help:** "How do I learn Python?"
4. **Get creative:** "Write a story about a robot"
5. **Learn coding:** "Explain what a function is"

---

## 💡 Pro Tips

1. **Save your API key** in a text file for future use
2. **Never share** your API key publicly
3. **Be patient** - first response might be slow
4. **Have fun!** Experiment with different questions
5. **Use 'history'** command to see past conversation

---

**🎊 Congratulations! You now have a FREE AI chatbot!**

Enjoy unlimited conversations with Google Gemini - completely FREE! 🚀
