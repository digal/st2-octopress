import sublime, sublime_plugin

class PostCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    print("hello?")
    #error_message("run")  
    self.view.window().show_input_panel("New Post", "", self.done, None, None)
    #self.view.insert(edit, 0, "Hello, World!")

  def done(self, text):
    print(text)  
