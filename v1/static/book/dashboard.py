import asyncio
from thingsdb.client import Client
from thingsdb.room import Room, event


class Dashboard(Room):
    @event("add-todo")
    def on_add_todo(self, user_id):
        self.get_user(user_id)["count"] += 1
        self.print_state()

    @event("add-user")
    def on_add_user(self, user):
        self.state.append(user)
        self.print_state()

    @event("mark-as-done")
    def on_mark_as_done(self, user_id):
        self.get_user(user_id)["count"] -= 1
        self.print_state()

    def get_user(self, user_id):
        for user in self.state:
            if user["id"] == user_id:
                return user

    def on_init(self):
        # Called on initialization
        self.state = []

    async def on_join(self):
        # Called when joining the room
        self.state = await self.client.run("get_dashboard_state")
        self.print_state()

    def print_state(self):
        print('-' * 20)
        for user in self.state:
            name, count = user["name"], user["count"]
            print(f"{name:<15}{count:>5}")

    @event("chat-message")
    def on_chat_message(self, message):
        print(message)


async def main():
    client = Client()
    client.set_default_scope('//todos')

    room = Dashboard("""//ti
        .dashboard.id();
    """)

    await client.connect('localhost')
    try:
        await client.authenticate('<TOKEN_OR_USERNAME_AND_PASSWORD>')
        await room.join(client)
        await asyncio.Future()  # run forever
    finally:
        client.close()
        await client.wait_closed()

asyncio.run(main())