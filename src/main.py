import argparse
from generator.prompts import EmailPromptTemplate, EmailPromptInputs

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--nombre", required=True)
    parser.add_argument("--contexto", required=True)
    args = parser.parse_args()
    
    inputs = EmailPromptInputs(nombre=args.nombre, contexto=args.contexto)
    print(EmailPromptTemplate().generate(inputs))

if __name__ == "__main__":
    main()
