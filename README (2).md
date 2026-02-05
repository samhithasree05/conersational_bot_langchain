# Conversational Knowledge Bot with LangChain

A powerful conversational AI bot built with LangChain, featuring tool integration, memory management, and RAG (Retrieval-Augmented Generation) capabilities.

## 🌟 Features

### Basic Version (`conversational_bot.py`)
- **Conversational Memory**: Remembers conversation context
- **Tool Integration**: Calculator, weather, knowledge base, time
- **Agent-based Reasoning**: Automatically selects appropriate tools
- **Simple and Clean**: Easy to understand and extend

### Advanced Version (`advanced_bot.py`)
- **Enhanced Tools**: Advanced calculator, unit converter, note-taking
- **RAG Knowledge Base**: Vector-based semantic search
- **Persistent Sessions**: Save and resume conversations
- **Multiple Memory Types**: Buffer or summary memory
- **Session Management**: Track and manage multiple sessions

## 📋 Prerequisites

- Python 3.8 or higher
- Anthropic API key ([Get one here](https://console.anthropic.com/))

## 🚀 Installation

1. **Clone or download the files**

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Set up your API key**:
```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

Or create a `.env` file:
```
ANTHROPIC_API_KEY=your-api-key-here
```

## 💻 Usage

### Basic Bot

```bash
python conversational_bot.py
```

**Example Interactions:**

```
👤 You: What's 25 * 4 + 10?
🤖 Bot: Let me calculate that for you. The result is 110.

👤 You: What's the weather like in London?
🤖 Bot: Current weather in London: 15°C, Cloudy with occasional rain

👤 You: Tell me about Python
🤖 Bot: Python is a high-level, interpreted programming language...
```

### Advanced Bot

```bash
python advanced_bot.py
```

**Example Commands:**

```bash
# Advanced calculations
Calculate sqrt(144) + log(100)

# Unit conversion
Convert 25,celsius,fahrenheit

# Note taking
Save a note: Buy groceries tomorrow|personal

# Retrieve notes
What are my personal notes?

# Knowledge search
Tell me about machine learning
```

## 🛠️ Available Tools

### Basic Version Tools

| Tool | Description | Example |
|------|-------------|---------|
| Calculator | Basic math operations | `2 + 2 * 3` |
| Weather | Get weather info | `weather in Tokyo` |
| KnowledgeBase | Search tech topics | `What is Python?` |
| CurrentTime | Get current time | `What time is it?` |

### Advanced Version Tools

| Tool | Description | Example |
|------|-------------|---------|
| Calculator | Advanced math (sqrt, sin, cos, log) | `sqrt(16) + log(100)` |
| UnitConverter | Convert units | `25,celsius,fahrenheit` |
| NoteTaker | Save notes by category | `Meeting notes\|work` |
| RetrieveNotes | Get saved notes | `work` |
| KnowledgeSearch | RAG-based semantic search | `machine learning` |

## 🎯 Commands

Both versions support these commands:

- `quit` or `exit` - Exit the bot
- `clear` - Clear conversation memory
- `stats` - Show session statistics (advanced only)
- `new session` - Start a new session (advanced only)

## 📚 Architecture

### Basic Bot Architecture

```
User Input
    ↓
LangChain Agent
    ↓
Tool Selection (Calculator, Weather, etc.)
    ↓
Conversation Memory (Buffer)
    ↓
Response Generation
```

### Advanced Bot Architecture

```
User Input
    ↓
LangChain Agent with Tools
    ↓
┌─────────────────┬──────────────────┬─────────────┐
│  Enhanced Tools │   RAG Knowledge  │   Session   │
│   (Calculator,  │   Base (Vector   │  Management │
│   Converter,    │   Search with    │  (Persistent│
│   Note-taking)  │   Embeddings)    │   Storage)  │
└─────────────────┴──────────────────┴─────────────┘
    ↓
Conversation Memory (Buffer/Summary)
    ↓
Response Generation
```

## 🔧 Customization

### Adding Custom Tools

```python
def custom_tool_function(input_param: str) -> str:
    """Your custom tool logic"""
    # Process the input
    result = process(input_param)
    return f"Result: {result}"

# Add to tools list
Tool(
    name="CustomTool",
    func=custom_tool_function,
    description="Description of what your tool does"
)
```

### Adding Knowledge Documents

```python
# In advanced_bot.py
document = Document(
    page_content="Your content here...",
    metadata={"topic": "your_topic", "type": "category"}
)

bot.rag.add_document(document.page_content, document.metadata)
```

### Changing Memory Type

```python
# Use summary memory instead of buffer
bot = AdvancedConversationalBot(
    session_id="my_session",
    memory_type="summary"  # or "buffer"
)
```

## 📊 Memory Types

### ConversationBufferMemory
- **Pros**: Preserves full conversation history
- **Cons**: Can get large with long conversations
- **Best for**: Short to medium conversations

### ConversationSummaryMemory
- **Pros**: Summarizes old messages, saves tokens
- **Cons**: May lose some details
- **Best for**: Long conversations

## 🔐 Security Notes

1. **API Keys**: Never commit API keys to version control
2. **Tool Execution**: Calculator uses safe evaluation (no `exec()`)
3. **File Access**: Note-taking tools create files in local directory only

## 🐛 Troubleshooting

### "ANTHROPIC_API_KEY not found"
```bash
# Make sure you've set the environment variable
export ANTHROPIC_API_KEY='your-key-here'

# Or add it to your .env file
echo "ANTHROPIC_API_KEY=your-key-here" > .env
```

### Import Errors
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

### Memory Issues with Long Conversations
```bash
# Use the 'clear' command to reset memory
# Or switch to summary memory in advanced bot
```

## 📈 Performance Tips

1. **Use Summary Memory**: For long conversations to save tokens
2. **Limit Tool Iterations**: Set `max_iterations` appropriately
3. **Batch Similar Queries**: Ask related questions together
4. **Clear Memory**: Regularly clear memory for fresh starts

## 🤝 Contributing

Feel free to extend this bot with:
- More tools (database access, email, etc.)
- Better knowledge base integration
- Multi-modal capabilities (images, audio)
- Different LLM providers
- Custom memory implementations

## 📝 Example Use Cases

### Personal Assistant
```python
# Track tasks, take notes, do calculations
"Save a note: Team meeting at 3 PM|work"
"What are my work notes?"
"Calculate my monthly savings: 5000 - 3200"
```

### Learning Assistant
```python
# Search knowledge base, get explanations
"What is machine learning?"
"Explain Python programming"
"Compare supervised and unsupervised learning"
```

### Data Analysis Helper
```python
# Calculations, conversions, data queries
"Calculate the average: (45 + 67 + 89 + 23) / 4"
"Convert 100,kg,lbs"
```

## 🎓 Learning Resources

- [LangChain Documentation](https://python.langchain.com/)
- [Anthropic API Docs](https://docs.anthropic.com/)
- [LangChain Agents Guide](https://python.langchain.com/docs/modules/agents/)
- [RAG Tutorial](https://python.langchain.com/docs/use_cases/question_answering/)

## 📄 License

This project is provided as-is for educational purposes.

## 🙏 Acknowledgments

- Built with [LangChain](https://github.com/langchain-ai/langchain)
- Powered by [Anthropic Claude](https://www.anthropic.com/)
- Vector search with [FAISS](https://github.com/facebookresearch/faiss)

---

**Happy Chatting! 🤖💬**
