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
		self._label5 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self._button1.Location = System.Drawing.Point(62, 278)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(122, 46)
		self._button1.TabIndex = 0
		self._button1.Text = "print"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self._button2.Location = System.Drawing.Point(219, 277)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(122, 46)
		self._button2.TabIndex = 1
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._button3.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self._button3.Location = System.Drawing.Point(373, 277)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(122, 46)
		self._button3.TabIndex = 2
		self._button3.Text = "exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.White
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._label1.Location = System.Drawing.Point(62, 69)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(180, 37)
		self._label1.TabIndex = 3
		self._label1.Text = "radius:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.White
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._label2.Location = System.Drawing.Point(62, 128)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(180, 37)
		self._label2.TabIndex = 4
		self._label2.Text = "circumference:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.White
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._label3.Location = System.Drawing.Point(62, 186)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(180, 37)
		self._label3.TabIndex = 5
		self._label3.Text = "area:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.SlateBlue
		self._label4.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.White
		self._label4.Location = System.Drawing.Point(307, 128)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(188, 37)
		self._label4.TabIndex = 6
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.SlateBlue
		self._label5.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.White
		self._label5.Location = System.Drawing.Point(307, 186)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(188, 37)
		self._label5.TabIndex = 7
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self._textBox1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.ForeColor = System.Drawing.Color.White
		self._textBox1.Location = System.Drawing.Point(307, 71)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(188, 35)
		self._textBox1.TabIndex = 8
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self.ClientSize = System.Drawing.Size(559, 363)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "lang54c"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		radius = float(self._textBox1.Text)
		pi = 3.14159
		circumference = 2*pi*radius 
		circumference = round(circumference, 3)
		area = pi*radius**2 
		area = round(area, 3)		
		self._label4.Text = str(circumference)
		self._label5.Text = str(area)

	def MainFormLoad(self, sender, e):
		pass

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._label4.Text = ""
		self._label5.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()