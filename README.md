# agi-house-hackathon

install requirements:

```
pip3 install -r requirements.txt
```

run with:

```
python3 -m news_agents.main
```

## summary of the agents

1. SorterAgent
   This agent views an RSS feed and decides on 3 articles that are most relevant stories for the news day
   Input: RSS feed
   Output: three article text bodies.

2. PitchAgent
   This agent recieves an entire article text body and writes a pitch on why this is most relevant and exciting for the news day.
   There are 3 of these because SorterAgent picks 3 articles.
   Input: article text body
   Output: a natural language pitch

3. JudgeAgent
   This agent views all pitches and decides which is the best.
   Input: 3 pitches
   Output: a single pitch and a reason as to why it is the best.

4. ScriptWriterAgent
   This agent takes the article text body associated with the winning pitch and writes the actual script that will be converted to speech.
   Input: winning article text body
   Output: an engaging narrative / script that the newscaster will read

## main loop:

pass data from each agent
queue the ScriptWriterAgent text response into the audio player and continuesly play()
