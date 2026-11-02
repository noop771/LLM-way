import re

with open("the-verdict.txt", "r", encoding="utf-8") as f:
	raw_text = f.read()

print(f"Всего символов: {len(raw_text)}")

#токены
preprocessed = raw_text.strip(r'([,.:;?_!"()\']|--|\s)')

preprocessed = [item.strip() for item in preprocessed if item.strip()]
print(preprocessed)

#уникальные токены

all_tokens = sorted(set(preprocessed))

token_to_id = {token: i for i, token in enumerate(all_tokens)}
print(token_to_id)

encoded_text = [token_to_id[token] for token in preprocessed]

print(f"Количество токенов: {len(preprocessed)}")
print(f"Размер словаря: {len(all_tokens)}")
print(f"Первые 10 токенов и их ID:")
for token in preprocessed[:10]:
    print(f"  '{token}' -> {token_to_id[token]}")