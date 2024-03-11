﻿import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._label5 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.OrangeRed
		self._label1.Location = System.Drawing.Point(32, 53)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(102, 32)
		self._label1.TabIndex = 0
		self._label1.Text = "Pounds:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.OrangeRed
		self._label2.Location = System.Drawing.Point(32, 96)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(102, 32)
		self._label2.TabIndex = 1
		self._label2.Text = "Shillings:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.OrangeRed
		self._label3.Location = System.Drawing.Point(32, 140)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(102, 32)
		self._label3.TabIndex = 2
		self._label3.Text = "Pence:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.OrangeRed
		self._label4.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.FromArgb(255, 224, 192)
		self._label4.Location = System.Drawing.Point(55, 259)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(213, 38)
		self._label4.TabIndex = 3
		self._label4.Text = "Decimal Pounds:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label4.Click += self.Label4Click
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
		self._textBox1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.ForeColor = System.Drawing.Color.OrangeRed
		self._textBox1.Location = System.Drawing.Point(159, 53)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 35)
		self._textBox1.TabIndex = 4
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
		self._textBox2.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.ForeColor = System.Drawing.Color.OrangeRed
		self._textBox2.Location = System.Drawing.Point(159, 96)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 35)
		self._textBox2.TabIndex = 5
		# 
		# textBox3
		# 
		self._textBox3.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
		self._textBox3.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.ForeColor = System.Drawing.Color.OrangeRed
		self._textBox3.Location = System.Drawing.Point(159, 140)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 35)
		self._textBox3.TabIndex = 6
		# 
		# groupBox1
		# 
		self._groupBox1.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
		self._groupBox1.Controls.Add(self._textBox3)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Controls.Add(self._textBox2)
		self._groupBox1.Controls.Add(self._label2)
		self._groupBox1.Controls.Add(self._textBox1)
		self._groupBox1.Controls.Add(self._label3)
		self._groupBox1.Location = System.Drawing.Point(23, 21)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(292, 225)
		self._groupBox1.TabIndex = 7
		self._groupBox1.TabStop = False
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
		self._label5.Font = System.Drawing.Font("Microsoft YaHei", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.OrangeRed
		self._label5.Location = System.Drawing.Point(77, 308)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(167, 35)
		self._label5.TabIndex = 8
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.Coral
		self._button1.Location = System.Drawing.Point(334, 21)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(192, 99)
		self._button1.TabIndex = 9
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.Coral
		self._button2.Location = System.Drawing.Point(334, 132)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(192, 99)
		self._button2.TabIndex = 10
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
		self._button3.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.Coral
		self._button3.Location = System.Drawing.Point(334, 244)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(192, 99)
		self._button3.TabIndex = 11
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Coral
		self.ClientSize = System.Drawing.Size(548, 376)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._groupBox1)
		self.Controls.Add(self._label4)
		self.Name = "MainForm"
		self.Text = "Prog65h"
		self._groupBox1.ResumeLayout(False)
		self._groupBox1.PerformLayout()
		self.ResumeLayout(False)


	def Label4Click(self, sender, e):
		pass

	def Button3Click(self, sender, e):
		Application.Exit()

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._label5.Text = ""

	def Button1Click(self, sender, e):
		num1 = float(self._textBox1.Text)
		num2 = float(self._textBox2.Text)
		num3 = float(self._textBox3.Text)
		Pence = (num3 / (12 * 20)) + num2 / 20
		DecimalPound = num1 + Pence
		DecimalPound = round(DecimalPound, 2)
		self._label5.Text = str(DecimalPound)
		
		