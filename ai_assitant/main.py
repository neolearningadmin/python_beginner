#!/usr/bin/env python3
from assistant import OpenAIAssistant
import argparse
from key import key


def main():
    parser = argparse.ArgumentParser(description="Simple OpenAI assistant CLI")
    parser.add_argument("--model", default="gpt-3.5-turbo", help="Model to use")
    args = parser.parse_args()

    assistant = OpenAIAssistant(model=args.model, api_key=key)

    print("Simple OpenAI assistant. Type 'exit' or Ctrl-C to quit.")
    while True:
        try:
            prompt = input("You are a philosophy teacher, answer my questions on philosophy \n").strip()
            if not prompt:
                continue
            if prompt.lower() in ("exit", "quit"):
                print("Goodbye.")
                break
            resp = assistant.ask(prompt)
            print("Assistant:", resp)
        except KeyboardInterrupt:
            print("\nGoodbye.")
            break
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
