import json

from news_agents.agents.script_agent import ScriptAgent
from news_agents.agents.sorter_agent import SorterAgent
from news_agents.agents.pitch_agent import PitchAgent
from news_agents.agents.judge_agent import JudgeAgent
from news_agents.agents.transition_agent import TransitionAgent
from news_agents.rss import FeedReader


def run_main_loop(
    scripter: ScriptAgent, sorter: SorterAgent, pitcher: PitchAgent, judge: JudgeAgent
) -> bool:
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

    sorted_headlines = sorter.sort_headlines(headlines)
    pitches = []
    for headline in sorted_headlines:
        index = headline["index"]
        body = reader.read_article(index)["body"]
        pitch = pitcher.write_pitch(body)
        pitches.append({"index": index, "pitch": pitch})

    pitches_string = json.dumps(pitches)

    best_pitch_num = judge.judge(pitches_string)

    script = scripter.write_script(reader.read_article(best_pitch_num)["body"])

    # read script
