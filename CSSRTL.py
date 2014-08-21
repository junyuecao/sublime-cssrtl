
import sublime, sublime_plugin, re, os

SETTINGS_FILE = 'CSSRTL.sublime-settings'
class CssrtlExecCommand(sublime_plugin.WindowCommand):
	def run(self, files=[]):

		settings = sublime.load_settings(SETTINGS_FILE)
		if os.name == "posix":
			path = "/usr/local/bin:" + os.environ['PATH']
		else:
			path = os.environ['PATH']

		paths = map(os.path.dirname, files)
		# , '/usr/local/lib/node_modules/css-flip-auto/bin/css-flip'
		self.window.run_command('exec', {
			'cmd': list( map(os.path.expanduser, ['cssrtl']))  + settings.get('options', []),
			'path': path,
			'working_dir' : paths[0] + '/../',
			'line_regex': settings.get('line_regex', '.*// Line ([0-9]*), Pos ([0-9]*)$'),
			'file_regex': settings.get('file_regex', '(^[^# ]+.*$)')
		})

class CssrtlCommand(sublime_plugin.WindowCommand):

	def run(self):
		self.window.run_command('cssrtl_exec', {
			'files': [self.window.active_view().file_name()]
		})
	def is_visible(self):
		pattern = re.compile(r'(^.*\.css$)')
		return pattern.match(self.window.active_view().file_name())