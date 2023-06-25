import json
from news_agents.agents.agent import Agent


class SorterAgent(Agent):
    def __init__(self, **kwargs):
        Agent.__init__(self, **kwargs)

    def sort_headlines(self, headlines, ran_stories):
        messages = self.message_thread
        self.update_message_thread("user", "Here are the headlines: " + headlines)
        # if ran_stories list is not empty
        if len(ran_stories) > 0:
            stories = ""
            for story in ran_stories:
                stories = stories + 'title: ' + story['title']
                stories = stories + 'link: ' + story['link']

            print("==========PREV. RAN STORIES==========")
            print(stories)

            self.update_message_thread("user", "Here are the stories you have already run: " + stories + "DO NOT use these stories again.")
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
