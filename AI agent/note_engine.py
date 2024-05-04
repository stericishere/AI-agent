from llama_index.core.tools import FunctionTool
import os

note_file = os.path.join("data", "notes.txt")
history = os.path.join("data", "history.txt")
# a simple function to save notes to a file
def saving_note(note):
    if not os.path.exists(note_file):
        open(note_file, "w")
    with open(note_file, "a") as f:
        f.writelines([note + "\n"])
    return "note saved"

def reading_notes():
    with open(note_file, "r") as f:
        notes = f.readlines()
    return notes

def check_history():
    with open(history, "r") as f:
        notes = f.readlines()
    return notes

note_engine = FunctionTool.from_defaults(
    fn=saving_note,
    name="note_saver",
    description="this tool save a text based note to a file for the user"
    )

reading_engine = FunctionTool.from_defaults(
    fn=reading_notes,
    name="note_reader",
    description="this tool reads a text based note from a file for the user"
    )

