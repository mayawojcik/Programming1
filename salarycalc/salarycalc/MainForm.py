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
		self._label5 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.ForeColor = System.Drawing.Color.FromArgb(255, 128, 255)
		self._textBox1.Location = System.Drawing.Point(313, 55)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(134, 33)
		self._textBox1.TabIndex = 0
		self._textBox1.TextChanged += self.TextBox1TextChanged
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.ForeColor = System.Drawing.Color.FromArgb(255, 128, 255)
		self._textBox2.Location = System.Drawing.Point(313, 114)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(134, 33)
		self._textBox2.TabIndex = 1
		self._textBox2.TextChanged += self.TextBox2TextChanged
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.White
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.FromArgb(255, 128, 255)
		self._label1.Location = System.Drawing.Point(26, 52)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(232, 38)
		self._label1.TabIndex = 2
		self._label1.Text = "Annual salary:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.White
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.FromArgb(255, 128, 255)
		self._label2.Location = System.Drawing.Point(26, 111)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(232, 38)
		self._label2.TabIndex = 3
		self._label2.Text = "Pay periods per year:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.White
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.FromArgb(255, 128, 255)
		self._label3.Location = System.Drawing.Point(26, 168)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(232, 38)
		self._label3.TabIndex = 4
		self._label3.Text = "Salary per pay period:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.White
		self._label4.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.FromArgb(255, 128, 255)
		self._label4.Location = System.Drawing.Point(313, 168)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(134, 38)
		self._label4.TabIndex = 5
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.FromArgb(255, 128, 255)
		self._button1.Location = System.Drawing.Point(142, 232)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(210, 53)
		self._button1.TabIndex = 6
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# label5
		# 
		self._label5.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.FromArgb(255, 128, 255)
		self._label5.Location = System.Drawing.Point(119, 9)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(256, 35)
		self._label5.TabIndex = 7
		self._label5.Text = "Salary Calculator"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self.ClientSize = System.Drawing.Size(489, 307)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "salarycalc"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		A = float(self._textBox1.Text)
		B = float(self._textBox2.Text)
		Salary = A / B
		Salary = round(Salary, 2)
		self._label4.Text = str(Salary)
		

	def TextBox1TextChanged(self, sender, e):
		pass

	def TextBox2TextChanged(self, sender, e):
		pass