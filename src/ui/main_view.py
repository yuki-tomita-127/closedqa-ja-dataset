import gradio

def greet(greeting, name):
    return f"{greeting} {name}!"

with gradio.Blocks() as main_view:
    greeting = gradio.Textbox(label="greeting")
    name = gradio.Textbox(label="name")
    greet_button = gradio.Button("Greet")

main_view.launch()
