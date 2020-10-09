from telethon import events

from .chain import Chain

invalid_starters = ("/", ".", "g.", "e.", "emmy", "r.", "v.", "#", "!")


class EventHandler():
    chain = Chain()

    def __init__(self, client):
        self.client = client
        client.add_event_handler(self.handle_outgoing, events.NewMessage(outgoing=True, func=lambda e: not e.via_bot_id and not e.is_private and e.raw_text))

    async def handle_outgoing(self, event):
        if event.raw_text == ".chain":
            await event.edit(self.chain.create_sentence())
            return

        if not event.raw_text.startswith(invalid_starters):
            self.chain.add_string(event.raw_text)
