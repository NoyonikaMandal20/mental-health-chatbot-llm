from datasets import load_dataset

ds = load_dataset("smolify/smolified-mental-health-chatbot")

ds["train"].select(range(1000)).to_csv("mental_health_dataset.csv")

print("Done!")