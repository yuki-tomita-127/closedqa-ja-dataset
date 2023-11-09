import json
import os

import gradio as gr


def register_data(instruction, input, output, url, sub_category):
    with open(f"data/{dataset_name.value}.json", "r") as f:
        data = json.load(f)
        data.append({
            "index": str(len(data)),
            "instruction": instruction,
            "input": input,
            "output": output,
            "url": url,
            "category": "closed_qa",
            "sub_category": sub_category
        })
    
    with open(f"data/{dataset_name.value}.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    return [None, None, None, None, None]

def clear_input():
    return [None, None, None, None, None]

def set_data(id):
    with open(f"data/{dataset_name.value}.json", "r") as f:
        data = json.load(f)
        selected_data = data[int(id)]
    
    return [selected_data["instruction"], selected_data["input"], selected_data["output"], selected_data["url"], selected_data["sub_category"]]


dataset_files = []
for file in os.listdir("data"):
    if file.endswith(".json"):
        dataset_files.append(file[:-5])

sub_categories = ["mathmatics", "psychology", "technology"]

with gr.Blocks(title="ClosedQA-ja-Dataset") as demo:
    dataset_name = gr.Dropdown(choices=dataset_files, value=dataset_files[0], label="dataset")
    with gr.Row(equal_height=True):
        with gr.Column():
            r_instruction = gr.Textbox(label="Instruction")
            r_input = gr.Textbox(label="Input")
            r_output = gr.Textbox(label="Output")
            r_url = gr.Textbox(label="URL")
            r_sub_category = gr.Dropdown(choices=sub_categories, label="Sub_category")
            with gr.Row():
                canecel_button = gr.Button("Cancel")
                canecel_button.click(fn=clear_input, outputs=[r_instruction, r_input, r_output, r_url, r_sub_category])
                register_button = gr.Button("Register", variant="primary")
                register_button.click(fn=register_data, inputs=[r_instruction, r_input, r_output, r_url, r_sub_category], outputs=[r_instruction, r_input, r_output, r_url, r_sub_category])
        with gr.Column():
            id = gr.Number(value=-1, label="ID")
            b_instruction = gr.Textbox(label="Instruction")
            b_input = gr.Textbox(label="Input")
            b_output = gr.Textbox(label="Output")
            b_url = gr.Textbox(label="URL")
            b_sub_category = gr.Dropdown(choices=sub_categories, label="Sub_category")
            id.change(fn=set_data, inputs=id, outputs=[b_instruction, b_input, b_output, b_url, b_sub_category])


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0") # on Docker
    # main.launch() # on local machine
