from news_agents.agents.summarizer_agent import SummarizerAgent


def run_main_loop(
    summarizer: SummarizerAgent,
) -> bool:
    summary = summarizer.get_file_summary("test content")
