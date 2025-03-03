from transformers import pipeline

# Load the model pipeline
qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-large")

def get_gardening_advice(question):
    # Refined prompt for detailed gardening advice
    prompt = f"Provide a detailed gardening advice with steps, tips, and potential challenges: {question}"
    
    # Generate more detailed advice with a larger max_length
    response = qa_pipeline(prompt, max_length=500, do_sample=False, temperature=0.7)
    return response[0]['generated_text']



# from transformers import AutoModelForCausalLM, AutoTokenizer

# tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-125M")
# model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-neo-125M")

# def get_gardening_advice(question):
#     input_ids = tokenizer.encode(f"Provide gardening advice: {question}", return_tensors="pt")
#     outputs = model.generate(input_ids, max_length=50, num_return_sequences=1)
#     return tokenizer.decode(outputs[0], skip_special_tokens=True)
