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
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.CornflowerBlue
		self._textBox1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.ForeColor = System.Drawing.Color.RoyalBlue
		self._textBox1.Location = System.Drawing.Point(40, 72)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 35)
		self._textBox1.TabIndex = 0
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.CornflowerBlue
		self._textBox2.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.ForeColor = System.Drawing.Color.RoyalBlue
		self._textBox2.Location = System.Drawing.Point(184, 72)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 35)
		self._textBox2.TabIndex = 1
		# 
		# textBox3
		# 
		self._textBox3.BackColor = System.Drawing.Color.CornflowerBlue
		self._textBox3.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.ForeColor = System.Drawing.Color.RoyalBlue
		self._textBox3.Location = System.Drawing.Point(327, 72)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 35)
		self._textBox3.TabIndex = 2
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.AliceBlue
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.SystemColors.InactiveCaption
		self._label1.Location = System.Drawing.Point(117, 19)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(236, 37)
		self._label1.TabIndex = 3
		self._label1.Text = "Input integers:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.AliceBlue
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.SystemColors.InactiveCaption
		self._label2.Location = System.Drawing.Point(73, 119)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(181, 35)
		self._label2.TabIndex = 4
		self._label2.Text = " positive roots:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.AliceBlue
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.SystemColors.InactiveCaption
		self._label3.Location = System.Drawing.Point(277, 119)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(118, 35)
		self._label3.TabIndex = 5
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.CornflowerBlue
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.RoyalBlue
		self._button1.Location = System.Drawing.Point(31, 272)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(199, 51)
		self._button1.TabIndex = 6
		self._button1.Text = "Clear"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.CornflowerBlue
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.RoyalBlue
		self._button2.Location = System.Drawing.Point(236, 272)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(202, 51)
		self._button2.TabIndex = 7
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.CornflowerBlue
		self._button3.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.RoyalBlue
		self._button3.Location = System.Drawing.Point(31, 214)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(407, 52)
		self._button3.TabIndex = 8
		self._button3.Text = "Calculate"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.AliceBlue
		self._label4.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.SystemColors.InactiveCaption
		self._label4.Location = System.Drawing.Point(73, 165)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(181, 35)
		self._label4.TabIndex = 9
		self._label4.Text = " negative roots:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.AliceBlue
		self._label5.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.SystemColors.InactiveCaption
		self._label5.Location = System.Drawing.Point(277, 165)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(118, 35)
		self._label5.TabIndex = 10
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightSteelBlue
		self.ClientSize = System.Drawing.Size(465, 335)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "lang58b"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button3Click(self, sender, e):
		A = int(self._textBox1.Text)
		B = int(self._textBox2.Text)
		C = int(self._textBox3.Text)
		positiveRoot = (-B + math.sqrt(B**2 - 4*A*C))/2*A
		negativeRoot = (-B - math.sqrt(B**2 - 4*A*C))/2*A
		# + - * / %    ** pow   ** divide and round down
		self._label3.Text = str(positiveRoot)
		self._label5.Text = str(negativeRoot)
		

	def Button2Click(self, sender, e):
		Application.Exit()

	def Button1Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._label3.Text = ""
		self._label5.Text = ""