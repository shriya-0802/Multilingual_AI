import google.generativeai as genai

# Use the correct parameter name 'api_key'
genai.configure(api_key="AIzaSyAYHTAAFcbFcIPqDO80XkP3pfamBRLvs1s")

# Convert the generator to a list to see all available models
models = list(genai.list_models())
print(models)
