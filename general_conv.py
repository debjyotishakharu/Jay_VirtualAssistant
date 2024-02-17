
######DIALOGPT################
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "microsoft/DialoGPT-large"

tokenizer = AutoTokenizer.from_pretrained(model_name, padding_side="left")
model = AutoModelForCausalLM.from_pretrained(model_name)


def dialogpt_conv(user_command):

    input_text = user_command
#     input_ids = tokenizer.encode(input_text + tokenizer.eos_token, return_tensors="pt")
# # generate a bot response
#     chat_history_ids = model.generate(
#         input_ids,
#         max_length=1000,
#         do_sample=True,
#         top_k=100,
#         temperature=0.2,
#         pad_token_id=tokenizer.eos_token_id
#     )
#     #print the output
#     output = tokenizer.decode(chat_history_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
#     return output
    new_user_input_ids = tokenizer.encode(input_text + tokenizer.eos_token, return_tensors='pt')

    # append the new user input tokens to the chat history
    bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1)
    # generated a response while limiting the total chat history to 1000 tokens, 
    chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

    # pretty print last ouput tokens from bot
    output=tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    return output
#################################################################################

