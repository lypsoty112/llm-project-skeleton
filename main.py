from src.controller import Controller

controller = Controller()

message = input("Enter a message: ")
data = {
    "history": [{
        "content": message, "role": "human"
    }]
}

output = controller.run(data)

print(output.message.content)
