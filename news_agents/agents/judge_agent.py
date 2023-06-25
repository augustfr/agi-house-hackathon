import json
from news_agents.agents.agent import Agent


class JudgeAgent(Agent):
    def __init__(self, **kwargs):
        Agent.__init__(self, **kwargs)

    def judge(self, file_content):
        self.update_message_thread(
            "user", "Here are the pitches to judge: " + file_content
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
            print("==========RAW JUDGE OUTPUT==========")
            print(response_content)
            print("\n==========END RAW JUDGE OUTPUT==========")

        return json.loads(response_content).get("pitch_num")
