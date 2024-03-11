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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(72, 19)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(196, 31)
		self._label1.TabIndex = 0
		self._label1.Text = "length:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(72, 56)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(196, 31)
		self._label2.TabIndex = 1
		self._label2.Text = "width:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
	
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(349, 24)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 2
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(349, 56)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 3
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(72, 156)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(196, 31)
		self._label3.TabIndex = 4
		self._label3.Text = "area:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._label4.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(72, 193)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(196, 31)
		self._label4.TabIndex = 5
		self._label4.Text = "perimeter:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._label5.Location = System.Drawing.Point(349, 164)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 6
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._label6.Location = System.Drawing.Point(349, 201)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 7
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.FromArgb(0, 0, 192)
		self._button1.Location = System.Drawing.Point(44, 269)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(127, 47)
		self._button1.TabIndex = 8
		self._button1.Text = "calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.FromArgb(0, 0, 192)
		self._button2.Location = System.Drawing.Point(217, 269)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(127, 47)
		self._button2.TabIndex = 9
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.FromArgb(0, 0, 192)
		self._button3.Location = System.Drawing.Point(394, 269)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(127, 47)
		self._button3.TabIndex = 10
		self._button3.Text = "exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self.ClientSize = System.Drawing.Size(552, 353)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "prog52a"
		self.ResumeLayout(False)
		self.PerformLayout()



	def Button1Click(self, sender, e):
		length = int(self._textBox1.Text)
		width = int(self._textBox2.Text)
		area = length * width
		perim = 2 * length + 2 * width
		self._label5.Text = str(area)
		self._label6.Text = str(perim)
		# + - * / %    ** pow  // divide & round down
		# int (Integer): a whole number pos/neg
		# float (Floating-point Number): anu number w/ a decimal
		# str (String): a string of text

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label5.Text = ""
		self._label6.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()