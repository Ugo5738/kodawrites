import json

dataset = []
articles = []
token_count = 0
with open('corpus.txt') as f:
    lines = f.read() # lines()
    articles = lines.split("\n\n\n\n")

    for article in articles:
        first_split = article.split("\n\n\n")
        top_split = first_split[0].split("\n\n")
        bottom_split = first_split[-1].split("\n\n")
        
        title = ''
        if len(top_split[0].split("\n")) == 3:
            title = top_split[0].split("\n")[1]
        elif len(top_split[0].split("\n")) == 3:
            title = top_split[0].split("\n")[0]
        keywords = first_split[-1].split("\n")[-1]
        prompt_text = title + "->" + keywords + "\n\n###\n\n"
        body_text = first_split[0].split("\n\n")[1:]
        body = ''
        for text in body_text:
            body = body + text + "\n"
        body = body + "\n\nEND"

        if len(body) > 1100 or body[:-3] == "\n\n":
            continue
        
        token_count += len(prompt_text + f" {body}")
        davinci_cost = (token_count/1000)*0.02

        dictionary = {"prompt": prompt_text, "completion": f" {body}"}
        dataset.append(dictionary)

print(len(dataset))
with open("dataset.json", "w") as outfile:
    json.dump(dataset, outfile)


# Prepare dataset
# !openai tools fine_tunes.prepare_data -f dataset.json

# Create Finetuned model
# !openai api fine_tunes.create -t dataset_prepared.jsonl -m davinci --n_epochs 2

# Delete Fine tuned model
# openai.Model.delete(FINE_TUNED_MODEL)