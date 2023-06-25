from news_agents.agents.script_agent import ScriptAgent
from news_agents.agents.sorter_agent import SorterAgent
from news_agents.agents.pitch_agent import PitchAgent
from news_agents.agents.judge_agent import JudgeAgent


def run_main_loop(
    scripter: ScriptAgent, sorter: SorterAgent, pitcher: PitchAgent, judge: JudgeAgent
) -> bool:
    # basic workflow idea

    # do something to get a list of headlines
    # sorted_headlines = sorter.sort_headlines(headlines)
    # pitches = []
    # for headline in sorted_headlines:
    #     pitch = pitcher.pitch(headline)
    #     pitches += pitch # this will needed to be parsed before this will work
    # best_pitch = judge.judge(pitches)
    # script = scripter.write_script(best_pitch)
    # read script

    summary = scripter.write_script(
        """Russia says Wagner Group’s leader will move to Belarus after his rebellious march challenged Putin
          The ultra-wealthy have dangerous pastimes. Who pays when they need saving?
          Orca pod attacks Ocean Race boats
          Four players suspended after hostile soccer game between US and Mexico
          Israeli military kills Palestinian gunman as settlers rampage through Palestinian town
          Packages from China are surging into the United States. Some say $800 duty-free limit was a mistake
          One year later, the Supreme Court’s abortion decision is both scorned and praised
          Speaker McCarthy supports expunging Trump’s impeachments over Ukraine and Jan. 6"""
    )

    # sorter_test = sorter.sort_headlines(
    #     """Fox News v Tucker Carlson: dispute rumbles on weeks after messy exit
    #     2023 NCAA baseball bracket: Men's College World Series scores, schedule in Omaha
    #     Skin moles that grow hair may offer treatment for baldness, study suggests
    #     Prematch Reading | All the biggest news ahead of tonight's homestand finale against Toronto FC
    #     News Flash • Hopewell Township, NJ • CivicEngage
    #     Judge keeps no bond order for Ponte Vedra triple stabbing suspect
    #     Glastonbury: Watch Lizzo, Lewis Capaldi and Rick Astley perform
    #     """
    # )
