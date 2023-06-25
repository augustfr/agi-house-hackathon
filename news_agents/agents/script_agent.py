import json
from news_agents.agents.agent import Agent


class ScriptAgent(Agent):
    def __init__(self, **kwargs):
        Agent.__init__(self, **kwargs)

    def write_script(self, file_content):
        self.update_message_thread(
            "user", "The article to write the script for: " + file_content
        )
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
            print("==========RAW SCRIPTER OUTPUT==========")
            print(response_content)
            print("\n==========END RAW SCRIPTER OUTPUT==========")

        return json.loads(response_content).get("summary")
