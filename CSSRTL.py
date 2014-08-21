
import sublime, sublime_plugin, re, os

SETTINGS_FILE = 'CSSRTL.sublime-settings'
class CssrtlExecCommand(sublime_plugin.WindowCommand):
	def run(self, files=[]):

		settings = sublime.load_settings(SETTINGS_FILE)
		if os.name == "posix":
			path = "/usr/local/bin:" + os.environ['PATH']
			cmd = 'cssrtl'
		else:
			path = os.environ['PATH']
			cmd = 'cssrtl.cmd'

		paths =map (os.path.dirname, map(os.path.dirname, files)) 

		# , '/usr/local/lib/node_modules/css-flip-auto/bin/css-flip'
		print os.path.join(paths[0])
		self.window.run_command('exec', {
			'cmd': list( map(os.path.expanduser, [cmd]))  + settings.get('options', []),
			'path': path,
			'working_dir' : os.path.join(paths[0]),
			'line_regex': settings.get('line_regex', '.*// Line ([0-9]*), Pos ([0-9]*)$'),
			'file_regex': settings.get('file_regex', '(^[^# ]+.*$)')
		})

class CssrtlCommand(sublime_plugin.WindowCommand):

	def run(self):
		self.window.active_view().run_command('save');
		self.window.run_command('cssrtl_exec', {
			'files': [self.window.active_view().file_name()]
		})
	def is_visible(self):
		pattern = re.compile(r'(^.*\.css$)')
		return pattern.match(self.window.active_view().file_name())