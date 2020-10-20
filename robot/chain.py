import os

import markovify


class Chain:
    if os.path.exists("chain.json"):
        with open("chain.json", "r+") as fh:
            chain_json = fh.read()

        chain = markovify.Text.from_json(chain_json)
    else:
        chain = None

    def write_to_disk(self):
        with open("chain.json", "w") as fh:
            fh.write(self.chain.to_json())

    def add_string(self, string: str):
        additional_chain = markovify.Text(string, retain_original=False)

        if self.chain:
            self.chain = markovify.combine([self.chain, additional_chain])
        else:
            self.chain = markovify.Text(string, retain_original=False)

        self.write_to_disk()

    def create_sentence(self) -> str:
        return self.chain.make_short_sentence(300, min_chars=25)
