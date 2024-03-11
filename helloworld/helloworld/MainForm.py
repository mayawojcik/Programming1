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
		self._label1.BackColor = System.Drawing.Color.Pink
		self._label1.Font = System.Drawing.Font("Times New Roman", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(169, 60)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(236, 87)
		self._label1.TabIndex = 0
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Tahoma", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(84, 172)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(117, 56)
		self._button1.TabIndex = 1
		self._button1.Text = "show"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Tahoma", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(228, 172)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(117, 56)
		self._button2.TabIndex = 2
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Tahoma", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(375, 172)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(117, 56)
		self._button3.TabIndex = 3
		self._button3.Text = "exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.MistyRose
		self.ClientSize = System.Drawing.Size(562, 298)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "helloworld"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)


	def MainFormLoad(self, sender, e):
		pass


	def Button1Click(self, sender, e):
		self._label1.Text = "Hello, world!"
	
	
	def Button2Click(self, sender, e):
		self._label1.Text = ""
		
		
	def Button3Click(self, sender, e):
		Application.Exit()