import json
import yaml
import tiktoken
from news_agents.system.message_thread import init_prompt
from news_agents.llms.language_model import LanguageModel

enc = tiktoken.encoding_for_model("text-davinci-003")


class Agent:
    def __init__(
        self,
        name: str,
        language_model: LanguageModel,
        max_tokens: int,
        debug_mode: bool = False,
    ):
        self.message_thread = init_prompt(name)
        self.debug_mode = debug_mode
        self.name = name
        self.language_model = language_model
        self.max_tokens = max_tokens

        yaml_path = f"news_agents/agents/config/{name}.yaml"
        yaml_obj = self.load_yaml_file(yaml_path)

        function_json = self.convert_yaml_function_to_json(yaml_obj)

        self.function = json.loads(function_json)

    def load_yaml_file(self, filepath):
        with open(filepath, "r") as file:
            yaml_obj = yaml.safe_load(file)
        return yaml_obj

    def convert_yaml_function_to_json(self, yaml_list):
        # Initialize an empty dictionary for the function object
        function_obj = {}

        # Loop through the list, checking each dictionary
        for item in yaml_list:
            if "function" in item:
                function_obj = item["function"]
                break

        # Convert the function object to a JSON string
        json_str = json.dumps(function_obj, indent=4)

        return json_str

    def update_message_thread(self, role, content):
        self.message_thread.append({"role": role, "content": content})

    def message_token_count(self, msg) -> int:
        return len(enc.encode(msg["content"]))

    def format_message_thread(self, replacements, placeholders):
        messages = []
        for message in self.message_thread:
            updated_message = {}
            for key, value in message.items():
                if isinstance(value, str):
                    updated_message[key] = value
                    for placeholder in placeholders:
                        if "{" + placeholder + "}" in value:
                            try:
                                updated_message[key] = updated_message[key].replace(
                                    "{" + placeholder + "}", replacements[placeholder]
                                )
                            except KeyError as e:
                                raise ValueError(
                                    f"Missing replacement for placeholder: {e.args[0]}"
                                )
                else:
                    updated_message[key] = value
            messages.append(updated_message)
        return messages
