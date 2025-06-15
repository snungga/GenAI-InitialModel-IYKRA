from transformers import pipeline, set_seed
import torch

class GenerativeAIModel:
    def __init__(self):
        set_seed(42)
        # Using a lightweight model for demo
        self.generator = pipeline('text-generation', 
                                model='gpt2',
                                device=0 if torch.cuda.is_available() else -1)
    
    def generate_text(self, prompt, max_length=100):
        try:
            result = self.generator(prompt, 
                                  max_length=max_length, 
                                  num_return_sequences=1, 
                                  temperature=0.7,
                                  pad_token_id=50256)
            return result[0]['generated_text']
        except Exception as e:
            return f"Error generating text: {str(e)}"
    
    def health_check(self):
        return "Model is healthy and ready"