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
		self._button1 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._button2 = System.Windows.Forms.Button()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.White
		self._label1.Location = System.Drawing.Point(55, 38)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(225, 33)
		self._label1.TabIndex = 0
		self._label1.Text = "Annual Salary:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.White
		self._label2.Location = System.Drawing.Point(23, 78)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(225, 33)
		self._label2.TabIndex = 1
		self._label2.Text = "Pay periods per year:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.White
		self._label3.Location = System.Drawing.Point(23, 118)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(225, 33)
		self._label3.TabIndex = 2
		self._label3.Text = "Salary per pay period:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.White
		self._button1.Location = System.Drawing.Point(90, 175)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(215, 37)
		self._button1.TabIndex = 3
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.White
		self._textBox1.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.ForeColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._textBox1.Location = System.Drawing.Point(254, 38)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 33)
		self._textBox1.TabIndex = 4
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.White
		self._textBox2.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.ForeColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._textBox2.Location = System.Drawing.Point(254, 78)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 33)
		self._textBox2.TabIndex = 5
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._button2.ForeColor = System.Drawing.Color.White
		self._button2.Location = System.Drawing.Point(156, 218)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(82, 23)
		self._button2.TabIndex = 7
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.White
		self._label4.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._label4.Location = System.Drawing.Point(254, 118)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 33)
		self._label4.TabIndex = 8
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self.ClientSize = System.Drawing.Size(393, 276)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "salarycalc153"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button2Click(self, sender, e):
		Application.Exit()

	def Button1Click(self, sender, e):
		annsalary = str(self._textBox1.Text)
		pppy = str(self._textBox2.Text)
		sppy = annsalary / pppy
		self._label4.Text = sppy