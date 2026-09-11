# 17 AI Sentiment Analyzer
Category: Business

## AI implementation
Classify sentiment and explain key emotional signals in feedback.

This project makes a real call to an IBM watsonx.ai foundation model through the `ibm-watsonx-ai` Python SDK. It is not a keyword/rule-based chatbot.

## Run
1. Python 3.10+
2. `python -m venv venv`
3. Windows: `venv\\Scripts\\activate`
4. `pip install -r requirements.txt`
5. Copy `.env.example` to `.env`
6. Add your IBM Cloud API key and watsonx.ai project ID
7. `python app.py`
8. Open http://127.0.0.1:5000

## Demo
Enter project-specific text in the box and click Generate with AI.

IBM watsonx.ai supports programmatic foundation-model inference through its APIs and Python library.
