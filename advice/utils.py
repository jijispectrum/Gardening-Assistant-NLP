from transformers import pipeline

# Load the model pipeline
qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-small")

def get_gardening_advice(question):
    # Generate gardening advice using the model
    prompt = f"Provide gardening advice: {question}"
    response = qa_pipeline(prompt, max_length=100, do_sample=True)
    return response[0]['generated_text']

# from transformers import AutoModelForCausalLM, AutoTokenizer

# tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-125M")
# model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-neo-125M")

# def get_gardening_advice(question):
#     input_ids = tokenizer.encode(f"Provide gardening advice: {question}", return_tensors="pt")
#     outputs = model.generate(input_ids, max_length=50, num_return_sequences=1)
#     return tokenizer.decode(outputs[0], skip_special_tokens=True)
