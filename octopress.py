import sublime, sublime_plugin, glob, os, subprocess, time

class PostCommand(sublime_plugin.TextCommand):
  
  def run(self, edit):
    print("hello?")
    octopress_dir = self.find_octopress_dir().next()
    print("Octopress dir: %s" % octopress_dir)
    self.new_post_in(octopress_dir)
    #except:
    #  sublime.error_message(u'Cannot find octopress dir!')
        
      
    #self.view.insert(edit, 0, "Hello, World!")

  def done(self, text):
    result = subprocess.Popen(
      'rake new_post["%s"]' % text, 
      shell = True, 
      stdout = subprocess.PIPE, 
      cwd = self.octopress_dir
    ).communicate()[0]
    print(result)
    filename = os.path.join(self.octopress_dir, result.replace('Creating new post: ', '').replace('\n', ''))
    print("Opening %s" % filename)
    self.view.window().open_file(filename)


  ##TODO: improve octopress dir criteria  
  def find_octopress_dir(self):
    for directory in self.view.window().folders():
      print(os.path.join(directory, u'Rakefile'))
      if (len(glob.glob(os.path.join(directory, u'Rakefile'))) > 0):
        yield directory

  def new_post_in(self, octopress_dir):
    self.octopress_dir = octopress_dir
    self.view.window().show_input_panel("Post title", "", self.done, None, None)
    

      

