# The broadcasters just finished this story: {news_story_script}\n\nWrite an engaging transition for the anchor to start talking about the new topic. Make sure it is a smooth change from the previous story to the new one. Here is the title and summary of the next topic: \n{next_topic}

import json
from news_agents.agents.agent import Agent


class TransitionAgent(Agent):
    def __init__(self, **kwargs):
        Agent.__init__(self, **kwargs)

    def generate_transition(self, previous_story, next_story):
        messages = self.message_thread
        self.update_message_thread("user", f"The broadcasters just finished this story: {previous_story}\n\nWrite an engaging transition for the anchor to start talking about the new topic. Make sure it is a smooth change from the previous story to the new one. Here is the title and summary of the next topic: \n{next_story}")
        completion = self.language_model.call(
            messages=messages,
            functions=[self.function],
            function_call={"name": self.function.get("name")},
        )

        response_content = completion["choices"][0]["message"]["function_call"][
            "arguments"
        ]
        if self.debug_mode:
            print("==========RAW SORTER OUTPUT==========")
            print(response_content)
            print("\n==========END RAW SORTER OUTPUT==========")

        return json.loads(response_content)
