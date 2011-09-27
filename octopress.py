import sublime, sublime_plugin, glob, os, subprocess, time

class OctoPostCommand(sublime_plugin.WindowCommand):

  def description(self):
    return "Creates a new octopress post"
  
  def run(self):
    print("hello?")
    try:
      octopress_dir = self.find_octopress_dir().next()
      print("Octopress dir: %s" % octopress_dir)
      self.new_post_in(octopress_dir)
    except:
      sublime.error_message(u'Cannot find octopress dir!')
      
  def new_post_done(self, text):
    result = subprocess.Popen(
      'rake new_post["%s"]' % text, 
      shell  = True, 
      stdout = subprocess.PIPE, 
      stderr = subprocess.STDOUT, 
      cwd    = self.octopress_dir
    ).communicate()[0]
    print(result)
    filename = os.path.join(self.octopress_dir, result.replace('Creating new post: ', '').replace('\n', ''))
    print("Opening %s" % filename)
    self.window.open_file(filename)


  ##TODO: improve octopress dir criteria  
  def find_octopress_dir(self):
    for directory in self.window.folders():
      print(os.path.join(directory, u'Rakefile'))
      if glob.glob(os.path.join(directory, u'Rakefile')):
        yield directory

  def new_post_in(self, octopress_dir):
    self.octopress_dir = octopress_dir
    self.window.show_input_panel("Post title", "", self.new_post_done, None, None)

  
    

      

