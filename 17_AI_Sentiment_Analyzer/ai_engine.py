import os, json
from dotenv import load_dotenv
load_dotenv()

def generate_ai(user_input, system_instruction):
    """REAL GENERATIVE AI: IBM watsonx.ai foundation-model inference."""
    key=os.getenv("WATSONX_APIKEY")
    project=os.getenv("WATSONX_PROJECT_ID")
    if not key or not project:
        raise RuntimeError("Set WATSONX_APIKEY and WATSONX_PROJECT_ID in .env")
    from ibm_watsonx_ai import Credentials
    from ibm_watsonx_ai.foundation_models import ModelInference
    credentials=Credentials(
        url=os.getenv("WATSONX_URL","https://us-south.ml.cloud.ibm.com"),
        api_key=key
    )
    model=ModelInference(
        model_id=os.getenv("WATSONX_MODEL_ID","ibm/granite-4-h-small"),
        credentials=credentials,
        project_id=project,
        params={"max_new_tokens":900,"temperature":0.2}
    )
    prompt=f"""SYSTEM:
{system_instruction}

USER INPUT:
{user_input}

Generate a useful, accurate response. Do not claim to have accessed information that is not supplied."""
    return model.generate_text(prompt=prompt, guardrails=True)

if __name__=="__main__":
    print(generate_ai(input("Enter your input: "), 'You are the AI engine for 17 AI Sentiment Analyzer.\nProject category: Business.\nCore task: Classify sentiment and explain key emotional signals in feedback.\nReturn practical, structured results suitable for a student/hackathon demonstration.\nFor healthcare or legal topics, clearly distinguish educational/document assistance from professional diagnosis or legal advice.'))
