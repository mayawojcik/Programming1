import math
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
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
		self._textBox1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(285, 22)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 35)
		self._textBox1.TabIndex = 0
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
		self._textBox2.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(285, 90)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 35)
		self._textBox2.TabIndex = 1
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
		self._label1.Font = System.Drawing.Font("Lucida Sans Typewriter", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.FromArgb(192, 0, 0)
		self._label1.Location = System.Drawing.Point(44, 22)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(197, 35)
		self._label1.TabIndex = 2
		self._label1.Text = "Speed limit:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
		self._label2.Font = System.Drawing.Font("Lucida Sans Typewriter", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.FromArgb(192, 0, 0)
		self._label2.Location = System.Drawing.Point(44, 90)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(197, 35)
		self._label2.TabIndex = 3
		self._label2.Text = "Vehicle speed:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
		self._label3.Font = System.Drawing.Font("Lucida Sans Typewriter", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.FromArgb(192, 0, 0)
		self._label3.Location = System.Drawing.Point(44, 157)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(197, 35)
		self._label3.TabIndex = 4
		self._label3.Text = "Ticket:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.FromArgb(192, 0, 0)
		self._label4.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.FromArgb(255, 192, 192)
		self._label4.Location = System.Drawing.Point(285, 157)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 35)
		self._label4.TabIndex = 5
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.Red
		self._button1.Location = System.Drawing.Point(12, 274)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(200, 64)
		self._button1.TabIndex = 6
		self._button1.Text = "Clear"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Red
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.FromArgb(192, 0, 0)
		self._button2.Location = System.Drawing.Point(218, 274)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(198, 64)
		self._button2.TabIndex = 7
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
		self._button3.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.FromArgb(255, 128, 128)
		self._button3.Location = System.Drawing.Point(13, 205)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(403, 63)
		self._button3.TabIndex = 8
		self._button3.Text = "Calculate"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
		self.ClientSize = System.Drawing.Size(428, 350)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "lang82a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label4.Text = ""

	def Button2Click(self, sender, e):
		Application.Exit()

	def Button3Click(self, sender, e):
		num1 = float(self._textBox1.Text)
		num2 = float(self._textBox2.Text)
		OverL = num2 - num1
		Fine = 20.00 + (OverL * 5.00)
		self._label4.Text = str(Fine)