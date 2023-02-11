import torch
from transformers import T5Tokenizer,T5ForConditionalGeneration,T5Config

#initialize pre-trained model
model=T5ForConditionalGeneration.from_pretrained("t5-small")
tokenizer=T5Tokenizer.from_pretrained("t5-small")
device=torch.device("cpu")

text="""
Back in the 1950s, the fathers of the field, Minsky and McCarthy, described artificial intelligence as any task performed by a machine that would have previously been considered to require human intelligence.

That's obviously a fairly broad definition, which is why you will sometimes see arguments over whether something is truly AI or not.

Modern definitions of what it means to create intelligence are more specific. Francois Chollet, an AI researcher at Google and creator of the machine-learning software library Keras, has said intelligence is tied to a system's ability to adapt and improvise in a new environment, to generalise its knowledge and apply it to unfamiliar scenarios.

"Intelligence is the efficiency with which you acquire new skills at tasks you didn't previously prepare for," he said.

"Intelligence is not skill itself; it's not what you can do; it's how well and how efficiently you can learn new things."

It's a definition under which modern AI-powered systems, such as virtual assistants, would be characterised as having demonstrated 'narrow AI', the ability to generalise their training when carrying out a limited set of tasks, such as speech recognition or computer vision.

Typically, AI systems demonstrate at least some of the following behaviours associated with human intelligence: planning, learning, reasoning, problem-solving, knowledge representation, perception, motion, and manipulation and, to a lesser extent, social intelligence and creativity.

AlexNet's performance demonstrated the power of learning systems based on neural networks, a model for machine learning that had existed for decades but that was finally realising its potential due to refinements to architecture and leaps in parallel processing power made possible by Moore's Law. The prowess of machine-learning systems at carrying out computer vision also hit the headlines that year, with Google training a system to recognise an internet favorite: pictures of cats.

The next demonstration of the efficacy of machine-learning systems that caught the public's attention was the 2016 triumph of the Google DeepMind A
"""

#preprocessing
preprocessed_text=text.strip().replace("\n","")

input_text='summarize: '+preprocessed_text
tokenized_text=tokenizer.encode(input_text,max_length=512,return_tensors="pt").to(device)
# print(input_text)
# print(tokenized_text)

#summarize
summary=model.generate(tokenized_text,min_length=30,max_length=120)
summary1=tokenizer.decode(summary[0],skip_special_tokens=True)
print(summary1)