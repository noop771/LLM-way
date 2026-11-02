import re

with open("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

print(f"Всего символов: {len(raw_text)}")

preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]

all_tokens = sorted(set(preprocessed))
all_tokens.extend(["<|endoftext|>", "<|unk|>"])

vocab = {token: i for i, token in enumerate(all_tokens)}


class SimpleTokenizerV2:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {i: s for s, i in vocab.items()}

    def encode(self, text):
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]

        preprocessed = [
            item if item in self.str_to_int else "<|unk|>"
            for item in preprocessed
        ]
        ids = [self.str_to_int[token] for token in preprocessed]
        return ids

    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)
        return text


print(f"Количество токенов: {len(preprocessed)}")
print(f"Размер словаря: {len(vocab)}")

tokenizer = SimpleTokenizerV2(vocab)

test_text = "Hello, do you like tea? <|endoftext|> In the sunlit terraces of the palace."
print("\nОригинал:", test_text)

encoded = tokenizer.encode(test_text)
print("Закодировано:", encoded[:10], "...")

decoded = tokenizer.decode(encoded)
print("Декодировано:", decoded)