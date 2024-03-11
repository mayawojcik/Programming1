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
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.LavenderBlush
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.DarkCyan
		self._label1.Location = System.Drawing.Point(42, 37)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(174, 34)
		self._label1.TabIndex = 0
		self._label1.Text = "Kilowatts used:"
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.DarkSlateGray
		self._textBox1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.ForeColor = System.Drawing.Color.DarkCyan
		self._textBox1.Location = System.Drawing.Point(242, 36)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(81, 35)
		self._textBox1.TabIndex = 1
		self._textBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
		self._textBox1.TextChanged += self.TextBox1TextChanged
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.LavenderBlush
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.DarkCyan
		self._label2.Location = System.Drawing.Point(42, 126)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(174, 36)
		self._label2.TabIndex = 2
		self._label2.Text = "Surcharge:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.LavenderBlush
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.DarkCyan
		self._label3.Location = System.Drawing.Point(42, 172)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(174, 36)
		self._label3.TabIndex = 3
		self._label3.Text = "Citytax:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.LavenderBlush
		self._label4.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.DarkCyan
		self._label4.Location = System.Drawing.Point(42, 218)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(174, 36)
		self._label4.TabIndex = 4
		self._label4.Text = "Total:"
		self._label4.Click += self.Label4Click
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.LavenderBlush
		self._label5.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.DarkCyan
		self._label5.Location = System.Drawing.Point(42, 268)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(174, 57)
		self._label5.TabIndex = 5
		self._label5.Text = "Total after May 20th:"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.DarkCyan
		self._label6.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.Color.DarkSlateGray
		self._label6.Location = System.Drawing.Point(242, 126)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(81, 36)
		self._label6.TabIndex = 6
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.DarkCyan
		self._label7.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.ForeColor = System.Drawing.Color.DarkSlateGray
		self._label7.Location = System.Drawing.Point(242, 279)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(81, 36)
		self._label7.TabIndex = 7
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.DarkCyan
		self._label8.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.ForeColor = System.Drawing.Color.DarkSlateGray
		self._label8.Location = System.Drawing.Point(242, 218)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(81, 36)
		self._label8.TabIndex = 8
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.DarkCyan
		self._label9.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.ForeColor = System.Drawing.Color.DarkSlateGray
		self._label9.Location = System.Drawing.Point(242, 172)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(81, 36)
		self._label9.TabIndex = 9
		self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Thistle
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.PaleVioletRed
		self._button1.Location = System.Drawing.Point(12, 339)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(163, 49)
		self._button1.TabIndex = 10
		self._button1.Text = "Clear"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Thistle
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.PaleVioletRed
		self._button2.Location = System.Drawing.Point(190, 339)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(164, 49)
		self._button2.TabIndex = 11
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Thistle
		self._button3.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.PaleVioletRed
		self._button3.Location = System.Drawing.Point(12, 394)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(342, 49)
		self._button3.TabIndex = 12
		self._button3.Text = "Calculate"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.LavenderBlush
		self._label10.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.ForeColor = System.Drawing.Color.DarkCyan
		self._label10.Location = System.Drawing.Point(42, 80)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(174, 36)
		self._label10.TabIndex = 13
		self._label10.Text = "Base rate:"
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.DarkCyan
		self._label11.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.ForeColor = System.Drawing.Color.DarkSlateGray
		self._label11.Location = System.Drawing.Point(242, 80)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(81, 36)
		self._label11.TabIndex = 14
		self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Thistle
		self.ClientSize = System.Drawing.Size(366, 455)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "lang93a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def TextBox1TextChanged(self, sender, e):
		pass

	def Label4Click(self, sender, e):
		pass

	def Button2Click(self, sender, e):
		Application.Exit()

	def Button1Click(self, sender, e):
		self._textBox1.Text = ""
		self._label6.Text = ""
		self._label7.Text = ""
		self._label8.Text = ""
		self._label9.Text = ""
		self._label11.Text = ""

	def Button3Click(self, sender, e):
		Watts = float(self._textBox1.Text)
		BaseRate = Watts * 0.0475
		BaseRate = round(BaseRate, 2)
		self._label11.Text = str(BaseRate)
		
		Surcharge = BaseRate * 0.10
		Surcharge = round(Surcharge, 2)
		self._label6.Text = str(Surcharge)
		
		Citytax = BaseRate * 0.03
		Citytax = round(Citytax, 2)
		self._label9.Text = str(Citytax)
		
		subTotal = BaseRate + Surcharge + Citytax
		subTotal = round(subTotal, 2)
		self._label8.Text = str(subTotal)
		
		Latepay = subTotal * 0.04
		Latepay = round(Latepay, 2)
		Total = Latepay + subTotal
		self._label7.Text = str(Total)
		
	
		
		