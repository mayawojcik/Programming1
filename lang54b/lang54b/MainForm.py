import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.Pink
		self._textBox1.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.ForeColor = System.Drawing.Color.MediumOrchid
		self._textBox1.Location = System.Drawing.Point(93, 44)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 33)
		self._textBox1.TabIndex = 0
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.Pink
		self._textBox2.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.ForeColor = System.Drawing.Color.MediumOrchid
		self._textBox2.Location = System.Drawing.Point(93, 101)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 33)
		self._textBox2.TabIndex = 1
		# 
		# textBox3
		# 
		self._textBox3.BackColor = System.Drawing.Color.Pink
		self._textBox3.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.ForeColor = System.Drawing.Color.MediumOrchid
		self._textBox3.Location = System.Drawing.Point(264, 44)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 33)
		self._textBox3.TabIndex = 2
		# 
		# textBox4
		# 
		self._textBox4.BackColor = System.Drawing.Color.Pink
		self._textBox4.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox4.ForeColor = System.Drawing.Color.MediumOrchid
		self._textBox4.Location = System.Drawing.Point(264, 101)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(100, 33)
		self._textBox4.TabIndex = 3
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Pink
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.DarkOrchid
		self._button1.Location = System.Drawing.Point(15, 293)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(122, 47)
		self._button1.TabIndex = 4
		self._button1.Text = "caluclate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Pink
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.DarkOrchid
		self._button2.Location = System.Drawing.Point(171, 293)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(122, 47)
		self._button2.TabIndex = 5
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Pink
		self._button3.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.DarkOrchid
		self._button3.Location = System.Drawing.Point(328, 293)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(122, 47)
		self._button3.TabIndex = 6
		self._button3.Text = "exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.Thistle
		self._label1.Location = System.Drawing.Point(93, 162)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 29)
		self._label1.TabIndex = 7
		self._label1.Text = "sum:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.Thistle
		self._label2.Location = System.Drawing.Point(93, 209)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 31)
		self._label2.TabIndex = 8
		self._label2.Text = "average:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Pink
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.DarkOrchid
		self._label3.Location = System.Drawing.Point(249, 157)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(127, 42)
		self._label3.TabIndex = 9
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label3.Click += self.Label3Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Pink
		self._label4.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.DarkOrchid
		self._label4.Location = System.Drawing.Point(249, 209)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(127, 44)
		self._label4.TabIndex = 10
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label4.Click += self.Label4Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.MediumOrchid
		self.ClientSize = System.Drawing.Size(462, 415)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "lang54b"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button3Click(self, sender, e):
		Application.Exit()

	def Button1Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		num3 = int(self._textBox3.Text)
		num4 = int(self._textBox4.Text)
		S = num1 + num2 + num3 + num4
		average = S / 4.0
		self._label3.Text = str(S)
		self._label4.Text = str(average)
	

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._textBox4.Text = ""
		self._label3.Text = ""
		self._label4.Text = ""

	def Label3Click(self, sender, e):
		pass

	def Label4Click(self, sender, e):
		pass