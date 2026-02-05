"""
FREE Conversational Knowledge Bot using Google Gemini
======================================================
This version uses Google's FREE Gemini API - NO CREDIT CARD NEEDED!

Get your FREE API key: https://ai.google.dev/
"""

import os
from datetime import datetime

# We'll use simple logic instead of LangChain to keep it beginner-friendly
try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False
    print("📦 Installing Google Gemini...")
    print("Run: pip install google-generativeai")

# ============================================================================
# SIMPLE TOOLS (No external dependencies needed!)
# ============================================================================

def calculator(expression):
    """Simple calculator"""
    try:
        # Safe math evaluation
        result = eval(expression, {"__builtins__": {}}, {})
        return f"✓ Result: {result}"
    except:
        return "❌ Error: Invalid math expression"

def get_time():
    """Get current time"""
    now = datetime.now()
    return f"🕐 Current time: {now.strftime('%Y-%m-%d %H:%M:%S')}"

def knowledge_base(topic):
    """Simple knowledge base"""
    knowledge = {
        "python": "🐍 Python is an easy-to-learn programming language created in 1991. Great for beginners!",
        "ai": "🤖 AI (Artificial Intelligence) means making computers smart enough to learn and make decisions.",
        "coding": "💻 Coding is writing instructions for computers. It's like teaching them a new language!",
        "hello": "👋 Hi! I'm a simple chatbot. I can do math, tell time, and answer basic questions!"
    }
    
    topic_lower = topic.lower()
    for key in knowledge:
        if key in topic_lower:
            return knowledge[key]
    
    return "🤔 I don't know about that yet. Try asking about: python, ai, or coding!"

# ============================================================================
# SIMPLE CONVERSATIONAL BOT (No LangChain needed!)
# ============================================================================

class SimpleBot:
    """A simple chatbot that works without paid APIs"""
    
    def __init__(self, use_gemini=False, api_key=None):
        self.conversation_history = []
        self.use_gemini = use_gemini and GEMINI_AVAILABLE
        
        if self.use_gemini and api_key:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-pro')
            print("✓ Using Google Gemini AI (FREE!)")
        else:
            print("✓ Using Simple Rule-Based Bot (No AI needed)")
    
    def chat(self, user_input):
        """Process user input and respond"""
        
        # Save to history
        self.conversation_history.append(f"You: {user_input}")
        
        # Check if it's a calculation
        if any(op in user_input for op in ['+', '-', '*', '/', 'calculate']):
            # Extract numbers and operators
            for word in user_input.split():
                if any(op in word for op in ['+', '-', '*', '/']):
                    response = calculator(word)
                    self.conversation_history.append(f"Bot: {response}")
                    return response
        
        # Check if asking for time
        if 'time' in user_input.lower():
            response = get_time()
            self.conversation_history.append(f"Bot: {response}")
            return response
        
        # Check knowledge base
        response = knowledge_base(user_input)
        if "I don't know" not in response:
            self.conversation_history.append(f"Bot: {response}")
            return response
        
        # If using Gemini AI, ask it
        if self.use_gemini:
            try:
                ai_response = self.model.generate_content(user_input)
                response = f"🤖 {ai_response.text}"
                self.conversation_history.append(f"Bot: {response}")
                return response
            except:
                pass
        
        # Default friendly response
        response = "🤔 I'm a simple bot. I can:\n  • Do math (try: 2+2)\n  • Tell time (try: what time is it?)\n  • Answer questions about: python, ai, coding"
        self.conversation_history.append(f"Bot: {response}")
        return response
    
    def show_history(self):
        """Show conversation history"""
        print("\n📜 Conversation History:")
        for msg in self.conversation_history[-10:]:  # Last 10 messages
            print(f"   {msg}")

# ============================================================================
# MAIN PROGRAM
# ============================================================================

def main():
    print("=" * 70)
    print("🤖 FREE Conversational Knowledge Bot")
    print("=" * 70)
    print("\n💡 This bot works in TWO modes:\n")
    print("   1. SIMPLE MODE (No API needed) - Basic responses")
    print("   2. GEMINI MODE (FREE API) - Smart AI responses")
    print("\n" + "=" * 70)
    
    # Ask user which mode
    print("\n🎯 Choose your mode:")
    print("   1 - Simple Mode (Works right now, no setup!)")
    print("   2 - Gemini AI Mode (Need FREE API key from https://ai.google.dev/)")
    
    choice = input("\nYour choice (1 or 2): ").strip()
    
    bot = None
    
    if choice == "2":
        if not GEMINI_AVAILABLE:
            print("\n⚠️  Google Gemini not installed!")
            print("Install it with: pip install google-generativeai")
            print("Falling back to Simple Mode...\n")
            bot = SimpleBot(use_gemini=False)
        else:
            api_key = input("\nEnter your Gemini API key (or press Enter to skip): ").strip()
            if api_key:
                bot = SimpleBot(use_gemini=True, api_key=api_key)
            else:
                print("No API key provided. Using Simple Mode...\n")
                bot = SimpleBot(use_gemini=False)
    else:
        bot = SimpleBot(use_gemini=False)
    
    # Help message
    print("\n" + "=" * 70)
    print("✨ Try these commands:")
    print("   • 'Calculate 2+2' or '5*10'")
    print("   • 'What time is it?'")
    print("   • 'Tell me about Python'")
    print("   • 'history' - See conversation history")
    print("   • 'quit' - Exit")
    print("=" * 70 + "\n")
    
    # Chat loop
    while True:
        try:
            user_input = input("👤 You: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("\n👋 Goodbye! Thanks for chatting!")
                break
            
            if user_input.lower() == 'history':
                bot.show_history()
                continue
            
            # Get response
            response = bot.chat(user_input)
            print(f"🤖 Bot: {response}\n")
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    # Check Python version
    import sys
    if sys.version_info < (3, 6):
        print("⚠️  Please use Python 3.6 or higher")
        sys.exit(1)
    
    main()
