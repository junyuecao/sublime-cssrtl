import sublime, sublime_plugin, re, os

SETTINGS_FILE = 'CSSRTL.sublime-settings'
class CssrtlExecCommand(sublime_plugin.WindowCommand):
	def run(self, files=[], reverse='',flip=False):

		settings = sublime.load_settings(SETTINGS_FILE)
		if os.name == "posix":
			path = "/usr/local/bin:" + os.environ['PATH']
			cmd = 'cssrtl'
		else:
			path = os.environ['PATH']
			cmd = 'cssrtl.cmd'

		paths =map (os.path.dirname, map(os.path.dirname, files))
		opt = list( map(os.path.expanduser, [cmd]))


		if bool(reverse.strip()):
			opt.append(reverse)
		if flip:
			opt = opt + files

		print os.path.join(paths[0])
		print opt
		# , '/usr/local/lib/node_modules/css-flip-auto/bin/css-flip'
		self.window.run_command('my_exec', {
			'cmd': opt,
			'path': path,
			'working_dir' : os.path.join(paths[0]),
			'line_regex': settings.get('line_regex', '.*// Line ([0-9]*), Pos ([0-9]*)$'),
			'file_regex': settings.get('file_regex', '(^[^# ]+.*$)'),
			'flip' : flip
		})

class CssrtlCommand(sublime_plugin.WindowCommand):

	def run(self,reverse='', flip=False, file=None):
		file=self.window.active_view().file_name()
		self.window.active_view().run_command('save');
		self.window.run_command('cssrtl_exec', {
			'files': [file],
			'reverse' : reverse,
			'flip' : flip
		})
	def is_visible(self):
		pattern = re.compile(r'(^.*\.css$)')
		return pattern.match(self.window.active_view().file_name())
