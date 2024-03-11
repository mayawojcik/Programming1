import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.LightCyan
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.DarkOrchid
		self._label1.Location = System.Drawing.Point(70, 35)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(510, 343)
		self._label1.TabIndex = 0
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.LightCyan
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.DarkOrchid
		self._button1.Location = System.Drawing.Point(659, 33)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(179, 85)
		self._button1.TabIndex = 1
		self._button1.Text = "click"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.LightCyan
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.DarkOrchid
		self._button2.Location = System.Drawing.Point(659, 164)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(179, 85)
		self._button2.TabIndex = 2
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.LightCyan
		self._button3.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.DarkOrchid
		self._button3.Location = System.Drawing.Point(659, 304)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(179, 85)
		self._button3.TabIndex = 3
		self._button3.Text = "exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightBlue
		self.ClientSize = System.Drawing.Size(952, 417)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "phonenumbers"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self._label1.Text = "McDonald's-(847) 439-6141\n Taco Bell-(847) 298-2355\n Ross-(847) 795-2704\n Target-(847) 795-1760\n Culver's-(847) 635-2005"

	def Button2Click(self, sender, e):
		self._label1.Text = ""

	def Button3Click(self, sender, e):
		Applications.Exit()