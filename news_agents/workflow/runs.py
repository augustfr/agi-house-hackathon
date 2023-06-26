import json

from news_agents.agents.script_agent import ScriptAgent
from news_agents.agents.sorter_agent import SorterAgent
from news_agents.agents.pitch_agent import PitchAgent
from news_agents.agents.judge_agent import JudgeAgent
from news_agents.agents.transition_agent import TransitionAgent
from news_agents.rss import FeedReader
from traceback import print_exc

from time import sleep

import socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('10.1.8.110', 8080)
client.sendto(b'Starting transmission', ('10.1.8.110', 8080))

# send json data
def send_data(data):
    # print sending type:
    print("sending data type: ", type(data))
    # send data as json
    for obj in data:
        client.sendto(json.dumps(obj).encode(), server_address)


def retry_on_failure(func, *args, retries=10, **kwargs):
    for i in range(retries):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            print("got invalid JSON response, retrying...")
            if i == retries - 1:
                raise e


def run_main_loop(
    scripter: ScriptAgent,
    sorter: SorterAgent,
    pitcher: PitchAgent,
    judge: JudgeAgent,
    transitioner: TransitionAgent,
) -> bool:
    memory = {
        "stories_ran": [],
        "previous_story": "",
    }

    introduction_msg = (
        """welcome to ByteFeedNews! Our 24/7 livestream is starting now!"""
    )

    count = 0
    while True:
        try:
            reader = FeedReader("http://feeds.bbci.co.uk/news/rss.xml")
            feed = ""
            headlines = ""
            for idx, article in enumerate(reader.feed):
                index = "index: " + str(idx) + "\n"
                title = "title: " + article["title"] + "\n"
                summary = "summary: " + article["summary"] + "\n"
                headlines += index
                feed += index
                headlines += title
                feed += title
                headlines += summary
                feed += summary
                feed += "link: " + article["link"] + "\n"
                feed += "published: " + article["published"] + "\n"
                feed += "\n"

            original_dict = sorter.sort_headlines(headlines, memory["stories_ran"])
            sorted_headlines = [
                {
                    "specialist": original_dict["specialist_1"],
                    "headline": original_dict["headline_1"],
                    "index": original_dict["index_1"],
                },
                {
                    "specialist": original_dict["specialist_2"],
                    "headline": original_dict["headline_2"],
                    "index": original_dict["index_2"],
                },
                {
                    "specialist": original_dict["specialist_3"],
                    "headline": original_dict["headline_3"],
                    "index": original_dict["index_3"],
                },
            ]
            pitches = []
            for headline in sorted_headlines:
                index = headline["index"]
                body = reader.read_article(index)["body"]
                pitch = retry_on_failure(pitcher.write_pitch, body)
                pitches.append({"index": index, "pitch": pitch})

            pitches_string = json.dumps(pitches)

            best_pitch_num = retry_on_failure(judge.judge, pitches_string)

            script = retry_on_failure(
                scripter.write_script, reader.read_article(best_pitch_num)["body"]
            )

            if memory["previous_story"] == "":
                send_data([{"author": "Arnold", "message": introduction_msg}])
            else:
                transition = retry_on_failure(
                    transitioner.generate_transition, script, memory["previous_story"]
                )

                send_data([{"author": "Arnold", "message": transition["transition"]}])

                # speech_queue.add_text(transition["transition"], "Arnold")

            memory["previous_story"] = script

            for s_obj in script:
                send_data([{"author": s_obj['author'], "message": s_obj["message"]}])

            count += 1

            if count == 3:
                sleep(1000000)
        except Exception as e:
            print_exc()
