# Octopress plugin for Sublime Text 2

## Pitfalls

Plugin assumes that you have your octopress folder opened in the file pane. For now, 'octopress folder' means 'first folder with Rakefile in it' :) 

OS X Pitfall: Octopress uses rake, which uses ruby. If you run Sublime Text 2 from the GUI (dock/launchpad/etc.) it may not see your bash environment, including your usual ruby path. To fix this you need to add necessary environment variables to `~/.MacOSX/environment.plist`. It could be done manually or using a simple script like [this one](http://hints.macworld.com/article.php?story=20040715133738459). The changes to the environment symbol definitions will become active the next time you log in.

## Installation 

Copy/clone repo contents to `Packages/Octopress` directory.

## Commands supported (Tools/Octopress)

- `New post...` - create a new post (asks for title)
- `Deploy` - deploys blog (may block for a few seconds, to be improved in the future)

## TODO

- Better packaging
- Other commands (generate, preview, etc.)
- Store octopress dir in config

## Links

- [Sublime text 2](http://www.sublimetext.com/2)
- [Octopress](http://octopress.org/)