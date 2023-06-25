import json
from news_agents.agents.agent import Agent


class PitchAgent(Agent):
    def __init__(self, **kwargs):
        Agent.__init__(self, **kwargs)

    def write_pitch(self, file_content):
        self.update_message_thread(
            "user", "The article to write the pitch for: " + file_content
        )
        messages = self.message_thread
        completion = self.language_model.call(
            messages=messages,
            functions=[self.function],
            function_call={"name": self.function.get("name")},
        )

        response_content = completion["choices"][0]["message"]["function_call"][
            "arguments"
        ]
        if self.debug_mode:
            print("==========RAW PITCHER OUTPUT==========")
            print(response_content)
            print("\n==========END RAW PITCHER OUTPUT==========")

        return json.loads(response_content).get("pitch")
