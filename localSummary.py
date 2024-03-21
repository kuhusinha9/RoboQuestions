from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

def localSummary(text):
    tokenizer = AutoTokenizer.from_pretrained("pszemraj/long-t5-tglobal-base-16384-book-summary")
    model = AutoModelForSeq2SeqLM.from_pretrained("pszemraj/long-t5-tglobal-base-16384-book-summary")
    params = {
        "max_length": 500,
        "min_length": 8,
        "no_repeat_ngram_size": 3,
        "early_stopping": True,
        "repetition_penalty": 3.5,
        "length_penalty": 0.3,
        "encoder_no_repeat_ngram_size": 3,
        "num_beams": 4,
    } 

    summarizer = pipeline(
        "summarization",
        model=model,
        tokenizer=tokenizer,
    )

    result = summarizer(text, **params)
    return result[0]['summary_text']

with open("stories/chapter25.txt", 'r', encoding='utf-8') as f:
    t= f.read()

print(localSummary(t))
