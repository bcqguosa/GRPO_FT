# train_grpo.py
from datasets import load_dataset
from trl import GRPOConfig, GRPOTrainer

dataset = load_dataset("trl-lib/tldr", split="train")

# Define the reward function, which rewards completions that are close to 50 characters
def reward_len(completions, **kwargs):
    return [-abs(50 - len(completion)) for completion in completions]

training_args = GRPOConfig(
    output_dir="Qwen2-0.5B-GRPO")

trainer = GRPOTrainer(
    model="Qwen/Qwen2-0.5B-Instruct",
    reward_funcs=reward_len,
    args=training_args,
    train_dataset=dataset,
)
trainer.train()

#Execute the script
#accelerate launch train_grpo.py