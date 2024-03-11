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
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(29, 212)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(109, 56)
		self._button1.TabIndex = 0
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(154, 212)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(109, 56)
		self._button2.TabIndex = 1
		self._button2.Text = "button2"
		self._button2.UseVisualStyleBackColor = True
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(278, 212)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(109, 56)
		self._button3.TabIndex = 2
		self._button3.Text = "button3"
		self._button3.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self.ClientSize = System.Drawing.Size(423, 305)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "lang54cGUI"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		radius = float(self._textBox1.Text)
		circumference = 2*radius
		area = 3.14159*radius**2 
		self._label4.Text = str(circumference)
		self._label5.Text = str(area)