import sublime, sublime_plugin, glob, os, subprocess, time, re


class OctoCommandBase(sublime_plugin.WindowCommand):

  ##TODO: improve octopress dir criteria  
  def find_octopress_dir(self):
    for directory in self.window.folders():
      print(os.path.join(directory, u'Rakefile'))
      if glob.glob(os.path.join(directory, u'Rakefile')):
        return directory
    return None


class OctoPostCommand(OctoCommandBase):

  def description(self):
    return "Creates a new octopress post"
  
  def run(self):
    print("hello?")
    octopress_dir = self.find_octopress_dir()
    if octopress_dir != None:
      print("Octopress dir: %s" % octopress_dir)
      self.new_post_in(octopress_dir)
    else:
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
    r = re.search('new post: (.*)$', result)
    postfile = r.groups(0)[0]
    filename = os.path.join(self.octopress_dir, postfile)
    print("Opening %s" % filename)
    self.window.open_file(filename)

  def new_post_in(self, octopress_dir):
    self.octopress_dir = octopress_dir
    self.window.show_input_panel("Post title", "", self.new_post_done, None, None)


class OctoDeployCommand(OctoCommandBase):

  def description(self):
    return "Deploys blog"

  def run(self):
    print("hello?")
    octopress_dir = self.find_octopress_dir()
    if octopress_dir != None:
      print("Octopress dir: %s" % octopress_dir)
      self.deploy_in(octopress_dir)
    else:
      sublime.error_message(u'Cannot find octopress dir!')

  def deploy_in(self, octopress_dir):
    result = subprocess.Popen(
      'rake deploy', 
      shell  = True, 
      stdout = subprocess.PIPE, 
      stderr = subprocess.STDOUT, 
      cwd    = octopress_dir
    ).communicate()[0]
    print(result)
    sublime.status_message(result)

  
    

      

