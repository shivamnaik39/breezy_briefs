from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load the pre-trained T5 model and tokenizer
model = T5ForConditionalGeneration.from_pretrained('t5-base')
tokenizer = T5Tokenizer.from_pretrained('t5-base')

# Define the input text
input_text = "The quick brown fox jumps over the lazy dog. The dog barks loudly, but the fox ignores it."

# Tokenize the input text
input_ids = tokenizer.encode(input_text, return_tensors='pt')

# Generate a summary from the input text
summary_ids = model.generate(
    input_ids, num_beams=4, max_length=50, early_stopping=True)
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

# Print the summary
print(summary)
