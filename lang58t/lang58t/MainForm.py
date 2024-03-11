import math
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
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._label13 = System.Windows.Forms.Label()
		self._label14 = System.Windows.Forms.Label()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.FromArgb(255, 192, 192)
		self._button1.Location = System.Drawing.Point(264, 12)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(106, 50)
		self._button1.TabIndex = 0
		self._button1.Text = "Clear"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.FromArgb(255, 192, 192)
		self._button2.Location = System.Drawing.Point(378, 12)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(103, 50)
		self._button2.TabIndex = 1
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
		self._button3.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.FromArgb(255, 192, 192)
		self._button3.Location = System.Drawing.Point(264, 67)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(217, 52)
		self._button3.TabIndex = 2
		self._button3.Text = "Calculate"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.FromArgb(255, 192, 192)
		self._label1.Location = System.Drawing.Point(6, 12)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(173, 37)
		self._label1.TabIndex = 3
		self._label1.Text = "Purchase price"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.FromArgb(255, 192, 192)
		self._label2.Location = System.Drawing.Point(6, 67)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(173, 38)
		self._label2.TabIndex = 4
		self._label2.Text = "Amount received"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.FromArgb(255, 192, 192)
		self._label3.Location = System.Drawing.Point(6, 120)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(173, 38)
		self._label3.TabIndex = 5
		self._label3.Text = "Change due"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.White
		self._label4.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.FromArgb(255, 192, 192)
		self._label4.Location = System.Drawing.Point(187, 120)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(71, 38)
		self._label4.TabIndex = 6
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
		self._textBox1.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.ForeColor = System.Drawing.Color.FromArgb(255, 128, 128)
		self._textBox1.Location = System.Drawing.Point(185, 15)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(73, 33)
		self._textBox1.TabIndex = 7
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
		self._textBox2.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.ForeColor = System.Drawing.Color.FromArgb(255, 128, 128)
		self._textBox2.Location = System.Drawing.Point(185, 67)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(73, 33)
		self._textBox2.TabIndex = 8
		# 
		# groupBox1
		# 
		self._groupBox1.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
		self._groupBox1.Controls.Add(self._label14)
		self._groupBox1.Controls.Add(self._label13)
		self._groupBox1.Controls.Add(self._label12)
		self._groupBox1.Controls.Add(self._label11)
		self._groupBox1.Controls.Add(self._label10)
		self._groupBox1.Controls.Add(self._label9)
		self._groupBox1.Controls.Add(self._label8)
		self._groupBox1.Controls.Add(self._label7)
		self._groupBox1.Controls.Add(self._label6)
		self._groupBox1.Controls.Add(self._label5)
		self._groupBox1.Location = System.Drawing.Point(13, 172)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(245, 181)
		self._groupBox1.TabIndex = 9
		self._groupBox1.TabStop = False
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.White
		self._label5.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.FromArgb(255, 128, 128)
		self._label5.Location = System.Drawing.Point(6, 16)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 0
		self._label5.Text = "Dollars:"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.White
		self._label6.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.Color.FromArgb(255, 128, 128)
		self._label6.Location = System.Drawing.Point(6, 48)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 1
		self._label6.Text = "Quarters:"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.White
		self._label7.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.ForeColor = System.Drawing.Color.FromArgb(255, 128, 128)
		self._label7.Location = System.Drawing.Point(6, 80)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(100, 23)
		self._label7.TabIndex = 2
		self._label7.Text = "Dimes:"
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.White
		self._label8.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.ForeColor = System.Drawing.Color.FromArgb(255, 128, 128)
		self._label8.Location = System.Drawing.Point(6, 112)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(100, 23)
		self._label8.TabIndex = 3
		self._label8.Text = "Nickels:"
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.White
		self._label9.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.ForeColor = System.Drawing.Color.FromArgb(255, 128, 128)
		self._label9.Location = System.Drawing.Point(6, 145)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(100, 23)
		self._label9.TabIndex = 4
		self._label9.Text = "Pennies"
		self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
		self._label10.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.ForeColor = System.Drawing.Color.FromArgb(196, 255, 172)
		self._label10.Location = System.Drawing.Point(123, 16)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(106, 23)
		self._label10.TabIndex = 10
		self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
		self._label11.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.ForeColor = System.Drawing.Color.FromArgb(196, 255, 172)
		self._label11.Location = System.Drawing.Point(123, 48)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(106, 23)
		self._label11.TabIndex = 11
		self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
		self._label12.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label12.ForeColor = System.Drawing.Color.FromArgb(196, 255, 172)
		self._label12.Location = System.Drawing.Point(123, 80)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(106, 23)
		self._label12.TabIndex = 12
		self._label12.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label13
		# 
		self._label13.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
		self._label13.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label13.ForeColor = System.Drawing.Color.FromArgb(196, 255, 172)
		self._label13.Location = System.Drawing.Point(123, 112)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(106, 23)
		self._label13.TabIndex = 13
		self._label13.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label14
		# 
		self._label14.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
		self._label14.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label14.ForeColor = System.Drawing.Color.FromArgb(196, 255, 172)
		self._label14.Location = System.Drawing.Point(123, 145)
		self._label14.Name = "label14"
		self._label14.Size = System.Drawing.Size(106, 23)
		self._label14.TabIndex = 14
		self._label14.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(196, 255, 172)
		self.ClientSize = System.Drawing.Size(493, 365)
		self.Controls.Add(self._groupBox1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "lang58t"
		self._groupBox1.ResumeLayout(False)
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button3Click(self, sender, e):
		num1 = float(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		Change = num2 - num1
		self._label4.Text = str(Change)
		Dollars = Change // 1
		self._label10.Text = str(Dollars)
		
		Change2 = Change - Dollars
		Quarters = Change2 // .25
		self._label11.Text = str(Quarters)
		
		Change3 = Change2 - (Quarters * .25)
		Dimes = Change3 // .10
		self._label12.Text = str(Dimes)
		
		Change4 = Change3 - (Dimes * .10)
		Nickles = Change4 // .05
		self._label13.Text = str(Nickles)
		
		Change5 = Change4 - (Nickles * .05)
		Pennies = (Change5 // .01)
		self._label14.Text = str(Pennies)
	
	

	def Button2Click(self, sender, e):
		Application.Exit()

	def Button1Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label4.Text = ""
		self._label10.Text = ""
		self._label11.Text = ""
		self._label12.Text = ""
		self._label13.Text = ""
		self._label14.Text = ""