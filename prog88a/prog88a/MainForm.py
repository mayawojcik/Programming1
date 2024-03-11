import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._textBox6 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._label13 = System.Windows.Forms.Label()
		self._label14 = System.Windows.Forms.Label()
		self._label15 = System.Windows.Forms.Label()
		self._label16 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._label1.Location = System.Drawing.Point(2, 19)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(124, 31)
		self._label1.TabIndex = 0
		self._label1.Text = "Num1:"
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.ForeColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._textBox1.Location = System.Drawing.Point(132, 15)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(109, 35)
		self._textBox1.TabIndex = 1
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._label4.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._label4.Location = System.Drawing.Point(2, 240)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(124, 31)
		self._label4.TabIndex = 4
		self._label4.Text = "Average"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._label5.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._label5.Location = System.Drawing.Point(2, 198)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(124, 31)
		self._label5.TabIndex = 5
		self._label5.Text = "Product:"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._label6.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._label6.Location = System.Drawing.Point(2, 153)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(124, 31)
		self._label6.TabIndex = 6
		self._label6.Text = "Difference:"
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._label7.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._label7.Location = System.Drawing.Point(2, 109)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(124, 31)
		self._label7.TabIndex = 7
		self._label7.Text = "Sum:"
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._label8.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._label8.Location = System.Drawing.Point(2, 64)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(124, 31)
		self._label8.TabIndex = 8
		self._label8.Text = "Num2:"
		# 
		# textBox6
		# 
		self._textBox6.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox6.ForeColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._textBox6.Location = System.Drawing.Point(132, 60)
		self._textBox6.Name = "textBox6"
		self._textBox6.Size = System.Drawing.Size(109, 35)
		self._textBox6.TabIndex = 13
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._label2.Location = System.Drawing.Point(2, 283)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(124, 31)
		self._label2.TabIndex = 14
		self._label2.Text = "Distance:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._label3.Location = System.Drawing.Point(2, 372)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(124, 31)
		self._label3.TabIndex = 15
		self._label3.Text = "Min:"
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._label9.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._label9.Location = System.Drawing.Point(2, 328)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(124, 31)
		self._label9.TabIndex = 16
		self._label9.Text = "Max:"
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._button1.Location = System.Drawing.Point(247, 30)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(114, 109)
		self._button1.TabIndex = 20
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._button2.Location = System.Drawing.Point(247, 153)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(114, 108)
		self._button2.TabIndex = 21
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self._button3.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._button3.Location = System.Drawing.Point(247, 278)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(114, 107)
		self._button3.TabIndex = 22
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.White
		self._label10.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.ForeColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._label10.Location = System.Drawing.Point(132, 109)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(109, 31)
		self._label10.TabIndex = 23
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.White
		self._label11.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.ForeColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._label11.Location = System.Drawing.Point(132, 153)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(109, 31)
		self._label11.TabIndex = 24
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.Color.White
		self._label12.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label12.ForeColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._label12.Location = System.Drawing.Point(132, 198)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(109, 31)
		self._label12.TabIndex = 25
		# 
		# label13
		# 
		self._label13.BackColor = System.Drawing.Color.White
		self._label13.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label13.ForeColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._label13.Location = System.Drawing.Point(132, 240)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(109, 31)
		self._label13.TabIndex = 26
		# 
		# label14
		# 
		self._label14.BackColor = System.Drawing.Color.White
		self._label14.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label14.ForeColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._label14.Location = System.Drawing.Point(132, 283)
		self._label14.Name = "label14"
		self._label14.Size = System.Drawing.Size(109, 31)
		self._label14.TabIndex = 27
		# 
		# label15
		# 
		self._label15.BackColor = System.Drawing.Color.White
		self._label15.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label15.ForeColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._label15.Location = System.Drawing.Point(132, 328)
		self._label15.Name = "label15"
		self._label15.Size = System.Drawing.Size(109, 31)
		self._label15.TabIndex = 28
		# 
		# label16
		# 
		self._label16.BackColor = System.Drawing.Color.White
		self._label16.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label16.ForeColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._label16.Location = System.Drawing.Point(132, 372)
		self._label16.Name = "label16"
		self._label16.Size = System.Drawing.Size(109, 31)
		self._label16.TabIndex = 29
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self.ClientSize = System.Drawing.Size(373, 434)
		self.Controls.Add(self._label16)
		self.Controls.Add(self._label15)
		self.Controls.Add(self._label14)
		self.Controls.Add(self._label13)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox6)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "prog88a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		num1 = float(self._textBox1.Text)
		num2 = float(self._textBox6.Text)
		Sum = num1 + num2
		Diff = num1 - num2
		# TODO : finish product and average
		Product = num1 * num2
		Average = Sum / 2
		AbsDiff = abs(Diff)
		Max = 0
		Min = 0
		if num1 >= num2:
			Max = num1
		else:  # Otherwise...
			Max = num2
			
		if Max == num1: # If Max has the same value as num1
			Min = num2
		else:
			Min = num1
			
		self._label15.Text = str(Max)
		self._label16.Text = str(Min)
		self._label10.Text = str(Sum)
		self._label11.Text = str(Diff)
		self._label12.Text = str(Product)
		self._label13.Text = str(Average)
		self._label14.Text = str(AbsDiff)

	def Button3Click(self, sender, e):
		Application.Exit()

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox6.Text = ""
		self._label10.Text = ""
		self._label11.Text = ""
		self._label12.Text = ""
		self._label13.Text = ""
		self._label14.Text = ""
		self._label15.Text = ""
		self._label16.Text = ""