from app import Config
from openai import OpenAI

class EmailClassifier:
    def __init__(self):
        try:
            api_key = Config.OPENAI_API_KEY
            if api_key:
                self.openai_client = OpenAI(api_key=api_key)
                print("OpenAI client initialized successfully")
            else:
                self.openai_client = None
                print("OPENAI_API_KEY not found")
        except Exception as e:
            print(f"Error to initialize OpenAI client: {e}")

    def classify_email(self, email_text):
        try:
            response = self.openai_client.chat.completions.create(
                model="gpt-3.5-turbo", 
                messages=[
                    {
                        "role": "system",
                        "content": """
Você é um assistente especializado em classificar emails corporativos.
Classifique o email em uma das categorias:
- "Produtivo": Emails que requerem ação (suporte, solicitações, dúvidas técnicas, status)
- "Improdutivo": Emails que não requerem ação (felicitações, agradecimentos, mensagens casuais)

Responda APENAS com um JSON no formato:
{"category": "Produtivo" ou "Improdutivo"}
"""
                    },
                    {
                        "role": "user",
                        "content": f"Classifique este email:\n\n{email_text}"
                    }
                ],
                temperature=0.3,
                max_tokens=50
            )

            import json
            result_text = response.choices[0].message.content.strip()
            
            result = json.loads(result_text)
            category = result.get('category', 'Produtivo')

            #print(f"Classified category: {category}")
            #print(f"Processed text: {email_text}")

            return {
                'category': category,
                'processed_text': email_text
            }
        except Exception as e:
            print(f"Error during classification: {e}")

            #TODO: Melhorar o tratamento de erros e logging da classificação
            return {
                'category': 'Produtivo',
                'processed_text': email_text
            }

    def generate_response(self, category, original_text):
        try:
            if category == "Produtivo":
                system_prompt = """
Você é um assistente de atendimento profissional de uma empresa financeira.
Gere uma resposta educada e profissional para emails produtivos (que requerem ação).
A resposta deve:
- Confirmar recebimento
- Informar que a solicitação está sendo analisada
- Ser cordial e profissional
- Ter no máximo 100 palavras"""
            else:
                system_prompt = """
Você é um assistente de atendimento profissional de uma empresa financeira.
Gere uma resposta educada e breve para emails improdutivos (felicitações, agradecimentos).
A resposta deve:
- Agradecer pela mensagem
- Ser cordial e simpática
- Ter no máximo 50 palavras"""

            response = self.openai_client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Gere uma resposta para este email:\n\n{original_text[:500]}"}
                ],
                temperature=0.7,
                max_tokens=200
            )
            
            generated_response = response.choices[0].message.content.strip()

            #print(f"Generated response: {generated_response}")

            return generated_response

        except Exception as e:
            print(f"Error during response generation: {e}")

            #TODO: Melhorar o tratamento de erros e logging da geração de resposta
            return "Ocorreu um erro durante a geração da resposta. Tente novamente mais tarde."

    def classify_and_respond(self, email_text):
        classification_result = self.classify_email(email_text)
        
        if not classification_result:
            return {
                'category': 'Produtivo',
                'processed_text': email_text,
                'suggested_response': 'Obrigado pelo seu email. Estamos analisando sua solicitação.'
            }

        suggested_response = self.generate_response(
            classification_result['category'],
            email_text
        )

        return {
            'category': classification_result['category'],
            'processed_text': classification_result['processed_text'],
            'suggested_response': suggested_response
        }