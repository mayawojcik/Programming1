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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._listBox1 = System.Windows.Forms.ListBox()
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.FromArgb(255, 224, 192)
		self._button1.Location = System.Drawing.Point(270, 36)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(146, 90)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.FromArgb(255, 224, 192)
		self._button2.Location = System.Drawing.Point(270, 132)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(146, 90)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
		self._button3.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.FromArgb(255, 224, 192)
		self._button3.Location = System.Drawing.Point(270, 228)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(146, 90)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
		self._textBox1.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.ForeColor = System.Drawing.Color.FromArgb(255, 224, 192)
		self._textBox1.Location = System.Drawing.Point(37, 285)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(186, 33)
		self._textBox1.TabIndex = 3
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.White
		self._listBox1.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.ForeColor = System.Drawing.Color.FromArgb(255, 192, 128)
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 19
		self._listBox1.Location = System.Drawing.Point(12, 12)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(240, 213)
		self._listBox1.TabIndex = 4
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.White
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.FromArgb(255, 192, 128)
		self._label1.Location = System.Drawing.Point(37, 242)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(186, 31)
		self._label1.TabIndex = 5
		self._label1.Text = "Input test value:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
		self.ClientSize = System.Drawing.Size(435, 342)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "prog152b"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()
		self._textBox1.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()

	def Button1Click(self, sender, e):
		heading = "Even Integer:" + "\t" + "Sum:"
		self._listBox1.Items.Add(heading)
		testv = self._textBox1.Text
		for num in range(2, 2):
			evenint = num
			msg1 = "evenint"
			self._listBox1.Items.Add(msg1)