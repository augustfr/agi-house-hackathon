import os
import json
from news_agents.agents.agent import Agent


class SummarizerAgent(Agent):
    def __init__(self, **kwargs):
        Agent.__init__(self, **kwargs)

    def read_file_content(self, file_path):
        with open(file_path, "r") as file:
            content = file.read()
        return content

    def get_file_summary(self, file_content):
        messages = []
        replacements = {"file_content": file_content}
        placeholders = ["file_content"]
        messages = self.format_message_thread(replacements, placeholders)

        completion = self.language_model.call(
            messages=messages,
            functions=[self.function],
            function_call={"name": self.function.get("name")},
        )

        total_tokens = sum(self.message_token_count(msg) for msg in messages)

        response_content = completion["choices"][0]["message"]["function_call"][
            "arguments"
        ]
        if self.debug_mode:
            print("==========RAW SUMMARIZER OUTPUT==========")
            print(response_content)
            print("\n==========END RAW SUMMARIZER OUTPUT==========")
        # response_tokens = self.message_token_count(
        #     {"role": "assistant", "content": response_content}
        # )
        # input_tokens = total_tokens - response_tokens

        # log_data = {
        #     "added_input": messages,
        #     "input_tokens": input_tokens,
        #     "completion": response_content,
        #     "completion_tokens": response_tokens,
        #     "full_prompt": messages,
        # }
        # save_log_to_file(log_data)

        return json.loads(response_content).get("summary")
