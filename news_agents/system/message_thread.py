import yaml
import copy
from typing import TypedDict, List, Dict, Optional


class MessageThread(TypedDict):
    role: str
    content: Optional[str]  # Use Optional for keys that might not exist
    function_call: Optional[Dict]


def load_yaml(agent_name: str) -> Dict:
    with open(f"news_agents/agents/config/{agent_name}.yaml", "r") as file:
        return yaml.safe_load(file)


def get_agent_data(yaml_data: List[Dict], agent_name: str) -> Dict:
    for data in yaml_data:
        if data["agent"]["name"] == agent_name:
            return data["agent"]
    raise ValueError(f"No agent found with name: {agent_name}")


def init_prompt(agent_name: str) -> List[MessageThread]:
    yaml_data = load_yaml(agent_name)
    agent_data = get_agent_data(yaml_data, agent_name)
    system_prompt: MessageThread = {
        "role": agent_data["system_prompt"]["role"],
        "content": agent_data["system_prompt"]["content"],
    }
    few_shot_prompt = agent_data.get("few_shot_prompt", [])

    # Initialize the list with the system prompt
    messageThreads = [copy.deepcopy(system_prompt)]

    # Add all few_shot_prompt threads
    for thread in few_shot_prompt:
        new_thread: MessageThread = {
            "role": thread["role"],
            "content": thread.get("content"),
        }
        # Only add function_call if it exists
        if "function_call" in thread:
            new_thread["function_call"] = thread["function_call"]

        messageThreads.append(copy.deepcopy(new_thread))

    return messageThreads
