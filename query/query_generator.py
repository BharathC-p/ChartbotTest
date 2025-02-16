from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Load Open-Source NLP Model for Text-to-SQL
MODEL_NAME = "Salesforce/grappa_large"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

def generate_sql_query(nl_query):
    """Convert natural language to SQL"""
    inputs = tokenizer(nl_query, return_tensors="pt", padding=True, truncation=True)
    outputs = model.generate(**inputs)
    sql_query = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return sql_query
