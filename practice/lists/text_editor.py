class ActionNode:
    def __init__(self, action, next=None):
        self.action = action
        self.next = next


class ActionStack:
    def __init__(self):
        self._top = None

    def push(self, action):
        self._top = ActionNode(action, self._top)

    def pop(self):
        if not self._top:
            return None
        action = self._top.action
        self._top = self._top.next
        return action

    def is_empty(self):
        return self._top is None

    def peek(self):
        return self._top.action if self._top else None


class SimpleEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = ActionStack()
        self.redo_stack = ActionStack()

    def type(self, word):
        self.text += word
        self.undo_stack.push(("type", word))
        self.redo_stack = ActionStack()

    def delete(self, n):
        if n <= 0:
            return  # Don't delete anything if n is zero or negative
        deleted = self.text[-n:]
        self.text = self.text[:-n]
        self.undo_stack.push(("delete", deleted))
        self.redo_stack = ActionStack()

    def undo(self):
        action = self.undo_stack.pop()
        if not action:
            return "Nothing to undo"
        act_type, data = action
        if act_type == "type":
            self.text = self.text[: -len(data)]
        elif act_type == "delete":
            self.text += data
        self.redo_stack.push(action)

    def redo(self):
        action = self.redo_stack.pop()
        if not action:
            return "Nothing to redo"
        act_type, data = action
        if act_type == "type":
            self.text += data
        elif act_type == "delete":
            self.text = self.text[: -len(data)]
        self.undo_stack.push(action)

    def get_text(self):
        return self.text


# Simulate actions
editor = SimpleEditor()
editor.type("Hello")
editor.type(" World")
editor.delete(6)  # remove " World"
undo_text = editor.get_text()
print(undo_text)
editor.undo()  # undo delete
redo_text = editor.get_text()
editor.redo()  # redo delete
final_text = editor.get_text()
