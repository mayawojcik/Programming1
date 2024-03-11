import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.LavenderBlush
		self._button1.Font = System.Drawing.Font("Myanmar Text", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.HotPink
		self._button1.Location = System.Drawing.Point(108, 202)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(157, 61)
		self._button1.TabIndex = 0
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.LavenderBlush
		self._button2.Font = System.Drawing.Font("Myanmar Text", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.HotPink
		self._button2.Location = System.Drawing.Point(293, 202)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(157, 61)
		self._button2.TabIndex = 1
		self._button2.Text = "button2"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.LavenderBlush
		self._button3.Font = System.Drawing.Font("Myanmar Text", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.HotPink
		self._button3.Location = System.Drawing.Point(479, 202)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(157, 61)
		self._button3.TabIndex = 2
		self._button3.Text = "button3"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.LavenderBlush
		self._label1.Font = System.Drawing.Font("Yu Gothic UI", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.HotPink
		self._label1.Location = System.Drawing.Point(164, 55)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(400, 120)
		self._label1.TabIndex = 3
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self.ClientSize = System.Drawing.Size(750, 324)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Favquote"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self._label1.Text = "If you play stupid games, you win stupid prizes"

	def Button2Click(self, sender, e):
		self._label1.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()