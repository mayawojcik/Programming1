import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._Enter_Three_Test_Scores = System.Windows.Forms.ListBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label5 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# Enter_Three_Test_Scores
		# 
		self._Enter_Three_Test_Scores.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self._Enter_Three_Test_Scores.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._Enter_Three_Test_Scores.FormattingEnabled = True
		self._Enter_Three_Test_Scores.Location = System.Drawing.Point(25, 12)
		self._Enter_Three_Test_Scores.Name = "Enter_Three_Test_Scores"
		self._Enter_Three_Test_Scores.Size = System.Drawing.Size(308, 262)
		self._Enter_Three_Test_Scores.TabIndex = 0
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._button1.Location = System.Drawing.Point(57, 286)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(119, 76)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._button2.Location = System.Drawing.Point(182, 286)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(117, 35)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self._button3.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._button3.Location = System.Drawing.Point(182, 327)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(117, 35)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.White
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._label1.Location = System.Drawing.Point(57, 48)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 33)
		self._label1.TabIndex = 4
		self._label1.Text = "Score1:"
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.ForeColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._textBox1.Location = System.Drawing.Point(199, 48)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 33)
		self._textBox1.TabIndex = 9
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.White
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._label2.Location = System.Drawing.Point(57, 101)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 33)
		self._label2.TabIndex = 10
		self._label2.Text = "Score2:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.White
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._label3.Location = System.Drawing.Point(57, 151)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 33)
		self._label3.TabIndex = 11
		self._label3.Text = "Score3:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.White
		self._label4.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._label4.Location = System.Drawing.Point(57, 203)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 32)
		self._label4.TabIndex = 12
		self._label4.Text = "Average:"
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.ForeColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._textBox2.Location = System.Drawing.Point(199, 101)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 33)
		self._textBox2.TabIndex = 13
		# 
		# textBox3
		# 
		self._textBox3.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.ForeColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._textBox3.Location = System.Drawing.Point(199, 151)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 33)
		self._textBox3.TabIndex = 14
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.White
		self._label5.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._label5.Location = System.Drawing.Point(199, 203)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 32)
		self._label5.TabIndex = 15
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self.ClientSize = System.Drawing.Size(358, 385)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._Enter_Three_Test_Scores)
		self.Name = "MainForm"
		self.Text = "scoreavg"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	def MainFormLoad(self, sender, e):
		pass

	def Label5Click(self, sender, e):
		pass

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._label5.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()

	def Button1Click(self, sender, e):
		s1 = float(self._textBox1.Text)
		s2 = float(self._textBox2.Text)
		s3 = float(self._textBox3.Text)
		average = (s1 + s2 + s3) / 3
		average = round(average, 2)
		self._label5.Text = str(average)