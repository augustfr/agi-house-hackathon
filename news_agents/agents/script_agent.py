import json
from news_agents.agents.agent import Agent


class ScriptAgent(Agent):
    def __init__(self, **kwargs):
        Agent.__init__(self, **kwargs)

    def get_file_summary(self, file_content):
        self.update_message_thread("user", "The article to summarize: " + file_content)
        messages = self.message_thread
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

        return json.loads(response_content).get("summary")
