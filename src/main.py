import argparse
from src.generator import EmailPromptTemplate, OpenAIClient, EmailPostProcessor
from src.utils.logging import configure_logging

def main():
    configure_logging()
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--nombre", required=True)
    parser.add_argument("--contexto", required=True)
    parser.add_argument("--tono", default="formal")
    args = parser.parse_args()
    
    try:
        # Flujo completo
        prompt = EmailPromptTemplate().generate(vars(args))
        response = OpenAIClient("tu_api_key").send_prompt(prompt)
        email = EmailPostProcessor().process(response)
        
        print(f"Asunto: {email['asunto']}\n\n{email['cuerpo']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
